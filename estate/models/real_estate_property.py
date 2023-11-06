from odoo import models, fields

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Availability Date')
    expected_price = fields.Float(string='Expected Price')
    # prevent copying of selling price, calculated field expected_price + 10%
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False, compute='_compute_selling_price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Char(string='Garden Orientation')
    kitchen_type = fields.Char(string='Kitchen Type')
    
    
    def _compute_selling_price(self):
        for record in self:
            record.selling_price = record.expected_price * 1.1
            