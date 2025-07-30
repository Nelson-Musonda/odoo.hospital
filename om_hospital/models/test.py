from odoo import models, fields

class my_test(models.Model):
    _name = 'hospital.test'
    _description = 'Hospital Test'

    illness = fields.Text(string='illness', required=False)
    patient_id = fields.Many2one(comodel_name="hospital.patient", string="Patient")
    doctor_id = fields.Many2one(comodel_name="hospital.doctor", string="Doctor")
    date_of_test = fields.Date(string='date of test', required=False)


