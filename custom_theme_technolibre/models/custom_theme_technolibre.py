from odoo import _, api, models, fields


class CustomThemeTechnolibre(models.AbstractModel):
    _inherit = 'theme.utils'

    def _custom_theme_technolibre_post_copy(self, mod):
        self.disable_view('website_theme_install.customize_modal')
