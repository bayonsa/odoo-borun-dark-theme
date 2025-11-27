{
    'name': 'Borun Dark Backend',
    'summary': 'Lightweight dark theme for Odoo backend (Borun Studios)',
    'version': '1.0.0',
    'category': 'Theme/Backend',
    'author': 'Borun Studios',
    'website': 'https://borunstudios.co.uk',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'borun_dark_backend/static/src/scss/borun_dark.scss',
        ],
    },
    'installable': True,
    'application': False,
}
