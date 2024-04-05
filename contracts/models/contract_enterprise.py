from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class ContractEnterprise(models.Model):
    _name = "contract.enterprise"
    _description = "contract enterprise model"

    id = fields.Integer('id', requests=True)
    name = fields.Char("contract name", required=True)
    start_date = fields.Datetime('start date', requests=True, select=True)
    end_date = fields.Datetime('end date', requests=True, select=True)
    type_contract = fields.Integer('contract type', requests=True)
    sign_day = fields.Datetime('sign day', requests=True, select=True)
    salary_level = fields.Float('salary level', requests=True)
    effective_salary = fields.Float('effective salary', requests=False)
    status = fields.Selection([
                ('complete', 'Complete'),
                ('unfinished', 'Unfinished')
            ], string='Status', default='unfinished')
