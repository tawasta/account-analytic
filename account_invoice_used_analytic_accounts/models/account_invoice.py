from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    @api.depends("invoice_line_ids")
    def _compute_row_analytic_account_ids(self):
        for invoice in self:
            invoice.row_analytic_account_ids = invoice.invoice_line_ids.mapped(
                "analytic_account_id"
            )

    row_analytic_account_ids = fields.Many2many(
        compute="_compute_row_analytic_account_ids",
        comodel_name="account.analytic.account",
        relation="move_row_analytic_rel",
        column1="invoice_id",
        column2="analytic_account_id",
        string="Lines' analytic accounts",
        domain=["|", ("active", "=", False), ("active", "=", True)],
        store=True,
        help="List of analytic accounts used in the invoice rows",
    )
