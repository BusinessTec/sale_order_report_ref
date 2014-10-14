# -*- coding: utf-8 -*- 

from openerp import models, fields, api

class price_product_template(models.Model):

	_inherit = "product.template"
	target_margin = fields.Float(string='Margen previsto', digits=(6,3), default='31')
	price_cal = fields.Float(string='precio base', digits=(6,3),compute='new_price')
#	price_cal = fields.Float(string='Margen previsto', digits=(6,3))

	@api.one
	@api.depends('standard_price','target_margin')
	def new_price(self):
		self.price_cal=self.standard_price * (1 + self.target_margin/100)
