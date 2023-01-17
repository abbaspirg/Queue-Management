{
    'name': 'Queue Management',
    'version': '16.0.1.0.0',
    'summary': """Queue Management""",
    'description': 'Queue Management',
    'category': '',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/counter.xml',
        'views/departments.xml',
        'views/interface.xml',
        'views/processing.xml',
        'views/sequence.xml',
        'views/sessions.xml',
        'views/tokens.xml',
        'views/dashboard.xml',
        'views/display.xml',
        'views/view_session.xml',
        'views/view_tokens.xml',
        'views/view_processing.xml',
        'views/view_processing_current.xml',
        'wizard/process_wizard.xml',
        'views/menus.xml',
    ],
    'assets': {
        # 'web.assets_frontend': [
        #     'queue_management_cybrosys/static/src/js/counter.js',
        # ],
        'web.assets_backend': [
            'queue_management_cybrosys/static/src/js/dashboard.js',
            'queue_management_cybrosys/static/src/xml/dashboard.xml',
        ],
    },
    'demo': [],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
