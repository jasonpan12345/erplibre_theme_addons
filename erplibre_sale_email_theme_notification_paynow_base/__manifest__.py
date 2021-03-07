
{
    'name': 'ERPLibre Sale Email Theme Notification Paynow Base',
    'author': 'TechnoLibre',
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'category': 'Other',
    'description': 'Base module for sale email theme. Exposing the theme color variables for styling templates',
    'depends': [
        'mail',
        'sale',

        # Muk
        'muk_web_theme',
    ],
    'data': [
        'data/mail_data.xml',
    ],
    "auto_install": False,
}
