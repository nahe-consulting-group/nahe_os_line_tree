# -*- coding: utf-8 -*-
{
    "name": "Sale Order Line Tree view",
    "summary": """
       Creamos la lista vista y el menu para acceder a ver todas los registros de sale.order.line.""",
    "description": """
       Creamos la lista vista y el menu para acceder a ver todas los registros de sale.order.line. Es importante
       
    """,
    "author": "Nähe Consulting Group - Matias Bressanello",
    "website": "http://www.nahe.com.ar",
    "category": "Sale",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "sale",
    ],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/sale_order_line_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
