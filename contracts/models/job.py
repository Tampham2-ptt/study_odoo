from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
class Job(models.Model):
    _name = 'job'
    _description = 'Job'

    name = fields.Char(string="Job Name", required=True)
    code = fields.Char(string="Job Code", required=True)

    @api.constrains('name')
    def _validate_name(self):
        for record in self:
            jobs = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if jobs:
                raise ValidationError("Name must be unique.")