from odoo import api
from odoo import models


class ResUsers(models.Model):
    _inherit = "res.users"

    @api.multi
    def _is_system(self):
        # This allows normal users to upload XML-files.
        # XML-file mimetype is mismatched to image/svg+xml,
        # which requires the user to be system user.
        # This is a dumb (and a bit dangerous) way to allow upload, but other
        # ways of overriding this seemed a lot more complicated
        if self.env.context.get("active_model") == "account.journal":
            return True

        return super()._is_system()
