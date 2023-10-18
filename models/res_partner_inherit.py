# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class ResPartner(models.Model):

    _inherit = "res.partner"

    name_fantasy = fields.Char('Nombre Fantasia')