# -*- coding: utf-8 -*- 

from openerp.osv import osv,fields,orm
import openerp.addons.decimal_precision as dp

class product_template(osv.osv):
    _inherit = "product.template"
    _columns = {
        'target_margin': fields.float(''purchase_price': fields.float('Cost Price', digits=(16,2))', digits=(6,3)),
        'price_cal': fields.function(_get_price_cal, method=True, string="Precio base", type='float', store=False),
               }
    _defaults = {
        'target_margin': 35.0,
    }

