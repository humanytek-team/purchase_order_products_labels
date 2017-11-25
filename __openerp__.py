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
    'depends': ['purchase', ],
    'data': [
        'wizard/print_products_labels_view.xml',
        'views/purchase_view.xml',
    ],
    'installable': True,
    'auto_install': False
}
