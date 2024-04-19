from odoo import api, fields, models, tools, _

class WorkExperiences(models.Model):
    _name = 'work.experiences'
    _description = 'Work Experiences'

    from_date = fields.Datetime(string="From")
    to_date = fields.Datetime(string="To")
    company = fields.Char(string="Name Company")
    job_id = fields.Many2one('job', string='Job', required=True)
    role_id = fields.Many2one('role', string='Role', required=True)
    level_id = fields.Many2one('level', string='Level', required=True)
    reference = fields.Text(string='Reference')
    employee_id = fields.Many2one('hr.employee', string="Employee")

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # Chỉ cho phép người dùng thuộc nhóm staff xem các kinh nghiệm làm việc của họ
        if self.env.user.has_group('contracts.module_contract_user'):
            user_employee_id = self.env.user.employee_id.id
            if user_employee_id:
                args.append(('employee_id', '=', user_employee_id))
        return super(WorkExperiences, self).search(args, offset, limit, order, count)
