from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError

class Role(models.Model):
    _name = 'role'
    _description = 'Role'

    name = fields.Char(string="Role Name", required=True)
    code = fields.Char(string="Role Code", required=True)

    @api.constrains('name')
    def _validate_name(self):
        for record in self:
            roles = self.search([('name', '=', record.name), ('id', '!=', record.id)])
            if roles:
                raise ValidationError("Name must be unique.")
