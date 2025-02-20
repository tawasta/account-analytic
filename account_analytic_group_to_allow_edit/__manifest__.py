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
    "name": "Analytic Account – Allow editing only for one group",
    "summary": "Adds a group who only has the rights to edit analytic accounts",
    "version": "17.0.1.0.0",
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
        "security/allow_edit_group.xml",
    ],
}
