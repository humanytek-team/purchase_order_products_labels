# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import fields, models


class PrintProductsLabels(models.TransientModel):
    _name = 'print.products.labels'

    line_ids = fields.One2many(
        'product.label.line',
        'products_labels_wizard_id',
        'Products',
        required=True)


class ProductLabelLine(models.TransientModel):
    _name = 'product.label.line'

    product_id = fields.Many2one('product.product', 'Product', required=True)
    product_qty = fields.Float('Quantity', required=True)
    products_labels_wizard_id = fields.Many2one(
        'print.products.labels', 'Wizard of Products Labels', required=True)
