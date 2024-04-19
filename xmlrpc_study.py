try:
    from xmlrpc import client as xmlrpclib
except:
    import xmlrpclib

# Kết nối tới server Odoo XML-RPC
url = 'http://localhost:8069/'
user = 'admin'
database = 'odoo_16'
username = 'admin'
password = '1234'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(database, username, password, {})
print(uid)

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

def get_work_experiences():

    fields_display = {
        'field': ['name', 'from_date', 'to_date']
    }

    data_work_experiences = models.execute_kw(database, uid, password, 'contracts.work.experiences', 'search', [[]], fields_display)
    print(data_work_experiences)
#
get_work_experiences()
