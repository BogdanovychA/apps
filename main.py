from datetime import datetime

from flask import Flask, abort, render_template

from data import index_ua, root

app = Flask(__name__)


@app.context_processor
def inject_globals():
    return dict(debug=app.debug, now=datetime.now())


@app.route('/')
def index():
    return render_template(
        'index_ua.html',
        header=index_ua.header,
        apps=index_ua.apps,
        footer=root.footer,
    )


@app.route('/app/<sub_url>')
def application(sub_url):

    selected_app = index_ua.apps.get(sub_url)

    if not selected_app:
        abort(404)  # Покаже стандартну сторінку 404 замість помилки коду

    return render_template(
        'app_ua.html',
        header=index_ua.header,
        app=selected_app,
        footer=root.footer,
    )


@app.errorhandler(404)
def page_not_found(e):
    # e — це об'єкт помилки, який передає Flask
    return render_template('404.html', header=index_ua.header, footer=root.footer), 404


@app.route('/privacy-policy')
def privacy():
    return render_template('privacy.html')
