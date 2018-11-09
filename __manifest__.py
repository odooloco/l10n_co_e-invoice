# -*- coding: utf-8 -*-
# Copyright 2018 Dominic Krimmer, dominic.krimmer@gmail.com
# Copyright 2018 https://github.com/johnsh, sebastian80_23@hotmail.com
# Copyright 2018 https://github.com/exaap, EXA Auto Parts S.A.S
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': "Colombian e-invoice",
    'summary': """
        Genera la facturación electrónica para la distribución colombiana según requisitos de la DIAN""",
    'category': 'Administration',
    'version': '10.0.0.0.1',
    'license': 'AGPL-3',
    'depends': [
        'account', 'l10n_co_tax_extension',
    ],
    'data': [
    'views/dian_view.xml',
    'views/company_view.xml',
    'views/invoice_view.xml',
    'views/sequence_view.xml',
    'views/report_dian_document.xml'
    ],
    'installable': True,
}
