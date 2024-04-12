from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

class Level(models.Model):
    _name = 'level'
    _description = 'Level'

    name = fields.Char(string="Level Name", required=True)
    code = fields.Char(string="Level Code", required=True)

    @api.constrains('name')
    def _validate_name(self):
        for record in self:
            levels = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if levels:
                raise ValidationError("Name must be unique.")
