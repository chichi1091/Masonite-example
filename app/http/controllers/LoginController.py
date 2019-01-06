""" A LoginController Module """
from masonite.request import Request
from masonite.view import View
import config.application as app
from masonite.auth.Auth import Auth


class LoginController:
    """LoginController
    """

    def show(self, view: View, request: Request):
        return view.render('login', {'app': app, 'Auth': Auth(request)})

    def store(self, request: Request):
        if Auth(request).login(request.input('username'), request.input('password')):
            request.redirect('/home')
        else:
            request.redirect('/login')
        return 'check terminal'

    def logout(self, request: Request):
        Auth(request).logout()
        return request.redirect('/login')
