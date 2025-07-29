from odoo import api, fields, models
from . import patient

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patients Module'

    hospital = fields.Char(string='Hospital Name', required=True)
    patient_name = fields.Char(string='Patient Name', required=True)
    address = fields.Text(string='Address', required=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    num_of_dependants = fields.Integer(string='Number of Dependents', required=True)


