from odoo import fields, models

class IrSequence(models.Model):
    _inherit = 'ir.sequence'

    l10n_uy_letter = fields.Selection(selection='_get_l10n_uy_letters', string='Letra')

    def _get_l10n_uy_letters(self):
        return self.env['l10n_latam.document.type']._get_l10n_uy_letters()