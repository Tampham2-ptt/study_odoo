from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class ContractEnterprise(models.Model):
    _name = "contract.enterprise"
    _description = "contract enterprise model"

    id = fields.Integer('id', required=True)
    name = fields.Char("contract name", required=True)
    start_date = fields.Datetime('start date', required=True, select=True, default=datetime.now())
    end_date = fields.Datetime('end date', required=True, select=True)
    type_contract = fields.Integer('contract type', required=True)
    sign_day = fields.Datetime('sign day', required=True, select=True, default=datetime.now() + timedelta(days=7))
    salary_level = fields.Float('salary level', required=False, default=0)
    effective_salary = fields.Float('effective salary', required=False, default=0)
    status = fields.Selection([
                ('new', 'New'),
                ('running', 'Running'),
                ('expired', 'Expired'),
                ('pause', 'Pause')
            ], string='Status', default='new')
