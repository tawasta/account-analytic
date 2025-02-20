from odoo import fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    revenue_budget = fields.Monetary(string="Revenue", copy=False)
    materials_budget = fields.Monetary(string="Materials", copy=False)
    subcontract_budget = fields.Monetary(string="Services", copy=False)
    hours_budget = fields.Float(string="Hours", copy=False)
