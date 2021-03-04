from lxml import etree
from odoo import api
from odoo import models


class AccountBankStatementImport(models.TransientModel):
    _inherit = "account.bank.statement.import"

    @api.model
    def _parse_file(self, data_file):
        data_str = str(data_file, "utf-8")
        statements = data_str.split('<?xml version="1.0" encoding="UTF-8"?>')
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

            res = super(AccountBankStatementImport, self)._parse_file(
                etree.tostring(root)
            )

            if statement == statements[-1]:
                # Return res for the last item
                return res

    def _find_additional_data(self, currency_code, account_number):
        context = {}
        bank = self.env["res.partner.bank"].search(
            [("sanitized_acc_number", "=", account_number)]
        )
        if bank:
            context["journal_id"] = bank.journal_id.id

        return super(
            AccountBankStatementImport, self.with_context(context)
        )._find_additional_data(currency_code, account_number)
