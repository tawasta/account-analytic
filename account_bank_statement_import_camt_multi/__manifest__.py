##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2021 Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
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
    "name": "CAMT Format Bank Statements Import multiple statements",
    "summary": "Import multiple CAMT statements from a same file",
    "version": "12.0.1.2.0",
    "category": "Invoicing",
    "website": "https://github.com/Tawasta/account-analytic",
    "author": "Tawasta",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": [
        "account_bank_statement_import",
        "account_bank_statement_import_camt_oca",
    ],
    "data": ["wizard/account_bank_statement_import.xml"],
    "demo": [],
}
