# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Print labels for products from purchase orders',
    'version': '9.0.0.1.0',
    'category': 'Purchases',
    'author': 'Humanytek',
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'depends': [
        'product',
        'purchase',
        'printer_zpl2',
        'product_season',
        'product_brand',
        'product_style_concept',
        'product_box',
        ],
    'data': [
        'report/products_labels_report.xml',
        'report/products_labels_report_templates.xml',
        'wizard/print_products_labels_view.xml',
        'views/purchase_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
