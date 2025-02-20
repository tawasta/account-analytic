from odoo import _, api, models
from odoo.exceptions import ValidationError


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    def write(self, vals):
        if self.env["res.users"].has_group(
            "account_analytic_group_to_allow_edit.allow_analytic_account_edit"
        ):
            return super().write(vals)
        else:
            raise ValidationError(
                _(
                    "\nEditing or creating analytic accounts is not enabled for your user"
                )
            )

    @api.model
    def create(self, vals):
        if self.env["res.users"].has_group(
            "account_analytic_group_to_allow_edit.allow_analytic_account_edit"
        ):
            return super().create(vals)
        else:
            raise ValidationError(
                _(
                    "\nEditing or creating analytic accounts is not enabled for your user"
                )
            )
