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
    'depends': ['hr', 'website'],
    'data': [
        'security/work_experiences.xml',
        'security/ir.model.access.csv',
        'views/work_experiences_views.xml',
        'views/for_python_templates.xml',
        'report/work_experiences_template.xml',
        'report/work_experiences_report.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'static/src/*',
        ]
    },
    'installable': True,
    'application': True,
}
