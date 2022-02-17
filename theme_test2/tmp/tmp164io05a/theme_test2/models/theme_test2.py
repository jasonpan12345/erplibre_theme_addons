from odoo import _, api, fields, models


class ThemeTest2(models.AbstractModel):
    _inherit = "theme.utils"

    def _theme_test2_post_copy(self, mod):
        self.disable_view("website_theme_install.customize_modal")
