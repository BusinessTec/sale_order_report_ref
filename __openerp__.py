# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Business Tec Systems S.A.(<http://businesstec.net>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Sale Orders in Reporting Currency',
    'version': '0.1',
    'author': 'Business Tec Systems',
    'summary': 'Adds additionl column for sales order in reference currency',
    'description': """
Sale Order in Reporting Currency
================================
Calculates sales orders amount in ref currency (can be any currency or company currency). All calculation done at exchange rate of the order date.
    """,
    'website': 'https://businesstec.net',
    'images': [],
    'depends': ['product', 'sale'],
    'sequence': 18,
    'data': [
#        'cost_plus_price.xml',
    ],
    'installable': True,
    'auto_install': False,
}
