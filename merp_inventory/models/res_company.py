from odoo import models, fields


class Company(models.Model):
    _inherit = 'res.company'

    stock_inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location')
