# -*- coding: utf-8 -*-
# © 2020 FreeDoo: Juan Ignacio Úbeda <juani@freedoo.es>
# © 2020 Avanzosc: Ana Juaristi <ana@avanzosc.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
import datetime


class ResCity(models.Model):
	_inherit = 'res.city'

	partner_zone_id = fields.Many2one(comodel_name='partner.delivery.zone', string='Zone')


class PartnerDeliveryZone(models.Model):
	_inherit = 'partner.delivery.zone'

	city_ids = fields.One2many(comodel_name="res.city",
							   inverse_name="partner_zone_id",
							   string="Cities")

class ResCityZip(models.Model):
	_inherit = 'res.city.zip'

	partner_zone_id = fields.Many2one(comodel_name='partner.delivery.zone',
							  		  string='Zone',
									  related='city_id.partner_zone_id')
