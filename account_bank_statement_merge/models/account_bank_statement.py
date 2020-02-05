# -*- coding: utf-8 -*-
from odoo import models, _


class AccountBankStatement(models.Model):

    _name = 'account.bank.statement'
    _inherit = ['account.bank.statement', 'mail.thread', 'ir.needaction_mixin']

    def action_merge_statements(self):
        """
        Automated action for merging bank statements
        """
        # Search all open bank statements
        statements = self.search([
            ('state', '=', 'open'),
        ], order='total_entry_encoding ASC')

        merged_keys = []

        for statement_from in statements:
            key = statement_from.date, statement_from.journal_id.id
            if key in merged_keys:
                # Already merged. Skip
                continue

            statement_to = self.search([
                ('journal_id', '=', statement_from.journal_id.id),
                ('date', '=', statement_from.date),
                ('id', '!=', statement_from.id),
                ('total_entry_encoding', '>', statement_from.total_entry_encoding)
            ], limit=1)

            if not statement_to:
                # No matching statement
                continue

            line_to = statement_to.line_ids.filtered(
                lambda r: round(r.amount, 2) == round(
                    statement_from.balance_end, 2)
                and not r.partner_name
                and not r.partner_id
            )

            if len(line_to) > 1:
                # Multiple matching lines found. Skip this for now
                continue

            if line_to:
                # Matching statement line found
                # Remove the statement sum line
                line_content = "{date} {name} {amount} / {ref}".format(
                    date=line_to.date,
                    name=line_to.name,
                    amount=line_to.amount,
                    ref=line_to.ref or '',
                )

                line_msg = _("Statement line '{}' removed".format(line_content))
                line_to.unlink()
            else:
                # Don't move lines if no sum line is found
                line_msg = _("Warning! No matching statement line was found!")

            # Mark this statement as merged
            merged_keys.append(key)

            # Move lines to new statement
            for line in statement_from.line_ids:
                line_content = "{date} {name} {amount} / {ref}"\
                    .format(
                        date=line.date,
                        name=line.name,
                        amount=line.amount,
                        ref=line.ref or '',
                    )

                line.statement_id = statement_to.id
                msg = _("Merged line '{}' from {} to {}").format(
                        line_content,
                        statement_from.name,
                        statement_to.name,
                    )

                statement_from.message_post(msg)
                statement_to.message_post(msg)

            # Confirm the old (empty) statement
            statement_from.state = 'confirm'

            statement_to.message_post(line_msg)

        return True
