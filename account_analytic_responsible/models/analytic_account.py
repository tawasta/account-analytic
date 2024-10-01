from odoo import fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    responsible_id = fields.Many2one("res.user", string="Responsible", copy=False)
