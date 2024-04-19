from odoo import api, fields, models, tools, _

class HrEmployee(models.Model):
    _name = 'hr.employee'
    _description = 'HR Employee'
    _inherit = 'hr.employee'

    status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('waiting_approve', 'Waiting Approve'),
            ('approved', 'Approved'),
            ('terminated', 'Terminated'),
        ], string='Status', default='draft', readonly=True
    )
    work_experiences_ids = fields.One2many('work.experiences', 'employee_id', string='Work Experiences')


    def action_submit(self):
        self.status = "waiting_approve"

    def action_approve(self):
        self.status = 'approved'

    def action_terminate(self):
        self.status = 'terminated'

    def action_set_to_draft(self):
        self.status = 'draft'

    def action_update_status(self):
        for record in self:
            record.status = "approved"

