from odoo import models, api, fields, _


class L10nLatamDocumentType(models.Model):

    _inherit = 'l10n_latam.document.type'
    
    l10n_uy_letter = fields.Selection(
        selection='_get_l10n_uy_letters',
        string='Letters',)

    def _get_l10n_uy_letters(self):
        """ Return the list of values of the selection field. """
        return [
            ('et', 'eTicket'),
            ('NCeT', 'Nota de crédito de eTicket'),
            ('NDeT', 'Nota de débito de eTicket'),
            ('eF', 'eFactura'),
            ('NCeF', 'Nota de crédito de eFactura'),
            ('NDeF', 'Nota de débito de eFactura'),
            ('121', 'eFactura de exportación'),
            ('122', 'Nota de crédito de eFactura de exportación'),
            ('123', 'Nota de débito de eFactura de exportación'),
            ('124', 'eRemito de exportación'),
            ('131', 'eTicket Venta por cuenta ajena'),
            ('132', 'NC eTicket Venta por cuenta ajena'),
            ('133', 'ND eTicket venta por cuenta ajena'),
            ('141', 'eFactura Venta por cuenta ajena'),
            ('142', 'NC eFactura Venta por cuenta ajena'),
            ('143', 'ND eFactura venta por cuenta ajena'),
            ('151', 'eBoleta de entrada'),
            ('152', 'NC eBoleta de entrada'),
            ('153', 'ND eBoleta de entrada'),
            ('181', 'eRemito'),
            ('182', 'eResguardo')
        ]

    def _get_document_sequence_vals(self, journal):
        """ Values to create the sequences """
        values = super()._get_document_sequence_vals(journal)
        if self.country_id != self.env.ref('base.uy'):
            return values
        prefijo="%s-" % (journal.l10n_uy_cod_sucursal)
        values.update({'name': '%s - %s' % (journal.name, self.name),
                        'l10n_latam_document_type_id': self.id,
                        'padding': 5,
                        'implementation': 'no_gap',
                        'prefix': prefijo,
                        'l10n_latam_journal_id': journal.id})
        return values