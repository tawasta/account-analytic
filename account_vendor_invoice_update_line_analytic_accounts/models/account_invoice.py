# -*- coding: utf-8 -*-
from odoo import fields, models, exceptions, _


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Default Analytic Account',
        readonly=True,
        states={'draft': [('readonly', False)]},
        help=('Informational analytic account related to the invoice')
    )

    def set_line_analytic_accounts(self):
        self.ensure_one()
        if not self.analytic_account_id:
            error = _('Please select a default analytic account first')
            raise exceptions.UserError(error)

        for line in self.invoice_line_ids:
            line.account_analytic_id = self.analytic_account_id.id
