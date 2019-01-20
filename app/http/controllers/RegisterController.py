""" A RegisterController Module """
from masonite.request import Request
from masonite.view import View
import config.application as app
from masonite.auth.Auth import Auth
from config import auth
import bcrypt


class RegisterController:
    """RegisterController
    """

    def show(self, view: View, request: Request):
        return view.render('register', {'app': app, 'Auth': Auth(request)})

    def store(self, request: Request):
        ''' Register a new user '''
        # register the user
        password = bytes(bcrypt.hashpw(
            bytes(request.input('password'), 'utf-8'), bcrypt.gensalt()
        )).decode('utf-8')

        auth.AUTH['model'].create(
            name=request.input('name'),
            password=password,
            email=request.input('email'),
        )

        if Auth(request).login(request.input(auth.AUTH['model'].__auth__), request.input('password')):
            return request.redirect('/home')

        return request.redirect('/register')