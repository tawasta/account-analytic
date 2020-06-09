from odoo import api, models


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.onchange("account_analytic_id")
    def onchange_analytic_account_id_update_analytic_tags(self):
        for rec in self:
            if rec.account_analytic_id and rec.account_analytic_id.tag_ids:
                rec.analytic_tag_ids += \
                    rec.account_analytic_id.tag_ids - rec.analytic_tag_ids
