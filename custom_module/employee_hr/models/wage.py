from odoo import fields, models,api

class Wage(models.Model):
    _name = 'wage'
    _inherits = 'hr.employee'

    base_salary = fields.Float("Base Salary")
    has_medical = fields.Boolean("Has Medical")
    on_site = fields.Boolean("On Site")

    
