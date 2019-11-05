
from odoo import api, models


class AnalyticAccount(models.Model):

    _inherit = 'account.analytic.account'

    @api.multi
    def name_get(self):
        # Override the core functionality that formulates the analytic account
        # name as "[<code>] <name> - <commercial partner>", and remove 
        # the partner part
        res = []
        for analytic in self:
            name = analytic.name
            if analytic.code:
                name = '['+analytic.code+'] '+name
            res.append((analytic.id, name))

        return res
