from flask import render_template, Markup, abort, redirect, url_for, request
from brighton import app
import logging
import datetime
import markdown
import unicodedata
from urllib.parse import urljoin
from datetime import timedelta
from werkzeug import secure_filename
from werkzeug.contrib.atom import AtomFeed
import os
import yaml
import smtplib
from config import Configuration
from send import send_message
list = []

logger = logging.getLogger(__name__)

cache = {}


@app.route('/')
def index():
    return render_template('homepage.html')




def get_page(directory, file):
    """Load and parse a page from the filesystem. Returns the page, or None if not found"""
    filename = secure_filename(file)

    if filename in cache:
        return cache[filename]

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), directory, filename))
    try:
        file_contents = open(path, encoding='utf-8').read()
    except:
        logger.exception("Failed to open file at path: %s", path)
        return None
    data, text = file_contents.split('---\n', 1)
    page = yaml.load(data)
    page['content'] = Markup(markdown.markdown(text))
    page['path'] = file

    cache[filename] = page
    return page

@app.route('/pages/<path>/')
def page(path):
    page = get_page(app.config['PAGES_DIR'], path)
    if page is None:
        abort(404)
    return render_template('page.html', page=page)


@app.route('/backref', methods=['POST','GET'])
def sendem():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(Configuration.EMAIL_ADDRESS, Configuration.PASSWORD)
    subject = request.form['email']
    msg = request.form['text1']
    subject = str(subject)
    msg = str(msg)

    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail(Configuration.EMAIL_ADDRESS, Configuration.EMAIL_ADDRESS, message)
    server.quit()
    return render_template('one.html')



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



