from odoo import api, fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    analytic_tag_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        string="Default Analytic Tags",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Informational list of analytic tags related to the invoice",
    )

    @api.onchange("analytic_tag_ids", "analytic_account_id")
    def set_line_analytic_tags(self):
        self.ensure_one()
        if self.analytic_tag_ids:
            for line in self.invoice_line_ids:
                line.analytic_tag_ids = [(6, 0, self.analytic_tag_ids.ids)]
