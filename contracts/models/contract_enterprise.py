from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class ContractEnterprise(models.Model):
    _name = "contract.enterprise"
    _description = "contract enterprise model"

    def _default_sign_date(self):
        next_week = fields.Datetime.now() + timedelta(weeks=1)
        if next_week.weekday() >= 5:
            next_week += timedelta(days=7 - next_week.weekday())
        return next_week

    id = fields.Integer('id', required=True)
    name = fields.Char("contract name", required=True)
    start_date = fields.Datetime('start date', required=True, select=True, default=datetime.now())
    end_date = fields.Datetime('end date', required=True, select=True)
    type_contract = fields.Integer('contract type', required=True)
    sign_date = fields.Datetime('sign date', required=True, select=True, default=_default_sign_date)
    salary_level = fields.Float('salary level', required=False, default=0)
    effective_salary = fields.Float('effective salary', required=False, default=0)
    employee = fields.Many2one('employee.directory', string="Employee", required=True, ondelete='cascade')
    sign_day = fields.Date(string="Sign Date")
    status = fields.Selection([
                ('new', 'New'),
                ('running', 'Running'),
                ('expired', 'Expired'),
                ('pause', 'Pause')
            ], string='Status', default='new')

    total_salary = fields.Float(string='Total Salary', compute='_compute_total_salary', store=True)

    @api.depends('salary_level', 'effective_salary')
    def _compute_total_salary(self):
        for record in self:
            record.total_salary = record.salary_level + record.effective_salary
