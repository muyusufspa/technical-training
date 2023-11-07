# extend res.partner model of odoo

from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_salesman = fields.Boolean(string='Is a Salesman')