# -*- coding: utf-8 -*-
from odoo import models, fields


class AccountTaxGroup(models.Model):

    _inherit = 'account.tax.group'

    active = fields.Boolean(
        default=True,
    )
