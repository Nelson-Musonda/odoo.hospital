from odoo import models, fields

class AccountInherit(models.Model):
    _inherit = 'account.move'

    ZRA_invoice_number = fields.Integer(string='ZRA')
    SDC_id = fields.Integer(string='SDC')
    QR_code = fields.Binary(string='QR')
    valid_to = fields.Datetime(string='Valid Date')
    accepted = fields.Boolean(string='Accepted')
