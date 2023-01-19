from odoo import http, fields
from odoo.http import request


class Dashboard(http.Controller):
    @http.route(['/dashboard'], auth='public', type='json')
    def dashboard(self):
        today_tokens = request.env['tokens'].sudo().search_count([
            ('date_token', '=', fields.Date.today())
        ])
        today_missed = request.env['tokens'].sudo().search_count([
            ('date_token', '=', fields.Date.today()),
            ('state', '=', 'cancelled')
        ])
        today_served = request.env['tokens'].sudo().search_count([
            ('date_token', '=', fields.Date.today()),
            ('state', '=', 'done')
        ])
        today_left = request.env['tokens'].sudo().search_count([
            ('date_token', '=', fields.Date.today()),
            ('state', '=', 'draft')
        ])
        total_counter = request.env['counter'].sudo().search_count([])
        total_sessions = request.env['sessions'].sudo().search_count([])
        token_day = int(today_tokens) / 2
        vals = [{
            '1': today_tokens,
            '2': today_missed,
            '3': today_served,
            '4': today_left,
            '5': today_tokens,
            '6': today_served,
            '7': today_missed,
            '8': token_day,
            '9': total_counter,
            '10': total_sessions,
        }]
        return vals

    @http.route(['/at_top'], auth='public', type='json')
    def at_top(self):
        departments = request.env['departments'].sudo().search([])
        vals = []
        for rec in departments:
            served = request.env['tokens'].sudo().search_count([
                ('department_id', '=', rec.id),
                ('state', '=', 'done')
            ])
            cancelled = request.env['tokens'].sudo().search_count([
                ('department_id', '=', rec.id),
                ('state', '=', 'cancelled')
            ])
            vals.append({
                'name': rec.name,
                'served': served,
                'cancelled': cancelled,
            })
        return vals

