from odoo import models, fields, api


class GradingWage(models.Model):
    _inherit = 'hr.employee'
    grade_id = fields.Many2one('grade', string='Grade')
    wage_amount = fields.Float('Wage Amount')
