# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Book Library Extension',
    'version': '1.0',
	'category': 'Sales/Book_library',
    'summary': 'Book Library Exercise',
    'description': "Book Library",
    'depends': [        
        'novobi_library_book'
    ],    
    "data": [        
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/book_location_view.xml',
        'wizard/package_borrower_wizard.xml',
    ],
    'installable': True,	
    'auto_install': False,
    'license': 'LGPL-3',
}