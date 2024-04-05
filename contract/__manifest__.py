# -*- coding: utf-8 -*-

{
    'name': 'Enterprise Contract',
    'category': 'Website/Website',
    'summary': 'contract_enterprise models',
    'version': '1.0',
    'author': 'Tam kem',
    'description': """
        This is a module used to sign contracts between businesses and employees
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_views.xml',
    ],
    'installable': True,
    'application': True,
}
