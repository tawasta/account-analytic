# -*- coding: utf-8 -*-
from odoo import fields, models


class AccountAnalyticTag(models.Model):

    _inherit = 'account.analytic.tag'

    active = fields.Boolean(
        string='Active',
        default='True',
    )
