from odoo import api, models


class AccountInvoiceLine(models.Model):

    _inherit = "account.invoice.line"

    @api.onchange("account_analytic_id")
    def onchange_analytic_account_id_update_analytic_tags(self):
        for record in self:
            if record.account_analytic_id and record.account_analytic_id.tag_ids:
                record.analytic_tag_ids += record.account_analytic_id.tag_ids
