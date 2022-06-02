# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "ERPLibre Sale Report Template Vertical Header",
    "author": "TechnoLibre",
    "website": "https://technolibre.ca",
    "category": "Other",
    "description": """
ERPlivre Sale Report Template Vertical Header
=============================================
for best result with PDF generation, please set the paper format to US Letter (erplibre vertical header)
Setting > General Parameters > Format > (dropdown) US Letter (erplibre vertical header) > Save

    """,
    "license": "AGPL-3",
    "depends": [
        "account",
        "web",
        "sale",
    ],
    "data": [
        "views/report_invoice.xml",
        "views/report_templates.xml",
        "report/report_paperformat.xml",
        "data/report_layout.xml",
        "report/sale_report_templates.xml",
    ],
}
