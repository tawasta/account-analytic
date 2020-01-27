# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountBankStatement(models.Model):

    _inherit = "account.bank.statement"

    @api.multi
    def _balance_check(self):
        """ Override balance check and disable it completely """

        return True
