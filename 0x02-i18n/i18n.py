from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


def get_locale():
    return 'es'
    #return request.accept_languages.best_match(['en', 'es', 'de'])

babel.init_app(app, locale_selector=get_locale)

@app.route("/")
def index():
    

    #to mark as translatable use gettext from flask_babel
    anthony = gettext('anthony')

    us_num = numbers.format_decimal(12345, locale='en_US')
    ke_num = numbers.format_decimal(12345, locale='en_KE')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale='de_DE')

    d = date(2007, 4, 1)
    us_date = dates.format_date(d, locale='en_US')

    """
     if you flask_babel version you don't need the locale
     if you use the regular babel version you need the locale
    """
    de_date = format_date(d)

    ke_date = dates.format_date(d, locale='en_KE')

    dt = datetime(2008, 8, 3, 15, 30)

    us_datetime = dates.format_datetime(dt, locale='en_US')
    ke_datetime = dates.format_datetime(dt, locale='en_KE')
    de_datetime = dates.format_datetime(dt, locale='de_DE')
    results = {'us_num': us_num, 'ke_num': ke_num, 'se_num': se_num, 'de_num': de_num, 'us_date': us_date, 'de_date': de_date, 'ke_date': ke_date, 'us_datetime': us_datetime, 'ke_datetime': ke_datetime, 'de_datetime': de_datetime}
    return render_template('index.html', results=results, anthony=anthony)


if __name__ == '__main__':
    app.run(debug=True)