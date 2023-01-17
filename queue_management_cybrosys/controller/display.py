from odoo import http
from odoo.http import request


class Display(http.Controller):
    @http.route(['/display'], auth='public', type='http')
    def display(self):
        return request.render('queue_management_cybrosys.view_display')

    @http.route(['/session/<int:sess_id>'], auth='public', type='http')
    def session(self, sess_id):
        departments = request.env['departments'].sudo().search([])
        vals = []
        for rec in departments:
            vals.append({
                'name': rec.name,
                'id': rec.id
            })
        return request.render('queue_management_cybrosys.view_session', {
            'vals': vals, 'id': sess_id
        })

    @http.route(['/token/view'], auth='public', type='http')
    def token(self, **post):
        department = request.env['departments'].sudo().search([(
            'name', '=', post.get('department'))], limit=1)
        session = request.env['sessions'].sudo().search([(
            'interface_id', '=', int(post.get('session'))),
            ('state', '=', 'in_progress')])
        last_token = request.env['tokens'].sudo().search([(
            'session_id', '=', session.id),
            ('department_id', '=', department.id)],
            order='create_date desc', limit=1)
        if last_token:
            token = int(last_token.token)
            i = token + 1
            new_token = f'{i:04}'
        else:
            i = 1
            new_token = f'{i:04}'
        token = request.env['tokens'].sudo().create({
            'name': post.get('name'),
            'token': new_token,
            'mobile': post.get('mobile'),
            'department_id': department.id,
            'session_id': session.id,

        })
        token_no = token.token
        url = '/session/' + str(post.get('session'))
        return request.render('queue_management_cybrosys.view_tokens', {
            'token': token_no, 'url': url
        })

    @http.route(['/processing/<int:counter_id>'], auth='public', type='http')
    def processing(self, counter_id, **post):
        print(counter_id)
        print(post)
        if post:
            tokens_update = request.env['tokens'].sudo().search([
                ('token', '=', post.get('token')),
                ('mobile', '=', post.get('mobile')),
                ('name', '=', post.get('user')),
            ])
            tokens_update.sudo().write({
                'state': 'in_progress',
            })
            print(tokens_update)
        tokens = request.env['tokens'].sudo().search([])
        vals = []
        si_no = 0
        for rec in tokens:
            si_no += 1
            vals.append({
                'si_no': si_no,
                'counter': '',
                'token': rec.token,
                'called': 'No',
            })
        return request.render('queue_management_cybrosys.view_processing',
                              {'vals': vals})

    @http.route(['/processing/current'], auth='public', type='http')
    def processing_current(self):
        tokens = request.env['tokens'].sudo().search([
            ('state', '=', 'draft')], order='create_date asc', limit=1)
        vals = []
        for rec in tokens:
            vals.append({
                'user': rec.name,
                'token': rec.token,
                'mobile': rec.mobile,
                'department': rec.department_id.name,
            })
        print(vals)
        url = '/processing/' + '1'
        return request.render('queue_management_cybrosys.'
                              'view_processing_current', {'vals': vals,
                                                          'url': url})
