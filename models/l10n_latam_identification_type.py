# -*- encoding: utf-8 -*-

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class L10nLatamIdentificationType(models.Model):

    _inherit = "l10n_latam.identification.type"

    l10n_uy_code = fields.Char("UY Code")

    @api.model
    def _update_identification_core_uy(self):
        identificaction_pas = self.env['l10n_latam.identification.type'].search([('name','=','Passport')])
        identificaction_pas.write({
            'country_id' : self.env.ref('base.uy').id,
            'l10n_uy_code' : '5'
        })
        identificaction_ce = self.env['l10n_latam.identification.type'].search([('name','=','Foreign ID')])
        identificaction_ce.write({
            'active' : False
        })