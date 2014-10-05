# -*- coding: utf-8 -*- 

from openerp.osv import osv,fields,orm
import openerp.addons.decimal_precision as dp

class product_template(osv.osv):
    _inherit = "product.template"
    _columns = {
        'price_cal': fields.float('Precio de venta (ref.)', digits_compute=dp.get_precision('Product Price')),
        
    	             
    	           }

