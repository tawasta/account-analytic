# -*- coding: utf-8 -*-
from odoo import models, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_open(self):
        for record in self:
            if record.type == 'in_invoice' and record.analytic_account_id:
                if record.comment:
                    record.comment = '%s\n%s' % (
                        record.comment, record.analytic_account_id.name
                    )
                else:
                    record.comment = record.analytic_account_id.name

        return super(AccountInvoice, self).action_invoice_open()
