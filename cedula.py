# -*- coding: utf-8 -*- 

from openerp.osv import osv,fields,orm

class res_partner(osv.osv):


	_inherit = 'res.partner'
    	_columns = {
    	              'cedula':fields.char('Cédula', size=20),
    	              'tipo_de_cedula':
    	           }

