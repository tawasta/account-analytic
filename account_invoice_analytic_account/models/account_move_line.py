from odoo import api, models


class AccountMoveLine(models.Model):

    _inherit = "account.move.line"

    @api.depends("product_id", "account_id", "partner_id", "date")
    def _compute_analytic_account_id(self):
        res = super()._compute_analytic_account_id
        for record in self:
            # Set default analytic account value for new lines
            if not record.analytic_account_id and record.move_id.analytic_account_id:
                record.analytic_account_id = record.move_id.analytic_account_id

        return res
