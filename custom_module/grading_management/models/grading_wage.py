from odoo import models, fields, api
from odoo.tools.safe_eval import datetime


class GradingWage(models.Model):
    _inherit = 'hr.employee'
    grade_id = fields.Many2one('grade', string='Grade')
    ref = fields.Char(default='New', readonly=True)

    wage_amount = fields.Float('Wage Amount')
    total_package_amount = fields.Float('Total Package', compute='_compute_total_package_amount')

    # visa
    visa_status = fields.Selection([
        ('expiring_soon', 'Expiring Soon'),
        ('expired', 'Expired'),
        ('valid', 'Valid')
    ], readonly=True)

    On_site = fields.Boolean('On Site', default=False)
    gender_status = fields.Boolean('Gender Status', default=False)

    # constant Fields
    medical_allowance = fields.Float('Medical Allowance', compute='_compute_medical_allowance', store=True)
    internet_allowance = fields.Float('Internet Allowance', compute='_compute_internet_allowance', store=True)
    insurance = fields.Float('Insurance', compute='_compute_insurance', store=True)

    # Changing by gender
    female_allowance = fields.Float('Female Allowance', compute='_compute_female_allowance', store=True)

    # changing by sales in sales department
    sales_bonus_entry_rate = fields.Float('Sales Bonus Entry Rate', compute='_compute_sales_entry_allowance',
                                          store=True)
    sales_bonus_senior_rate = fields.Float('Sales Bonus Senior Rate', compute='_compute_sales_senior_allowance',
                                           store=True)
    sales_bonus_specialist_rate = fields.Float('Sales Bonus Specialist Rate',
                                               compute='_compute_sales_specialist_allowance',
                                               store=True)

    sales_bonus_manager_rate = fields.Float('Sales Bonus Manager Rate', compute='_compute_sales_manager_allowance',
                                            store=True)

    # changing by working onsite or remotely
    travel_allowance = fields.Float('Travel Allowance', compute='_compute_travel_allowance', store=True)
    food_allowance = fields.Float('Food Allowance', compute='_compute_food_allowance', store=True)
    device_allowance = fields.Float('Device Allowance', compute='_compute_device_allowance', store=True)

    # changes on the loyality of the employee varies every 3 years
    loyality_allowance_Entry = fields.Float('Loyalty Allowance Entry', compute='_compute_loyality_allowance_Entry',
                                            store=True)
    loyality_allowance_senior = fields.Float('Loyalty Allowance Senior', compute='_compute_loyality_allowance_senior',
                                             store=True)
    loyality_allowance_manager = fields.Float('Loyalty Allowance Manager',
                                              compute='_compute_loyality_allowance_manager', store=True)

    @api.depends('gender', 'gender_status')
    def _compute_gender_status(self):
        for record in self:
            if record.gender == 'female':
                record.gender_status = True

    @api.depends('medical_allowance', 'internet_allowance', 'insurance', 'food_allowance', 'device_allowance'
        , 'female_allowance', 'travel_allowance', 'gender', 'On_site', )
    def _compute_total_package_amount(self):
        for record in self:
            record.total_package_amount = (
                    record.wage_amount
                    + record.medical_allowance
                    + record.internet_allowance
                    + record.insurance
            )
            if record.gender == 'female':
                record.total_package_amount += record.female_allowance
            if record.On_site:
                record.total_package_amount += record.travel_allowance
                record.total_package_amount += record.food_allowance
                record.total_package_amount += record.device_allowance

    @api.depends('grade_id', 'grade_id.medical_allowance')
    def _compute_medical_allowance(self):
        for record in self:
            record.medical_allowance = record.grade_id.medical_allowance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.internet_allowance')
    def _compute_internet_allowance(self):
        for record in self:
            record.internet_allowance = record.grade_id.internet_allowance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.insurance')
    def _compute_insurance(self):
        for record in self:
            record.insurance = record.grade_id.insurance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.female_allowance')
    def _compute_female_allowance(self):
        for record in self:
            record.female_allowance = record.grade_id.female_allowance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.sales_bonus_entry_rate')
    def _compute_sales_entry_allowance(self):
        for record in self:
            record.sales_bonus_entry_rate = record.grade_id.sales_bonus_entry_rate if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.sales_bonus_senior_rate')
    def _compute_sales_senior_allowance(self):
        for record in self:
            record.sales_bonus_senior_rate = record.grade_id.sales_bonus_senior_rate if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.sales_bonus_specialist_rate')
    def _compute_sales_specialist_allowance(self):
        for record in self:
            record.sales_bonus_specialist_rate = record.grade_id.sales_bonus_specialist_rate if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.sales_bonus_manager_rate')
    def _compute_sales_manager_allowance(self):
        for record in self:
            record.sales_bonus_manager_rate = record.grade_id.sales_bonus_manager_rate if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.travel_allowance')
    def _compute_travel_allowance(self):
        for record in self:
            record.travel_allowance = record.grade_id.travel_allowance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.food_allowance')
    def _compute_food_allowance(self):
        for record in self:
            record.food_allowance = record.grade_id.food_allowance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.device_allowance')
    def _compute_device_allowance(self):
        for record in self:
            record.device_allowance = record.grade_id.device_allowance if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.loyality_allowance_Entry')
    def _compute_loyality_allowance_Entry(self):
        for record in self:
            record.loyality_allowance_Entry = record.grade_id.loyality_allowance_Entry if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.loyality_allowance_senior')
    def _compute_loyality_allowance_senior(self):
        for record in self:
            record.loyality_allowance_senior = record.grade_id.loyality_allowance_senior if record.grade_id else 0.0

    @api.depends('grade_id', 'grade_id.loyality_allowance_manager')
    def _compute_loyality_allowance_manager(self):
        for record in self:
            record.loyality_allowance_manager = record.grade_id.loyality_allowance_manager if record.grade_id else 0.0

    @api.model
    def create(self, vals):
        res = super(GradingWage, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('employee_sequence')
        return res

    @api.model
    def write(self, vals):
        res = super(GradingWage, self).write(vals)

        for record in self:
            if record.ref == 'New':
                record.ref = self.env['ir.sequence'].next_by_code('employee_sequence')

        return res

    def check_expiration_date(self):
        employee_ids = self.search([])
        today = datetime.date.today()
        for employee_id in employee_ids:
            if not employee_id.visa_expire:
                continue
            visa_date = employee_id.visa_expire
            if visa_date < today:
                employee_id.visa_status = 'expired'
            elif 0 <= (visa_date - today).days < 30:
                employee_id.visa_status = 'expiring_soon'
            else:
                employee_id.visa_status = 'valid'
