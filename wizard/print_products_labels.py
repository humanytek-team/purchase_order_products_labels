# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models
import logging
_logger = logging.getLogger(__name__)
class PrintProductsLabels(models.TransientModel):
    _name = 'print.products.labels'

    def _compute_default_line_ids(self):
        """Computes default value for field line_ids"""

        order_id = self._context['active_id']
        PurchaseOrder = self.env['purchase.order']
        purchase = PurchaseOrder.browse(order_id)
        value = list()

        for line in purchase.order_line:
            value.append(
                (0, 0,
                 {'product_id': line.product_id.id,
                  'product_qty': line.product_qty,
                 })
            )

        return value

    line_ids = fields.One2many(
        'product.label.line',
        'products_labels_wizard_id',
        'Products',
        required=True,
        default=_compute_default_line_ids)

    @api.multi
    def print_products_labels(self):
        """Prints report with one label per product from purchase order"""

        self.ensure_one()
        _logger.debug('DEBUG CONTEXT %s', self._context)
        _logger.debug('DEBUG SELF %s', self)
        _logger.debug('DEBUG SELF LINES %s', self.line_ids)
        order_id = self._context['active_id']
        data = dict()
        data['ids'] = [order_id]
        data['line_ids'] = self.line_ids.mapped('id')

        Report = self.env['report']

        return Report.get_action(
            self,
            'purchase_order_products_labels.products_labels',
            data=data)


class ProductLabelLine(models.TransientModel):
    _name = 'product.label.line'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', 'Product', required=True)
    product_qty = fields.Float('Quantity', required=True)
    products_labels_wizard_id = fields.Many2one(
        'print.products.labels', 'Wizard of Products Labels', required=True)
