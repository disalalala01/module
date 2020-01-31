# from odoo import models, fields, api, _
# from odoo.exceptions import ValidationError
#
# class HospitalAppointment(models.Model):
#     _name = "hostpital.appointment"
#     _description = "Appointment"
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     @api.model
#     def create(self, vals):
#         if vals.get('name', _('New')) == _('New'):
#             vals['name'] = self.env['ir.sequence'].next_