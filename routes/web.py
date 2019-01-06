"""Web Routes."""

from masonite.routes import Get, Post
from app.http.controllers.HomeController import HomeController

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),

    Get().route('/home', HomeController.show),
]
