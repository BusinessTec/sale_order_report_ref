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
    'name': 'Costa Rica Document ID ',
    'version': '0.1',
    'author': 'Business Tec Systems',
    'summary': 'Provides field for ID number and selection of document type in Costa Rica (without any validation)',
    'description': """
Costa Rica ID Number
=======================
Provides field for ID number and selection of document type.No validation is provided
    """,
    'website': 'https://businesstec.net',
    'images': [],
    'depends': ['base'],
    'sequence': 18,
    'data': [
        'cedula.xml',
    ],
    'installable': True,
    'auto_install': False,
}
