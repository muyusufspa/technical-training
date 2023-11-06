from odoo import models, fields
from datetime import timedelta


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    # Set the default date to 3 months from today
    date_availability = fields.Date(string='Availability Date', default=lambda self: fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float(string='Expected Price')
    # prevent copying of selling price, calculated field expected_price + 10%
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False, compute='_compute_selling_price')
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Char(string='Garden Orientation')
    kitchen_type = fields.Char(string='Kitchen Type')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        [('new', 'New'), 
         ('offer_received', 'Offer Received'), 
         ('offer_accepted', 'Offer Accepted'), 
         ('sold', 'Sold'), 
         ('canceled', 'Canceled')], 
        string='Status', default='new')
    
    
    def _compute_selling_price(self):
        for record in self:
            record.selling_price = record.expected_price * 1.1
            