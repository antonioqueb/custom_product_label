# models/product_label.py

from odoo import models, fields

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(selection_add=[
        ('hexagon_label', 'Etiqueta Hexágonos')
    ], ondelete={'hexagon_label': 'set default'})
