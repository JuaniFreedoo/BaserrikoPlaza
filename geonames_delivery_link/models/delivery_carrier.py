# -*- coding: utf-8 -*-
# © 2020 FreeDoo: Juan Ignacio Úbeda <juani@freedoo.es>
# © 2020 Avanzosc: Ana Juaristi <ana@avanzosc.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
import datetime



class DeliveryCarrier(models.Model):
	_inherit = 'delivery.carrier'

	city_ids = fields.Many2many(comodel_name='res.city',
								relation='delivery_city_rel',
								column1='delivery_id',
								column2='city_id',
								string='Cities')


class ResCity(models.Model):
	_inherit = 'res.city'

	delivery_carrier_ids = fields.Many2many(comodel_name='delivery.carrier',
								relation='delivery_city_rel',
								column1='city_id',
								column2='delivery_id',
								string='Delivery Methods')