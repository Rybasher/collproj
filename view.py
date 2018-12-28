from flask import render_template, Markup, abort, redirect, url_for, request
from brighton import app
import logging
import datetime
import markdown
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




"""
def get_meetings():
    "Return a list of all meetings"

    if 'meeting_list' in cache:
        return cache['meeting_list']

    files = os.listdir(os.path.abspath(os.path.join(os.path.dirname(__file__), app.config['MEETINGS_DIR'])))
    meetings = filter(lambda meeting: meeting is not None, [get_meeting(file) for file in files])
    result = sorted(meetings, key=lambda item: item['datetime'])

    cache['meeting_list'] = result
    return result


def past_meetings():
    meeting_list = get_meetings()
    now = datetime.datetime.now()
    return [meeting for meeting in meeting_list if meeting['datetime'] < now]


def future_meetings():
    meeting_list = get_meetings()
    now = datetime.datetime.now()
    return [meeting for meeting in meeting_list if meeting['datetime'] > now]

"""


@app.route('/')
def index():
    return render_template('homepage.html')


#@app.route('/thank')
#def send():
 #   send_message.email(subject=request.form("text"), msg=request.form('email'))






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
    subject = request.form('name')


    msg = request.form('text')
    list.append(subject)
    list.append(msg)
    first = str(list[0])
    sec = str(list[1])






    message = 'Subject: {}\n\n{}'.format(first, sec)
    server.sendmail(Configuration.EMAIL_ADDRESS, Configuration.EMAIL_ADDRESS, message)
    server.quit()
    return render_template('one.html')



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



