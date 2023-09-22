from odoo import models


class AccountMove(models.Model):

    _inherit = "account.move"

    def action_post(self):
        for record in self:
            if record.move_type == "in_invoice" and record.analytic_account_id:
                if record.narration:
                    record.narration = "%s\n%s" % (
                        record.narration,
                        record.analytic_account_id.name,
                    )
                else:
                    record.narration = record.analytic_account_id.name

        return super().action_post()
