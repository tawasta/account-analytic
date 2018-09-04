# -*- coding: utf-8 -*-
from odoo import fields, models, _, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Default Analytic Account',
        states={'draft': [('readonly', False)]},
        help=_('Informational analytic account related to the invoice')
    )

    @api.multi
    @api.onchange('analytic_account_id')
    def set_line_analytic_accounts(self):
        self.ensure_one()
        if self.analytic_account_id:
            for line in self.invoice_line_ids:
                line.account_analytic_id = self.analytic_account_id.id

    @api.multi
    @api.onchange('analytic_account_id')
    def set_analytic_tags(self):
        '''Additional onchange functionality if also
        account_vendor_invoice_update_line_analytic_tags is installed:
        update the analytic_tag_ids field which causes also the tag info
        to cascade to invoice lines '''
        self.ensure_one()
        if self.analytic_account_id and 'analytic_tag_ids' in self._fields:
            self.analytic_tag_ids \
                = self.analytic_account_id.tag_ids.mapped('id')
