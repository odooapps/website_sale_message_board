# -*- coding:utf-8 -*-
from openerp.osv import orm, fields


class sale_message_board(orm.Model):
    _name = "sale.message.board"
    _columns = {
        "product_id": fields.many2one("product.product"),
        "messager": fields.many2one("res.users", u"留言者"),
        "star": fields.integer(u"星级"),
        "content": fields.text(u"内容"),
        "active": fields.boolean(u"有效"),
        "parent": fields.many2one("sale.message.board", u"上级留言")
    }