
from odoo import fields, models, api


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    @api.depends('invoice_line_ids')
    def _compute_row_analytic_tag_ids(self):
        for invoice in self:
            invoice.row_analytic_tag_ids \
                = invoice.invoice_line_ids.mapped('analytic_tag_ids')

    row_analytic_tag_ids = fields.Many2many(
        compute='_compute_row_analytic_tag_ids',
        comodel_name='account.analytic.tag',
        relation='invoice_row_analytic_tag_rel',
        column1='invoice_id',
        column2='analytic_tag_id',
        string="Lines' analytic tags",
        domain=['|', ('active', '=', False), ('active', '=', True)],
        store=True,
        help='List of analytic tags used in the invoice rows'
    )
