from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Grade(models.Model):
    _name = 'grade'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Grade'

    # general information
    grade_number = fields.Integer(string='Grade Number', required=True, default=1)

    # Constant Information
    medical_allowance = fields.Float(string='Medical Allowance', required=True, default=0.0)
    internet_allowance = fields.Float(string='Internet Allowance', required=True, default=0.0)
    insurance = fields.Float(string='Insurance', required=True, default=0.0)

    # changing by gender
    female_allowance = fields.Float(string='Female Allowance', required=True, default=0.0)

    # changing by sales in sales department
    sales_bonus_entry_rate = fields.Float(string='Sales Bonus Entry Rate ', required=True, default=0.0)
    sales_bonus_senior_rate = fields.Float(string='Sales Bonus Senior Rate ', required=True, default=0.0)
    sales_bonus_specialist_rate = fields.Float(string='Sales Bonus specialist Rate ', required=True, default=0.0)
    sales_bonus_manager_rate = fields.Float(string='Sales Bonus manager Rate ', required=True, default=0.0)

    # changing by working onsite or remotely
    travel_allowance = fields.Float(string='Travel Allowance', required=True, default=0.0)
    food_allowance = fields.Float(string='Food Allowance', required=True, default=0.0)
    device_allowance = fields.Float(string='Device Allowance', required=True, default=0.0)

    # changes on the loyality of the employee varies every 3 years
    loyality_allowance_Entry = fields.Float(string='Loyalty Allowance Entry', required=True, default=0.0)
    loyality_allowance_senior = fields.Float(string='Loyalty Allowance Senior Entry', required=True, default=0.0)
    loyality_allowance_specialist = fields.Float(string='Loyalty Allowance Specialist', required=True, default=0.0)
    loyality_allowance_manager = fields.Float(string='Loyalty Allowance Manager', required=True, default=0.0)


    _sql_constraints = [
        ('grade_uniqueness', 'unique("grade_number")', 'Grade number must be unique!'),
    ]

    @api.constrains('medical_allowance', 'internet_allowance', 'insurance')
    def _greater_than_zero_must_allowance(self):
        for record in self:
            if record.medical_allowance <= 0 or record.internet_allowance <= 0 or record.insurance <= 0:
                raise ValidationError("The following allowances must be greater than zero:\n"
                                      "- Medical Allowance\n"
                                      "- Internet Allowance\n"
                                      "- Insurance\n"
                                      )

    @api.constrains('female_allowance')
    def _greater_or_equal_zero_allowance_by_gender(self):
        for record in self:
            if record.female_allowance < 0:
                raise ValidationError("The following allowances must be greater than zero:\n"
                                      "- Female Allowance\n")

    # @api.constrains('sales_bonus_entry_rate','sales_bonus_senior_rate'
    #     ,'sales_bonus_specialist_rate','sales_bonus_manager_rate','travel_allowance','food_allowance','device_allowance',
    #                 'loyality_allowance_Entry','loyality_allowance_senior','loyality_allowance_specialist',)
    # # def _greater_or_equal_zero_additional_allowance(self):
    #     for record in self:
    #         if any(allowance < 0 for allowance in [
    #             record.sales_bonus_entry_rate,record.sales_bonus_senior_rate,record.sales_bonus_specialist_rate,
    #             record.sales_bonus_manager_rate,record.travel_allowance,record.food_allowance,
    #             record.device_allowance,record.loyality_allowance_Entry,record.loyality_allowance_senior,
    #             record.loyality_allowance_specialist,]):
    #             raise ValidationError( "The following allowances must be greater than or equal to zero:\n"
    #                                    "- Sales Bonus Entry\n"
    #                                    "- Sales Bonus Senior Entry\n"
    #                                    "- Sales Bonus Specialist\n"
    #                                    "- Sales Bonus Manager\n"
    #                                    "- Travel Allowance\n"
    #                                    "- Food Allowance\n"
    #                                    "- Device Allowance\n"
    #                                    "- Loyalty allowance Entry\n"
    #                                    "- Loyalty allowance senior\n"
    #                                    "- Loyalty allowance specialist\n")

    @api.constrains('sales_bonus_entry_rate', 'sales_bonus_senior_rate'
        , 'sales_bonus_specialist_rate', 'sales_bonus_manager_rate')
    def _greater_or_equal_zero_sales_allowance(self):
        for record in self:
            if any(allowance < 0 or allowance > 100 for allowance in
                   [record.sales_bonus_entry_rate, record.sales_bonus_senior_rate, record.sales_bonus_specialist_rate,
                    record.sales_bonus_manager_rate, ]):
                raise ValidationError("The following allowances must be greater than or equal to zero:\n"
                                      "- Sales Bonus Entry\n"
                                      "- Sales Bonus Senior Entry\n"
                                      "- Sales Bonus Specialist\n"
                                      "- Sales Bonus Manager\n"
                                      )

    @api.constrains('travel_allowance', 'food_allowance', 'device_allowance')
    def _greater_or_equal_zero_remote_allowance(self):
        for record in self:
            if any(allowance < 0 for allowance in
                   [record.travel_allowance, record.food_allowance, record.device_allowance, ]):
                raise ValidationError("The following allowances must be greater than or equal to zero:\n"
                                      "- Travel Allowance\n"
                                      "- Food Allowance\n"
                                      "- Device Allowance\n"
                                      )

    @api.constrains('loyality_allowance_Entry', 'loyality_allowance_senior', 'loyality_allowance_specialist')
    def _greater_or_equal_zero_loyal_allowance(self):
        for record in self:
            if any(allowance < 0 for allowance in [record.loyality_allowance_Entry, record.loyality_allowance_senior,
                                                   record.loyality_allowance_specialist, ]):
                raise ValidationError("The following allowances must be greater than or equal to zero:\n"
                                      "- Loyalty allowance Entry\n"
                                      "- Loyalty allowance senior\n"
                                      "- Loyalty allowance specialist\n"
                                      )
