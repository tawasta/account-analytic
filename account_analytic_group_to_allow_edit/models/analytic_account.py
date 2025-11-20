from odoo import _, api, models
from odoo.exceptions import ValidationError


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    def write(self, vals):
        msg = _("\nEditing or creating analytic accounts is not enabled for your user")

        if self.env.user.has_group(
            "account_analytic_group_to_allow_edit.allow_analytic_account_edit"
        ):
            return super().write(vals)
        else:
            raise ValidationError(msg)

    @api.model
    def create(self, vals):
        msg = _("\nEditing or creating analytic accounts is not enabled for your user")
        if self.env.user.has_group(
            "account_analytic_group_to_allow_edit.allow_analytic_account_edit"
        ):
            return super().create(vals)
        else:
            raise ValidationError(msg)
