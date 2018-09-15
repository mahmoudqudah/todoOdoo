# -*- coding: utf-8 -*-
from openerp import http

# class To-do(http.Controller):
#     @http.route('/to-do/to-do/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/to-do/to-do/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('to-do.listing', {
#             'root': '/to-do/to-do',
#             'objects': http.request.env['to-do.to-do'].search([]),
#         })

#     @http.route('/to-do/to-do/objects/<model("to-do.to-do"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('to-do.object', {
#             'object': obj
#         })