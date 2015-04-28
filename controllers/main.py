# -*- coding:utf-8 -*-
from openerp import http
from openerp.http import request


class website_sale_message_board(http.Controller):
    @http.route(['/shop/product/<string:product>/m_b/<int:page>'], type="http", auth="public", website=1)
    def get_message(self, product, page):
        return request.render("website_sale_message_board.message_board", {})