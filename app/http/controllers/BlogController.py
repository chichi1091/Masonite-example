from app.models.Post import Post
from masonite.request import Request
from masonite.view import View


class BlogController:
    ''' Class Docstring Description '''

    def show(self, view: View):
        return view.render('blog')

    def store(self, request: Request):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id
        )

        return 'post created'
