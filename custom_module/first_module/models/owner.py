from odoo import models, fields, api

class Owner(models.Model):
    _name = 'owner'
    _description = 'Owner'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    age = fields.Integer(string='Age', required=True)
    address = fields.Char(string='Address', required=True)
    property_ids = fields.One2many('property', 'owner_id', string='Property')
