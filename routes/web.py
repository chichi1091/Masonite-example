"""Web Routes."""

from masonite.routes import Get, Post
from app.http.controllers.HomeController import HomeController
from app.http.controllers.LoginController import LoginController
from app.http.controllers.RegisterController import RegisterController
from app.http.controllers.BlogController import BlogController

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    Get().route('/home', HomeController.show),

    Get().route('/login', LoginController.show),
    Get().route('/logout', LoginController.logout),
    Post().route('/login', LoginController.store),

    Get().route('/register', RegisterController.show),
    Post().route('/register', RegisterController.store),

    Get().route('/blog', BlogController.show),
]
