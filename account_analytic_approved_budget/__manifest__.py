##############################################################################
#
#    Author: Futural Oy
#    Copyright 2024 Futural Oy (https://futural)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    "name": "Account Analytic – Approved budget",
    "summary": "Enable to specify an approved budget on analytic accounts",
    "version": "17.0.1.0.1",
    "category": "Accounting",
    "website": "https://github.com/tawasta/account-analytic",
    "author": "Futural",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "analytic",
    ],
    "data": [
        "views/analytic_account.xml",
    ],
}
