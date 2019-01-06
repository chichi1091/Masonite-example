""" Blog Model """

from config.database import Model
from orator.orm import belongs_to
from .User import User


class Blog(Model):
    """Blog Model
    """
    __fillable__ = ['title', 'user_id', 'body']

    @belongs_to('user_id', 'id')
    def author(self):
        return User
