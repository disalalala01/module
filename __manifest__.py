# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital management',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module to manage hospital',
    'sequence': '10',
    'licence': 'AGPL-3',
    'author': 'Nartay',
    'website': 'nartay',
    'depends': [

        "mail",
        "sale",

    ],
    'demo': [],
    'data': [

        'security/ir.model.access.csv',
        'views/patient.xml',
        'data/sequence.xml',
        'views/appointment.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
