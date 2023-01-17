from odoo import models, fields


class Sequence(models.Model):
    _name = 'sequence'
    _description = 'Sequence'

    name = fields.Char()
