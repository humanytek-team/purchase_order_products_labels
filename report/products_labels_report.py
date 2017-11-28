# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, models
import logging
_logger = logging.getLogger(__name__)
class ProductsLabelsReport(models.AbstractModel):
    _name = 'report.purchase_order_products_labels.products_labels'

    @api.model
    def render_html(self, docids, data=None):

        Report = self.env['report']
        PurchaseOrder = self.env['purchase.order']
        ProductLabelLine = self.env['product.label.line']

        docids = data['ids']
        _logger.debug('DEBUG BEFORE')
        report = Report._get_report_from_name(
            'purchase_order_products_labels.products_labels')
        _logger.debug('DEBUG AFTER')
        docs = PurchaseOrder.browse(docids)
        line_ids = ProductLabelLine.browse(data['line_ids'])
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': docs,
            'line_ids': line_ids,
        }

        return Report.render(
            'purchase_order_products_labels.products_labels', docargs)
