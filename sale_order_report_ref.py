#-*- coding: utf-8 -*- 
from openerp import models, fields, api

class sale_order_ref(models.Model):
	
	_inherit = "sale.order"
	ref_amount_total = fields.Float(string='Total en USD', digits=(12,2),compute='new_total',store=True)
	company_amount_total = fields.Float(string='Total en CRC', digits=(12,2),compute='new_total_1',store=True)
	@api.api
	@api.depends('currency_id','company_id','date_order','amount_total')
	def new_total(self):
		if self.currency_id==self.company_id.currency_ref:
			self.ref_amount_total=self.amount_total
		else:
			context={}
			context.update({'date': self.date_confirm})
			context={}
			from_currency_1 = self.env['res.currency'].search([('id','=','3')])
			from_currency = self.company_id.currency_ref
			ll=self.env['res.currency.rate'].search([('&'),('currency_id','=',self.currency_id.id),('name','<',self.date_order)])[0].rate
			self.ref_amount_total=self.amount_total/ll
	@api.api
	@api.depends('currency_id','company_id','date_order','amount_total')
	def new_total_1(self):
		if self.currency_id==self.company_id.currency_id:
			self.company_amount_total=self.amount_total
		else:
			context={}
			context.update({'date': self.date_confirm})
			context={}
			from_currency_1 = self.env['res.currency'].search([('id','=','3')])
			from_currency = self.company_id.currency_id
			ll=self.env['res.currency.rate'].search([('&'),('currency_id','=',self.currency_id.id),('name','<',self.date_order)])[0].rate
			self.company_amount_total=self.amount_total*ll			

