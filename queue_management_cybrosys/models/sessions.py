from odoo import models, fields, api


class Sessions(models.Model):
    _name = 'sessions'
    _description = 'Sessions'

    name = fields.Char('Session', required=True,
                       readonly=True, default=lambda self: 'New')
    user_id = fields.Many2one('res.users',
                              default=lambda self: self.env.user)
    interface_id = fields.Many2one('interface')
    state = fields.Selection([('open', 'Open'),
                              ('in_progress', 'In Progress'),
                              ('stopped', 'Stopped'),
                              ('closed', 'Closed'),
                              ], default='open')

    def session_open(self):
        self.state = 'in_progress'

    def session_view(self):
        url = '/session/' + str(self.interface_id.id)
        self.state = 'in_progress'
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url,
        }

    def session_closing_control(self):
        self.state = 'stopped'

    def session_close(self):
        self.state = 'closed'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'sessions.seq') or 'New'
        res = super(Sessions, self).create(vals)
        return res
