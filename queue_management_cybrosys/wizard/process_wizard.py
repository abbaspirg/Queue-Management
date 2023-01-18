from odoo import models, fields


class ProcessWizard(models.TransientModel):
    _name = 'process.wizard'
    _description = 'Process Wizard'

    department_id = fields.Many2one('departments')

    def process_start(self):
        counter_id = self._context.get('active_id')
        url = '/processing/' + str(counter_id)
        self.env['processing'].create({
            'counter_id': counter_id,
            'state': 'in_progress',
            'department_id': self.department_id.id,
        })
        counter = self.env['counter'].browse(int(counter_id))
        counter.state = 'opened'
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': url,
        }
