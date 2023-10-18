# -*- encoding: utf-8 -*-

{
    'name': 'Localización Uruguay',
    'version': '16.0',
    'category': 'Localization',
    'description': """ Localización Uruguay. """,
    'author': 'Ivan Arriola - Autodidacta TI',
    'depends': [
        'base',
        'contacts',
        'l10n_uy',
        'l10n_latam_base',
        'l10n_latam_invoice_document'],
    'data': [
        'data/res.country.state.csv',
        'data/l10n_latam_identification_type_data.xml',
        'data/l10n_latam.document.type.csv',
        'views/account_journal_inherit_view.xml',
        'views/account_move_inherit_view.xml',
        'views/res_partner_inherit_view.xml'
    ],
    'demo': [],
    'installable': True,
}