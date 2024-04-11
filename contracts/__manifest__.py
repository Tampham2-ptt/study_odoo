# -*- coding: utf-8 -*-

{
    'name': 'Enterprise Contract 2',
    'category': 'Website/Website',
    'summary': 'contract_enterprise models',
    'version': '1.0',
    'author': 'Pham tien tam',
    'description': """
        This is a module used to sign contracts between businesses and employees
    """,
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/work_experiences_views.xml',
    ],
    'installable': True,
    'application': True,
}
