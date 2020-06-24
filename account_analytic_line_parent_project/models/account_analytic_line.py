# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountAnalyticLine(models.Model):

    _inherit = 'account.analytic.line'

    parent_project_id = fields.Many2one(
        related='project_id.parent_project_id',
        comodel_name='project.project',
    )
