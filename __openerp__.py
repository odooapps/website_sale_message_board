# -*- coding:utf-8 -*-
{
    'name': 'eCommerce Message Board',
    'category': 'Website',
    'summary': '添加电商平台留言板',
    'website': 'https://www.odoo.com/page/e-commerce',
    'version': '1.0',
    'description': """
电商留言板
==================


消费者在电商平台上购物、消费前后对该产品以及产品提供商的服务作出评价，以供其它消费者参考并促使商家对产品和服务作出改善，帮助商家经营！
        """,
    'author': 'JP.D',
    'depends': ['website', 'sale', 'base'],
    'data': [
        'views/templates.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
}
