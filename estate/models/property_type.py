# Odoo model class for propoerty type:

from odoo import models, fields

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)