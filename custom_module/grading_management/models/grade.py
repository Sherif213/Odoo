from odoo import models , fields

class Grade(models.Model):
    _name = 'grade'
    _description = 'Grade'

    #general information
    name = fields.Char(string='Name', required= "1" , default = "New Grade")
    grade_number = fields.Integer(string='Grade Number', required=True,default = 1)


    #Information regarding salary and performance
    travel_allowance = fields.Float(string='Allowance', required= "1" ,default= 0.0 )
    mobile_allowance = fields.Float(string='Mobile', required= "1" ,default= 0.0 )
    food_allowance = fields.Float(string='Food', required= "1" ,default= 0.0 )
    medical_allowance = fields.Float(string='Medical', required= "1" ,default= 0.0 )
    overtime_allowance = fields.Float(string='Overtime', required= "1" ,default= 0.0 )

    