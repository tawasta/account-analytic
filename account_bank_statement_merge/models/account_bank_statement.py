# -*- coding: utf-8 -*-
from odoo import models


class AccountBankStatement(models.Model):

    _inherit = "account.bank.statement"

    def action_merge_statements(self):
        """
        Automated action for merging bank statements
        """
        # Search all open bank statements
        statements = self.search([
            ('state', '=', 'open'),
        ], order='balance_end ASC')

        merged_keys = []

        for statement in statements:
            key = statement.date, statement.journal_id.id
            if key in merged_keys:
                # Already merged. Skip
                continue

            statement_to = self.search([
                ('journal_id', '=', statement.journal_id.id),
                ('date', '=', statement.date),
                ('id', '!=', statement.id)
            ], limit=1)

            if not statement_to:
                # No matching statement
                continue

            line_to = statement_to.line_ids.filtered(
                lambda r: round(r.amount, 2) == round(statement.balance_end, 2)
                and not r.partner_name
            )

            merged_keys.append(key)

            if len(line_to) > 1:
                # Multiple matching lines found. Skip this for now
                continue
            
            # Matching statement line found
            if line_to:
                # Remove the statement sum line
                line_to.unlink()

            # Move lines to new statement
            statement.line_ids.write({'statement_id': statement_to.id})

            # Confirm the old (empty) statement
            statement.state = 'confirm'

        return True
