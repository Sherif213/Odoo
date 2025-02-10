from odoo import models,fields,api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    name = fields.Char(string='Property name' ,required = 1 ,default = 'New')
    description = fields.Text(string='Property Description')
    postcode = fields.Char(string='Postcode', required = 1 ,size = 6)
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
    ],default = 'north')

    _sql_constraints = [
        ('unique_for_name','unique("name")','The name must be unique.'),


    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
           if rec.bedrooms == 0:
               raise ValidationError('Bedrooms cannot be zero')

