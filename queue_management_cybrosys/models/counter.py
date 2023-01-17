from odoo import models, fields


class Counter(models.Model):
    _name = 'counter'
    _description = 'Counter'

    name = fields.Char()
    user_id = fields.Many2one('res.users',
                              default=lambda self: self.env.user)
    state = fields.Selection([('draft', 'Unused'),
                              ('opened', 'Opened'),
                              ('stopped', 'Stopped'),
                              ('closed', 'Closed'), ],
                             default='draft')

    def start_processing(self):
        print(self)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Select Department',
            'view_mode': 'form',
            'res_model': 'process.wizard',
            'target': 'new',
        }

    def resume_processing(self):
        print(self)

    def close_processing(self):
        print(self)
