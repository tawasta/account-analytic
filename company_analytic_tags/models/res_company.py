
from odoo import models, fields


class ResCompany(models.Model):

    _inherit = 'res.company'

    analytic_tag_ids = fields.Many2many(
        comodel_name='account.analytic.tag',
        string='Analytic tags',
    )
