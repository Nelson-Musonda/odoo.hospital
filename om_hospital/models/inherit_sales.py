from odoo import api, fields, models


class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'

    ZRA_invoice_number = fields.Integer(string='ZRA')
    SDC_id = fields.Char(string='SDC')
    QR_code = fields.Binary(string='QR')
    valid_to = fields.Datetime(string='Valid Date')
    accepted = fields.Boolean(string='Accepted')
