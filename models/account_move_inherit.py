import logging

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    forma_pago = fields.Selection([('credito', 'Crédito'),('debito','Debito') ], 'Forma de pago', default='debito')
    
    #Si el partner de la factura tiene de tipo de identificacion RUC definimos que el tipo de documento sera eFactura
    @api.onchange('partner_id')
    def _onchange_partner_document_type(self):
        for rec in self.filtered(lambda x: x.state == 'draft'):
            document_tmp = self.env['l10n_latam.document.type']
            if rec.move_type == 'out_invoice':
                if rec.partner_id.l10n_latam_identification_type_id.l10n_uy_code == '2':
                    document_tmp = document_tmp.search([('code','=','111')])
                    rec.l10n_latam_document_type_id = document_tmp
                else:
                    document_tmp = document_tmp.search([('code','=','101')])
                    rec.l10n_latam_document_type_id = document_tmp
            elif rec.move_type == 'out_refund':
                if rec.partner_id.l10n_latam_identification_type_id.l10n_uy_code == '2':
                    document_tmp = document_tmp.search([('code','=','112')])
                    rec.l10n_latam_document_type_id = document_tmp
                else:
                    document_tmp = document_tmp.search([('code','=','102')])
                    rec.l10n_latam_document_type_id = document_tmp

    @api.model
    def create(self, values):
        #Seteamos el tipo de documento para NC cuando la factura tiene reversed_entry_id
        if 'reversed_entry_id' in values:
            document_tmp = self.env['l10n_latam.document.type']
            reversed_id = self.env['account.move'].browse(values['reversed_entry_id'])
            if reversed_id.l10n_latam_document_type_id.code == '101':
                document_tmp = document_tmp.search([('code','=','102')])
                values['l10n_latam_document_type_id'] = document_tmp.id
            if reversed_id.l10n_latam_document_type_id.code == '111':
                document_tmp = document_tmp.search([('code','=','112')])
                values['l10n_latam_document_type_id'] = document_tmp.id

        res = super(AccountMove, self).create(values)
        return res

    @api.depends('l10n_latam_available_document_type_ids', 'debit_origin_id')
    def _compute_l10n_latam_document_type(self):
        for rec in self.filtered(lambda x: x.state == 'draft'):
            document_types = rec.l10n_latam_available_document_type_ids._origin
            invoice_type = rec.move_type
            if invoice_type in ['out_refund', 'in_refund']:
                document_types = document_types.filtered(lambda x: x.internal_type not in ['debit_note', 'invoice'])
            elif invoice_type in ['out_invoice', 'in_invoice']:
                document_types = document_types.filtered(lambda x: x.internal_type not in ['credit_note'])
            if rec.debit_origin_id:
                document_types = document_types.filtered(lambda x: x.internal_type == 'debit_note')
            rec.l10n_latam_document_type_id = document_types and document_types[0].id