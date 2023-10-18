# -*- encoding: utf-8 -*-
from odoo import fields, models, api, _

class ResCompany(models.Model):

    _inherit = "res.company"
    def _localization_use_documents(self):
        """ Uruguay localization use documents """
        self.ensure_one()
        return True if self.country_id == self.env.ref('base.uy') else super()._localization_use_documents()