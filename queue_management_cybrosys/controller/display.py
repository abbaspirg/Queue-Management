from odoo import http
from odoo.http import request


class Display(http.Controller):
    @http.route(['/display'], auth='public', type='http')
    def display(self):
        processing = request.env['processing'].search([('state', '=',
                                                        'in_progress')])
        vals = []
        for rec in processing:
            vals.append({
                'counter': rec.counter_id.name,
                'department': rec.department_id.name,
                'token': rec.current_token,
            })
        return request.render('queue_management_cybrosys.view_display',
                              {'vals': vals})

    @http.route(['/session/<int:sess_id>'], auth='public', type='http')
    def session(self, sess_id):
        departments = request.env['departments'].sudo().search([])
        vals = []
        for rec in departments:
            vals.append({
                'name': rec.name,
                'id': rec.id
            })
        url = '/session/close/' + str(sess_id)
        return request.render('queue_management_cybrosys.view_session', {
            'vals': vals, 'id': sess_id, 'url': url
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
        current_processing = request.env['processing'].sudo().search([
            ('department_id', '=', department.id),
            ('state', '=', 'in_progress'),
        ], limit=1)
        if current_processing:
            attending = current_processing.current_token
            position = f'{(int(new_token) - int(current_processing.current_token)):04}'
        else:
            attending = '--'
            position = new_token
        token_no = token.token
        url = '/session/' + str(post.get('session'))
        return request.render('queue_management_cybrosys.view_tokens', {
            'token': token_no, 'url': url, 'attending': attending,
            'position': position,
        })

    @http.route(['/processing/<int:counter_id>'], auth='public', type='http',
                csrf=False)
    def processing(self, counter_id, **post):
        if post:
            tokens_update = request.env['tokens'].sudo().search([
                ('token', '=', post.get('token')),
                ('mobile', '=', post.get('mobile')),
                ('name', '=', post.get('user')),
            ])
            tokens_update.sudo().write({
                'state': 'done',
            })
        counter = request.env['processing'].sudo().search([
            ('counter_id', '=', counter_id),
            ('state', '=', 'in_progress')], order='create_date desc', limit=1)
        counter_details = [{
            'user': request.env.user.name,
            'counter': counter.counter_id.name,
            'department': counter.department_id.name
        }]
        tokens = request.env['tokens'].sudo().search([
            ('department_id', '=', counter.department_id.id)])
        vals = []
        si_no = 0
        for rec in tokens:
            if rec.state == 'draft':
                si_no += 1
                vals.append({
                    'si_no': si_no,
                    'counter': '',
                    'token': rec.token,
                    'called': 'No',
                    'recall': 'No'
                })
            else:
                si_no += 1
                vals.append({
                    'si_no': si_no,
                    'counter': 'Counter 1',
                    'token': rec.token,
                    'called': 'Yes',
                    'recall': 'Yes',
                    'url': '/processing/current/' + str(counter_id) + '/' +
                           str(rec.id),
                })
        call_next = request.env['tokens'].sudo().search_count([
            ('department_id', '=', counter.department_id.id),
            ('state', '=', 'draft')])
        if call_next < 1:
            call = False
        else:
            call = True
        url = '/processing/current/' + str(counter_id)
        close_url = '/processing/close/' + str(counter_id)
        return request.render('queue_management_cybrosys.view_processing',
                              {'vals': vals, 'counter': counter_details,
                               'call': call, 'url': url,
                               'close_url': close_url})

    @http.route(['/processing/current/<int:counter_id>',
                 '/processing/current/<int:counter_id>/<int:token_id>'],
                auth='public', type='http')
    def processing_current(self, counter_id, token_id=False):
        if not token_id:
            current_session = request.env['processing'].sudo().search([
                ('state', '=', 'in_progress'),
                ('counter_id', '=', counter_id),
            ])
            tokens = request.env['tokens'].sudo().search([
                ('state', '=', 'draft')], order='create_date asc', limit=1)
            vals = []
            tokens.sudo().write({
                'state': 'in_progress',
            })
            current_session.sudo().write({
                'current_token': tokens.token,
            })
            for rec in tokens:
                vals.append({
                    'user': rec.name,
                    'token': rec.token,
                    'mobile': rec.mobile,
                    'department': rec.department_id.name,
                })
        else:
            current_session = request.env['processing'].sudo().search([
                ('state', '=', 'in_progress'),
                ('counter_id', '=', counter_id),
            ])
            token = request.env['tokens'].sudo().browse(int(token_id))
            token.sudo().write({
                'state': 'in_progress',
            })
            current_session.sudo().write({
                'current_token': token.token,
            })
            vals = [{
                'user': token.name,
                'token': token.token,
                'mobile': token.mobile,
                'department': token.department_id.name,
            }]
        url = '/processing/' + str(counter_id)
        return request.render('queue_management_cybrosys.'
                              'view_processing_current', {'vals': vals,
                                                          'url': url})

    @http.route(['/processing/close/<int:counter_id>'], auth='public', type='http')
    def processing_close(self, counter_id):
        counter = request.env['counter'].sudo().browse(int(counter_id))
        counter.state = 'stopped'
        processing = request.env['processing'].sudo().search([
            ('counter_id', '=', counter_id),
            ('state', '=', 'in_progress')])
        processing.sudo().write({
            'state': 'stopped'
        })
        action_id = request.env.ref(
            'queue_management_cybrosys.counter_action')
        return request.redirect('/web#&action=%s' % action_id.id)

    @http.route(['/session/close/<int:sess_id>'], auth='public', type='http')
    def session_close(self, sess_id):
        sessions = request.env['interface'].sudo().browse(int(sess_id))
        sessions.sudo().write({
            'state': 'stopped'
        })
        action_id = request.env.ref(
            'queue_management_cybrosys.interface_action')
        return request.redirect('/web#&action=%s' % action_id.id)

    @http.route(['/display/close'], auth='public', type='http')
    def display_close(self):
        action_id = request.env.ref(
            'queue_management_cybrosys.queue_dashboard_action')
        return request.redirect('/web#&action=%s' % action_id.id)
