from odoo import models, fields


class Processing(models.Model):
    _name = 'processing'
    _description = 'Processing'

    name = fields.Char()
    user_id = fields.Many2one('res.users',
                              default=lambda self: self.env.user)
    counter_id = fields.Many2one('counter')
    department_id = fields.Many2one('departments')
    state = fields.Selection([('open', 'Open'),
                              ('in_progress', 'In Progress'),
                              ('stopped', 'Stopped'),
                              ('closed', 'Closed'),
                              ], default='open')
    current_token = fields.Char('token')
