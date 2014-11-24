# -*- coding: utf-8 -*- 

from openerp import models, fields, api
import openerp.addons.

class currency_reference(models.Model):
# 
# temp: to be moved to seperate module with dependency rework 
#
	_inherit = "res.company"
	currency_ref=  fields.integer(string='Ref currency', default='3')
	
class sale_order_ref(models.Model):
	
	_inherit = "sale.order"
#	amount_untaxed_ref = fields.Float(string='Subtotal (USD)', digits=(13,2),compute='new_untaxed',readonly=True)
#	amount_taxed_ref = fields.Float(string='Imp. USD', digits=(13,2),readonly=True,compute='new_taxed')
	amount_total_ref = fields.Float(string='Total (USD)', digits=(13,2),readonly=True,compute='new_total')


	@api.one
	@api.depends('currency_id','amount_total')
	def new_total(self):
		self.amount_total_ref=compute(self, amount_total,3,True)

