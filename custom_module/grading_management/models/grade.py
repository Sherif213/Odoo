from odoo import models , fields

class Grade(models.Model):
    _name = 'grade'
    _description = 'Grade'

    #general information
    grade_number = fields.Integer(string='Grade Number', required=True,default = 1)

    #Constant Information
    medical_allowance = fields.Float(string='Medical Allowance', required=True,default = 0.0)
    internal_allowance = fields.Float(string='Internal Allowance', required=True,default = 0.0)



    