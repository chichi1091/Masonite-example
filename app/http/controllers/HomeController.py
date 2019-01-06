""" A HomeController Module """
from masonite.request import Request
from masonite.view import View
import config.application as app
from masonite.auth.Auth import Auth


class HomeController:
    """HomeController
    """

    def show(self, view: View, request: Request):
        if not Auth(Request).user():
            request.redirect('/login')
        return view.render('home', {'app': app, 'Auth': Auth(request)})
