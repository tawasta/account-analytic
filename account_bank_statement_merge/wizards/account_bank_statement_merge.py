# -*- coding: utf-8 -*-
from odoo import models, api, _
from odoo.exceptions import UserError


class AccountBankStatementMerge(models.TransientModel):
    _name = "account.bank.statement.merge"

    @api.multi
    def confirm(self):

        account_bank_statement = self.env['account.bank.statement']
        bank_statements = account_bank_statement.browse(
            self._context.get('active_ids')
        )

        statements_from = bank_statements.filtered(
            lambda r: "CAMT54" in r.name or "CAMT054" in r.name
        )

        statement_to = bank_statements.filtered(
            lambda r: "CAMT53" in r.name.upper() or "CAMT053" in r.name.upper()
        )

        if len(statement_to) > 1:
            raise UserError(_("Can't have several target statements (CAMT053)"))

        if statement_to.state != 'open':
            raise UserError(
                _("Target statement '%s' must be in 'open' state") %
                statement_to.name
            )

        for statement_from in statements_from:
            if statement_from.state != 'open':
                raise UserError(
                    _("Source statement '%s' must be in 'open' state") %
                    statement_from.name
                )

            account_bank_statement.bank_statement_merge(statement_from, statement_to)
