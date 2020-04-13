# -*- coding: utf-8 -*-
# © 2020 FreeDoo: Juan Ignacio Úbeda <juani@freedoo.es>
# © 2020 Avanzosc: Ana Juaristi <ana@avanzosc.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
import datetime


class ResPartner(models.Model):
	_inherit = 'res.partner'

	partner_zone_id = fields.Many2one(comodel_name='partner.delivery.zone', string='Zone',
									  related="zip_id.partner_zone_id")