from odoo import fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    tag_ids = fields.Many2many(
        "account.analytic.tag",
        "account_analytic_account_tag_rel",
        "account_id",
        "tag_id",
        string="Tags",
        copy=True,
    )
