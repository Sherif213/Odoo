from odoo import models,fields

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    name = fields.Char(string='Property name')
    description = fields.Text(string='Property Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Datetime(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])