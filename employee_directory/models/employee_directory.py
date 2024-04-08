from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class EmployeeDirectory(models.Model):
    _name = 'employee.directory'
    _description = 'Employee Directory'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    address = fields.Char(string='Address', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone Number')
    contract_count = fields.Integer(string="Contract Count", compute='_compute_contract_count')

    def action_open_contracts(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Contracts',
            'res_model': 'contract.enterprise',
            'domain': [('employee', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }

    def _compute_contract_count(self):
        for rec in self:
            contract_count = self.env['contract.enterprise'].search_count([('employee', '=', rec.id)])
            rec.contract_count = contract_count