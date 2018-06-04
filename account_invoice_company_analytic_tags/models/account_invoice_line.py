# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoiceLine(models.Model):

    _inherit = 'account.invoice.line'

    @api.model
    def _get_default_analytic_tag_ids(self):
        return self.env['res.company'] \
            ._company_default_get('account.invoice.line') \
            .analytic_tag_ids

    analytic_tag_ids = fields.Many2many(
        default=_get_default_analytic_tag_ids,
    )
