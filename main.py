from datetime import datetime

from flask import Flask, abort, render_template

from data import index_ua, root

app = Flask(__name__)


@app.context_processor
def inject_globals():
    return dict(
        debug=app.debug, now=datetime.now(), header=index_ua.header, footer=root.footer
    )


@app.route('/')
def page_index_ua():
    return render_template(
        'index_ua.html',
        apps=index_ua.apps,
    )


@app.route('/app/<sub_url>')
def page_app(sub_url):

    selected_app = index_ua.apps.get(sub_url)

    if not selected_app:
        abort(404)

    return render_template(
        'app_ua.html',
        app=selected_app,
    )


@app.errorhandler(404)
def page_404(e):
    return (
        render_template('404_ua.html'),
        404,
    )


@app.route('/en/privacy-policy')
@app.route('/privacy-policy')
def page_privacy_en():
    return render_template('privacy_en.html')
