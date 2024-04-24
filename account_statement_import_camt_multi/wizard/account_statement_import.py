import base64
import logging

from lxml import etree

from odoo import models

_logger = logging.getLogger(__name__)


class AccountStatementImport(models.TransientModel):
    _inherit = "account.statement.import"

    def import_files_button(self):
        data_str = str(base64.b64decode(self.statement_file), "utf-8")
        xml_def = '<?xml version="1.0" encoding="UTF-8"?>'
        statements = data_str.split(xml_def)
        parser = etree.XMLParser(recover=True, remove_comments=True)

        for statement in statements:
            if not statement:
                # The split will result for the first item to be empty
                continue
            try:
                root = etree.fromstring(statement, parser=parser)
            except etree.XMLSyntaxError:
                # ABNAmro is known to mix up encodings
                root = etree.fromstring(
                    statement.decode("iso-8859-15").encode("utf-8"), parser=parser
                )
            if root is None:
                raise ValueError("Not a valid xml file, or not an xml file at all.")

            _logger.debug("Try parsing with camt.")

            # Collect Ntfctn instances to a list
            notifications = [etree.tostring(x) for x in root[0].findall(".//{*}Ntfctn")]

            # Remove all Ntfctn instances
            for n in root[0].findall(".//{*}Ntfctn"):
                n.getparent().remove(n)

            statement_str = etree.tostring(root, encoding="unicode")
            # Re-add xml definition
            statement_str = "{}{}".format(xml_def, statement_str)

            # Import all statements as they were standalone files
            for notification in notifications:
                data_file = statement_str.replace(
                    "</GrpHdr>", "</GrpHdr>{}".format(str(notification))
                )
                self.statement_file = base64.b64encode(
                    data_file.encode(encoding="UTF-8")
                )
                self._import_file()

        action = self.env.ref("account.action_bank_statement_tree").read()[0]

        return action

    def _find_additional_data(self, currency_code, account_number):
        # Auto-match the journal
        context = {}
        bank = self.env["res.partner.bank"].search(
            [("sanitized_acc_number", "=", account_number)]
        )
        if bank:
            context["journal_id"] = bank.journal_id.id

        return super(
            AccountStatementImport,
        )._find_additional_data(currency_code, account_number)
