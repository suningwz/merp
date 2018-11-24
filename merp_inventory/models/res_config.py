from odoo import models, fields


class StockConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    inventory_location = fields.Many2one('stock.location',
        string='Default Inventory Location',
        readonly=False,
        related='company_id.stock_inventory_location')
