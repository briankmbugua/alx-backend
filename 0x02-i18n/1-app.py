#!/usr/bin/env python3
"""Basic Flask app.
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Flaks Babel config
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """Index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
