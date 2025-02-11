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

    owner_id = fields.Many2one('owner', string='Owner')


    _sql_constraints = [
        ('unique_for_name','unique("name")','The name must be unique.'),


    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
           if rec.bedrooms == 0:
               raise ValidationError('Bedrooms cannot be zero')

    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        # logic
        return res

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
        res = super(Property, self)._search(domain, offset, limit, order, access_rights_uid)
        return res

    def write(self, vals):
        res = super(Property, self).write(vals)
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        return res