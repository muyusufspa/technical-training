# Odoo model class for propoerty type:

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)