from odoo import fields, models, api, _
from odoo.exceptions import ValidationError, RedirectWarning


class AccountJournalInherit(models.Model):
    _inherit = "account.journal"

    l10n_uy_cod_sucursal = fields.Integer("Código de sucursal")