# -*- coding: utf-8 -*-
# © 2020 FreeDoo: Juan Ignacio Úbeda <juani@freedoo.es>
# © 2020 Avanzosc: Ana Juaristi <ana@avanzosc.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Delivery Geonames Zone Link',
    'category': 'Delivery',
    'summary': 'Delivery Geonames Zone Link',
    'author': 'Freedoo (juani@freedoo.es)' 'Avanzosc (ana@avanzosc.com)',
    'website': 'https://freedoo.es' 'https://avanzosc.com',
    'license': 'AGPL-3',
    'version': '13.0.1.0.0',
    'depends': [
        'geonames_delivery_link',
        'partner_delivery_zone'
    ],
    'data': [
        'views/res_city_view.xml',
        'views/res_partner_view.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
}
