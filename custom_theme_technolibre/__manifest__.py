{
    'name': 'Custom Theme TechnoLibre',
    'category': 'Theme',
    'version': '12.0.1.0',
    'author': 'TechnoLibre',
    'sequence': 900,
    'website': 'https://technolibre.ca',
    'license': 'AGPL-3',
    'depends': [
        'website',
        'website_theme_install',
    ],
    'data': [
        'data/assets.xml',
        'data/custom_theme_technolibre_data.xml',
        'views/custom_theme_technolibre_templates.xml',
    ],
    'installable': True,
}
