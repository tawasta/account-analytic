
from odoo import fields, models


class AccountAnalyticLine(models.Model):

    _inherit = 'account.analytic.line'

    account_move_partner_id = fields.Many2one(
        related='move_id.partner_id',
        string='Partner of Accounting Move',
        readonly=True,
        store=True,
        help=('The partner that is connected to the accounting move related '
              'to this analytic line')
    )
