try:
    from xmlrpc import client as xmlrpclib
except:
    import xmlrpclib

# Kết nối tới server Odoo XML-RPC
url = 'http://localhost:8069/'
user = 'truong'
database = 'odoo_16'
username = 'admin'
password = '1234'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(database, username, password, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

def get_work_experiences(fields_display, **kwargs):
    data_search = kwargs.get('data', [])
    search_conditions = []
    for data in data_search:
        for key, value in data.items():
            search_conditions.append([key, '=', value])
    data_work_experiences = models.execute_kw(database, uid, password, 'contract.enterprise', 'search_read', [search_conditions], fields_display)
    for format_data in data_work_experiences:
        if 'employee_id' in format_data:
            format_data['employee_id'] = {
                'id': format_data['employee_id'][0],
                'name': format_data['employee_id'][1],
            }
    return data_work_experiences


def get_work_experiences_detail(fields_display, contract_id):
    contract_detail = models.execute_kw(database, uid, password, 'contract.enterprise', 'read', [contract_id], fields_display)
    return contract_detail


def create_work_experiences(data_create):
    work_experiences_new = models.execute_kw(database, uid, password, 'contract.enterprise', 'create', [data_create])
    return work_experiences_new


def update_work_experiences(data_update, id):
    work_experiences_update = models.execute_kw(database, uid, password, 'contract.enterprise', 'write', [[id], data_update])
    return work_experiences_update

def delete_work_experiences(id):
    models.execute_kw(database, uid, password, 'contract.enterprise', 'unlink', [[id]])
    return True


while True:
    fields_contract_display = {
        'fields': ['name', 'start_date', 'end_date', 'type_contract', 'sign_date', 'salary_level',
                   'effective_salary', 'status', 'role_name', 'level_name', 'job_name', 'employee_id']
    }
    x = input('Nhap So : ')
    match int(x):
        case 1:
            data_search = [{
                'name': 'Hợp Đồng 3',
                'role_name': 'BA'
            }]
            print(get_work_experiences(fields_contract_display, data=data_search))
        case 2:
            contract_id = 9
            print(get_work_experiences_detail(fields_contract_display, contract_id))
        case 3:
            data_create = [
                {'name': 'Hợp Đồng 4', 'start_date': '2024-04-19 01:40:25', 'end_date': '2024-04-26 03:11:40', 'type_contract': 0, 'sign_date': '2024-04-26 03:11:40', 'salary_level': 1000000.0, 'effective_salary': 23123312.0, 'status': 'running', 'employee_id': 1}
            ]
            print(create_work_experiences(data_create))
        case 4:
            data_update = {'name': 'Hợp Đồng X'}
            id = 12
            print(update_work_experiences(data_update, id))
        case 5:
            id = 12
            print(delete_work_experiences(id))


