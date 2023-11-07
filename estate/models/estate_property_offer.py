
# Model for property offers

from odoo import models, fields

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property Offer'
    
    price = fields.Float(string='Price')
    # selections accepted, rejected, pending
    status = fields.Selection([('accepted', 'Accepted'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='peding', string='Status')
    partner_id = fields.Many2one('res.partner', string='Customer', domain=[('is_salesman', '=', False)], context={'default_is_salesman': False} )
    property_id = fields.Many2one('real.estate.property', string='Property')