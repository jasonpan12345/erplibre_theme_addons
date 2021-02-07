from odoo import _, api, models, fields, SUPERUSER_ID
import os

MODULE_NAME = "erplibre_website_snippets"


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        path_module_generate = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

        # Add code generator
        value = {
            "shortdesc": "Demo website snippet content",
            "name": MODULE_NAME,
            "license": "AGPL-3",
            "author": "TechnoLibre",
            "website": "https://technolibre.ca",
            "summary": "Snippet integration in website",
            "application": True,
            "category_id": env.ref("base.module_category_website").id,

            "enable_generate_website_snippet": True,
            "enable_generate_website_snippet_javascript": False,
            "generate_website_snippet_type": "content",
            "generate_website_snippet_list": "avatar;image;btn_outline",

            "enable_sync_code": True,
            "path_sync_code": path_module_generate,
        }
        code_generator_id = env["code.generator.module"].create(value)

        # Add dependency
        depend = "website"
        module_id = env["ir.module.module"].search([("name", "=", depend)])
        assert module_id
        value_dependency_website = {
            "module_id": code_generator_id.id,
            "name": depend,
            "depend_id": module_id.id
        }
        env["code.generator.module.dependency"].create(value_dependency_website)

        # Generate view
        # wizard_view = env['code.generator.generate.views.wizard'].create({
        #     'code_generator_id': code_generator_id.id,
        #     'enable_generate_all': False,
        #     'all_model': False,
        #     'enable_generate_website_snippet': True,
        # })
        #
        # wizard_view.button_generate_views()

        # Generate module
        value = {
            "code_generator_ids": code_generator_id.ids
        }
        code_generator_writer = env["code.generator.writer"].create(value)


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        code_generator_id = env["code.generator.module"].search([('name', '=', MODULE_NAME)])
        if code_generator_id:
            code_generator_id.unlink()
