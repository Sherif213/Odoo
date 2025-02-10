from odoo import models , fields

class Grade(models.Model):
    _name = 'grade'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Grade'

    #general information
    grade_number = fields.Integer(string='Grade Number', required=True,default = 1)

    #Constant Information
    medical_allowance = fields.Float(string='Medical Allowance', required=True,default = 0.0)
    internet_allowance = fields.Float(string='Internet Allowance', required=True,default = 0.0)
    insurance = fields.Float(string='Insurance', required=True,default = 0.0)

    #changing by gender
    female_allowance = fields.Float(string='Female Allowance', required=True,default = 0.0)

    #changing by sales in sales department
    sales_bonus_entry_rate = fields.Float(string='Sales Bonus Entry Rate ', required=True,default = 0.0)
    sales_bonus_senior_rate = fields.Float(string='Sales Bonus Senior Rate ', required=True,default = 0.0)
    sales_bonus_specialist_rate = fields.Float(string='Sales Bonus specialist Rate ', required=True,default = 0.0)
    sales_bonus_manager_rate = fields.Float(string='Sales Bonus manager Rate ', required=True,default = 0.0)


    #changing by working onsite or remotely
    travel_allowance = fields.Float(string='Travel Allowance', required=True,default = 0.0)
    food_allowance = fields.Float(string='Food Allowance', required=True,default = 0.0)
    device_allowance = fields.Float(string='Device Allowance', required=True,default = 0.0)

    #changes on the loyality of the employee varies every 3 years
    loyality_allowance_Entry = fields.Float(string='Loyalty Allowance Entry', required=True,default = 0.0)
    loyality_allowance_senior = fields.Float(string='Loyalty Allowance Senior Entry', required=True, default = 0.0)
    loyality_allowance_specialist = fields.Float(string='Loyalty Allowance Specialist', required=True, default = 0.0)
    loyality_allowance_manager = fields.Float(string='Loyalty Allowance Manager', required=True, default = 0.0)

    