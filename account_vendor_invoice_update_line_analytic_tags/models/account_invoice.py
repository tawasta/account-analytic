# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag',
        string='Default Analytic Tags',
        readonly=True,
        states={'draft': [('readonly', False)]},
        help=('Informational list of analytic tags related to the invoice')
    )

    def set_line_analytic_tags(self):
        self.ensure_one()
        if not self.analytic_tag_ids:
            error = _('Please select some default analytic tags first')
            raise exceptions.UserError(error)

        for line in self.invoice_line_ids:
            line.analytic_tag_ids \
                = [(6, 0, self.analytic_tag_ids.mapped('id'))]
