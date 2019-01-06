""" A HomeController Module """
from masonite.request import Request
from masonite.view import View
import config.application as app
from masonite.auth.Auth import Auth


class HomeController:
    """HomeController
    """

    def show(self, request: Request, view: View):
        if not Auth(Request).user():
            request.redirect('/login')
        return view('home', {'app': app, 'Auth': Auth(request)})
