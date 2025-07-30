from odoo import fields, models

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    doctor_id = fields.Integer(string="Doctor ID", required=True)
    name = fields.Char(string='Doctor Name', required=True)

    # Gender tuples to load into Selection List
    gender_male = ("Fale", "Male")
    gender_female = ("Memale", "Female")

    gender = fields.Selection(selection=[gender_male, gender_female], string="Gender", required=True)
    department = fields.Char(string="Department", required=True)
