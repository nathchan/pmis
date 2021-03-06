# -*- coding: utf-8 -*-
#    Copyright (C) 2017 Luxim d.o.o. (Matjaž Mozetič)
#    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import models, api, _


class FormView(models.Model):
    _inherit = 'project.task'

    @api.multi
    def button_save_data(self):
        return True

    @api.multi
    def action_open_task_form(self):
        context = self.env.context.copy()
        context['view_buttons'] = True
        view = {
            'name': _('Details'),
            'view_type': 'form',
            'view_mode': 'form,tree,kanban,gantt',
            'res_model': 'project.task',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': self.id,
            'context': context
        }
        return view
