from odoo import fields, models


class AccountMove(models.Model):

    _inherit = "account.move"

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Default Analytic Account",
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Informational analytic account related to the invoice",
    )
