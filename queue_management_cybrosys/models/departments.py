from odoo import models, fields


class Departments(models.Model):
    _name = 'departments'
    _description = 'Departments'

    name = fields.Char(required=True)
