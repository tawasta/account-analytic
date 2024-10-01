from odoo import fields, models


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    materials_budget = fields.Monetary(string="Materials", copy=False)
    subcontract_budget = fields.Monetary(string="Subcontracting", copy=False)
    hours_budget = fields.Float(string="Hours", copy=False)
