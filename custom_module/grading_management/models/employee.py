from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re



class Employee(models.Model):
    _name = 'employee'
    _description = 'Employee'
    #general Info.
    employee_id = fields.Many2one()
    employee_name = fields.Char('Employee Name',required=True)
    employee_phone_number = fields.Char('Employee Phone Number',required=True)
    employee_address = fields.Char('Employee Address',required=True)
    employee_birthdate = fields.Date('Employee Birthdate',required=True)
    employee_gender = fields.Selection((
        ('male', 'Male'),
        ('female', 'Female'),
    ),required=True)
    employee_department = fields.Selection((
        ('software_department', 'Software Department'),
        ('hardware_department', 'Hardware Department'),
        ('sales_department', 'Sales Department'),
        ('legal_department', 'Legal Department'),
        ('marketting_department', 'Marketting Department'),
        ('accounting_department', 'Accounting Department'),
        ('other', 'Other'),
    ),required=True)

    #contract Details
    contract_start_date = fields.Date('Contract Start Date',required=True)
    contract_end_date = fields.Date('Contract End Date',required=True)

    work_status= fields.Selection([
        ('remote', 'Remotely'),
        ('on_site', 'On Site'),
    ])


    _sql_constraints = [
        ('employee_number','unique(employee_number)','Employee phone number must be unique'),
    ]

    @api.constrains('employee_phone_number')
    def _check_phone_number(self):
        phone_pattern = re.compile(r"^\+?\(?\d{3}\)?[-\s.]?\d{3}[-\s.]?\d{4,6}$")
        for record in self:
            if not phone_pattern.match(record):
                raise ValidationError("There is an error in the phone number")



