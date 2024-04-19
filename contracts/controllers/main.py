from odoo import http
from odoo.http import request
import json


class QwebTest(http.Controller):
    @http.route(['/qweb-test', '/qweb-test/<int:id>'], type='http', auth='public', website=True)
    def qweb_test(self, id=None):
        print(id)
        if id:
            contracts = request.env['contract.enterprise'].browse(id)
        else:
            contracts = request.env['contract.enterprise'].search([])
        show_name = False
        if len(contracts) > 0:
            show_name = True
        data = {
            'show_name': show_name,
            'contracts': contracts
        }
        return http.request.render("contracts.somePythonTemplate", data)

    @http.route('/job-info', type='json', auth='none')
    def courses_json(self, *args, **kwargs):
        courses = request.env['job'].sudo().search([])
        courses_data = [{'name': course.name} for course in courses]
        print(json.dumps(courses_data))
        return courses_data


