import json

from odoo import http
from odoo.http import request


class WebsiteSnippetAll(http.Controller):
    @http.route(
        "/website_snippet_all/google_maps_api_key",
        type="json",
        auth="public",
        website=True,
    )
    def google_maps_api_key(self):
        return json.dumps(
            {"google_maps_api_key": request.website.google_maps_api_key or ""}
        )
