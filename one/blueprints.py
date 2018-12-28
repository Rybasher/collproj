from flask import Blueprint, render_template, request,redirect, url_for
from .forms import PostForm

from models import Post, Tag
from brighton import db
from flask_security import login_required
posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['POST','GET'])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print("Something going wrong")
        return redirect( url_for('posts.index'))
    form = PostForm()
    return render_template('one/create_post.html', form=form)


@posts.route('/<slug>/edit', methods=['POST','GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post) #change post
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))
    form = PostForm(obj=post)
    return render_template('one/edit.html', post=post, form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))#.all()
    else:
        posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=5)

    return render_template('one/index.html', pages=pages)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    tags = post.tags
    return render_template('one/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first_or_404()
    posts = tag.posts.all()
    return render_template('one/tag_detail.html', tag=tag, posts=posts)




