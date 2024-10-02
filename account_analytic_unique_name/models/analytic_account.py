from odoo import _, api, models
from odoo.exceptions import ValidationError


class AccountAnalyticAccount(models.Model):

    _inherit = "account.analytic.account"

    def write(self, vals):
        name = vals.get("name", False)

        if name:
            account_name_exists = self.env["account.analytic.account"].search(
                [("name", "=", name)]
            )
            if account_name_exists:
                raise ValidationError(
                    _("Analytic Account already exists with the name: {}".format(name))
                )

        return super().write(vals)

    @api.model
    def create(self, vals):
        name = vals.get("name", False)

        if name:
            account_name_exists = self.env["account.analytic.account"].search(
                [("name", "=", name)]
            )
            if account_name_exists:
                raise ValidationError(
                    _("Analytic Account already exists with the name: {}".format(name))
                )

        return super().create(vals)
