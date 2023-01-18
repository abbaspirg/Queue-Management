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
    url = fields.Char()

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
        url = '/processing/' + str(self.id)
        self.state = 'opened'
        processing = self.env['processing'].sudo().search([
            ('counter_id', '=', self.id),
            ('state', '=', 'stopped')])
        processing.sudo().write({
            'state': 'in_progress'
        })
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url,
        }

    def close_processing(self):
        self.state = 'closed'
