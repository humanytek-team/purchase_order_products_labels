# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models, _
from openerp.exceptions import ValidationError
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

    printer_id = fields.Many2one(
        comodel_name='printing.printer', string='Printer', required=True,
        help='Printer used to print the labels.')

    label_id = fields.Many2one(
        comodel_name='printing.label.zpl2', string='Label', required=True,
        domain=lambda self: [
            ('model_id.model', '=', 'product.label.line')],
        help='Label to print.')

    order_id = fields.Many2one(
        comodel_name='purchase.order', string='Order', required=True)

    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', required=True)

    @api.model
    def default_get(self, fields_list):
        values = super(PrintProductsLabels, self).default_get(fields_list)

        # Automatically select the printer, if only one is available
        printers = self.env['printing.printer'].search([])
        if len(printers) == 1:
            values['printer_id'] = printers.id

        labels = self.env['printing.label.zpl2'].search([
            ('model_id.model', '=', 'product.label.line'),
        ])

        if labels:
            values['label_id'] = labels[0].id
        else:
            raise ValidationError(
                _('Label formatting not defined')
                )

        values['order_id'] = self._context['active_id']
        PurchaseOrder = self.env['purchase.order']
        purchase_order = PurchaseOrder.browse(values['order_id'])
        values['company_id'] = purchase_order.company_id.id

        return values

    @api.multi
    def print_products_labels(self):
        """Prints report with one label per product from purchase order"""

        self.ensure_one()
        # _logger.debug('DEBUG CONTEXT %s', self._context)
        # _logger.debug('DEBUG SELF %s', self)
        # _logger.debug('DEBUG SELF LINES %s', self.line_ids)
        # order_id = self._context['active_id']
        # data = dict()
        # data['ids'] = [order_id]
        # data['line_ids'] = self.line_ids.mapped('id')
        #
        # Report = self.env['report']
        #
        # return Report.get_action(
        #     self,
        #     'purchase_order_products_labels.products_labels',
        #     data=data)

        # for line in self.line_ids:
            # for unit in range(line.product_qty):
            #     self.label_id.print_label(self.printer_id, line)

        # For tests
        self.label_id.print_label(self.printer_id, self.line_ids[0])


class ProductLabelLine(models.TransientModel):
    _name = 'product.label.line'
    _rec_name = 'product_id'

    product_id = fields.Many2one('product.product', 'Product', required=True)
    product_qty = fields.Float('Quantity', required=True)
    products_labels_wizard_id = fields.Many2one(
        'print.products.labels', 'Wizard of Products Labels', required=True)
