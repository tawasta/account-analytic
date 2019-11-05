
from odoo import api, fields, models


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    @api.model
    def _get_default_analytic_tag_ids(self):
        return self.env['res.company'] \
            ._company_default_get('sale.order.line') \
            .analytic_tag_ids

    analytic_tag_ids = fields.Many2many(
        default=_get_default_analytic_tag_ids,
    )
