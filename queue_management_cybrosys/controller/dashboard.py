from odoo import http
from odoo.http import request


class Dashboard(http.Controller):
    @http.route(['/dashboard'], auth='public', type='json')
    def dashboard(self):
        tokens = request.env['tokens'].sudo().search_count([])
        print(tokens)
        return True

