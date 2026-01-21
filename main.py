from datetime import datetime

from flask import Flask, render_template

from data import index_ua, root

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index_ua.html',
        header=index_ua.header,
        apps=index_ua.apps,
        footer=root.footer,
        now=datetime.now(),
    )
