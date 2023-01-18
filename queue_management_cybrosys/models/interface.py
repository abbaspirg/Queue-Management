from odoo import models, fields


class Interface(models.Model):
    _name = 'interface'
    _description = 'Interface'

    name = fields.Char()
    sequence_id = fields.Many2one('sequence')
    user_id = fields.Many2one('res.users',
                              default=lambda self: self.env.user)
    state = fields.Selection([('draft', 'Unused'),
                              ('opened', 'Opened'),
                              ('stopped', 'Stopped'),
                              ('closed', 'Closed'), ],
                             default='draft')

    def start_session(self):
        url = '/session/' + str(self.id)
        self.env['sessions'].create({
            'interface_id': self.id,
            'state': 'in_progress',
        })
        self.state = 'opened'
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url,
        }

    def resume_session(self):
        url = '/session/' + str(self.id)
        self.state = 'opened'
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url,
        }

    def close_session(self):
        self.state = 'draft'
