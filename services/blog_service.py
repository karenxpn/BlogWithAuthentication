from models.blog_post_model import BlogPost, db
from models.comment_model import Comment
import datetime

class BlogService:
    def get_all_posts(self):
        posts = BlogPost.query.all()
        return posts

    def get_post_by_id(self, post_id):
        requested_post = BlogPost.query.get(post_id)
        return requested_post

    def add_post(self, form, author):
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=author,
            date=datetime.date.today().strftime('%B %d, %Y')
        )

        db.session.add(new_post)
        db.session.commit()

    def update_post(self, post, form):
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()

    def delete_post(self, post_id):
        post_to_delete = self.get_post_by_id(post_id)
        db.session.delete(post_to_delete)
        db.session.commit()

    def post_comment(self, form, user, post):
        new_comment = Comment(text=form.comment_text.data,
                              comment_author=user,
                              parent_post=post)
        db.session.add(new_comment)
        db.session.commit()


