from odoo import api, fields, models, _


class AccountInvoice(models.Model):

    _inherit = "account.invoice"

    analytic_tag_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        string="Default Analytic Tags",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Informational list of analytic tags related to the invoice",
    )

    @api.multi
    @api.onchange("analytic_tag_ids")
    def set_line_analytic_tags(self):
        self.ensure_one()
        if self.analytic_tag_ids:
            for line in self.invoice_line_ids:
                line.analytic_tag_ids = [(6, 0, self.analytic_tag_ids.mapped("id"))]
