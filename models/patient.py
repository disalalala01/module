from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='Patient Name')

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name' #Patients/'patient_name', if you delete this line then in view there will be shown Patients/'surname'(name)
    _order = "name_seq desc"

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age < 5:
                raise ValidationError(_("Patient must be older than 5"))

    @api.depends('patient_age')
    # @api.one #ili mozhno dobvit' etu stroku i rabotat' bez for loopa
    def set_type(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.type = 'minor'
                else:
                    rec.type = 'major'

    @api.multi
    def open_patient_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointments_count = count



    patient_name = fields.Char(string='Name', required = True)
    patient_age = fields.Integer('Age', track_visibility="always") #kind of log, tracks changes in this field and shows it in form window
    notes = fields.Text(string='Notes')
    image = fields.Binary(string='Image')
    name = fields.Char(string='Surname')
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string="Gender")
    type = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], default='minor', compute='set_type')
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    appointments_count = fields.Integer(string='Appointment', compute='get_appointment_count')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence')
        result = super(HospitalPatient, self).create(vals)
        return result