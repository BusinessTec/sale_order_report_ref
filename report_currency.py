from openerp.osv import osv
from openerp import models, fields, api

class currency_reference(models.Model):

        _inherit = "res.company"
        currency_ref=fields.Many2one('res.currency', string='Reporting Currency')
