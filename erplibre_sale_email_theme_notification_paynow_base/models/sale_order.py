# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

XML_ID = "muk_web_theme._assets_primary_variables"
SCSS_URL = "/muk_web_theme/static/src/scss/colors.scss"


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_theme_color(self, field_name='theme_color_primary'):
        variables = [
            'o-brand-odoo',
            'o-brand-primary',
            'mk-required-color',
            'mk-apps-color',
            'mk-appbar-color',
            'mk-appbar-background',
        ]

        colors = self.env['muk_utils.scss_editor'].get_values(
            SCSS_URL, XML_ID, variables
        )

        dict_colors = {
            'theme_color_brand': colors['o-brand-odoo'],
            'theme_color_primary': colors['o-brand-primary'],
            'theme_color_required': colors['mk-required-color'],
            'theme_color_menu': colors['mk-apps-color'],
            'theme_color_appbar_color': colors['mk-appbar-color'],
            'theme_color_appbar_background': colors['mk-appbar-background'],
        }

        return dict_colors.get(field_name, '#5D8DA8')
