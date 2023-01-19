from odoo import models, fields


class Tokens(models.Model):
    _name = 'tokens'
    _description = 'Tokens'

    name = fields.Char('Name')
    token = fields.Char('Token No')
    mobile = fields.Char('Mobile No')
    session_id = fields.Many2one('sessions')
    department_id = fields.Many2one('departments')
    customer_query = fields.Text()
    feedback = fields.Text()
    state = fields.Selection([('draft', 'Draft'),
                              ('in_progress', 'In Progress'),
                              ('done', 'Done'),
                              ('cancelled', 'Cancelled'),
                              ], default='draft')
    date_token = fields.Date('Date', default=fields.Date.today())
    counter_id = fields.Many2one('counter')
