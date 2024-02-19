# Copyright 2019 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"

    analytic_account_id = fields.Many2one(
        compute="_compute_analytic_account_id",
        inverse="_inverse_analytic_account_id",
        comodel_name="account.analytic.account",
        string="Analytic Account",
        store=True,
        help="The analytic account related to a sales order.",
    )

    @api.depends("line_ids.analytic_distribution")
    def _compute_analytic_account_id(self):
        """If all purchase request lines have same analytic account set
        analytic_account_id
        """
        for pr in self:
            account_ids = []
            for prl in pr.line_ids:
                if prl.analytic_distribution:
                    account_id = False
                    for account, _ in prl.analytic_distribution.items():
                        account_id = self.env["account.analytic.account"].browse(
                            map(int, account.split(","))
                        )
                        account_ids.append(account_id)

            if account_ids and all(
                account == account_ids[0] for account in account_ids
            ):
                pr.analytic_account_id = account_ids[0]
            else:
                pr.analytic_account_id = False

    def _inverse_analytic_account_id(self):
        """If analytic_account is set on PR, propagate it to all purchase
        request lines
        """
        for pr in self:
            if pr.analytic_account_id:
                account_id = pr.analytic_account_id.id
                distr = dict()
                distr[account_id] = 100

                for line in pr.line_ids:
                    line.analytic_distribution = distr
