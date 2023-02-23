from odoo import _, exceptions, models


class AccountPaymentMassCancel(models.TransientModel):

    _name = "account.payment.mass.cancel"
    _description = "Mass cancel payments"

    def get_cancellable_states(self):
        return ["posted", "sent", "reconciled"]

    def cancel_payments(self):
        payment_ids = self.env["account.payment"].browse(
            self._context.get("active_ids")
        )

        allowed_states = self.get_cancellable_states()

        if any(p.state not in allowed_states for p in payment_ids):
            msg = _("Please only select Payments whose states allow cancelling")
            raise exceptions.UserError(msg)

        for payment in payment_ids:
            payment.action_draft()
            payment.action_cancel()
