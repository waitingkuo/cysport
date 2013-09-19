from flask.ext.assets import Bundle, Environment

js_common = Bundle(
    'common/js/jquery.js',
    'common/js/bootstrap.js',
)

css_common = Bundle(
    'common/css/bootstrap.css',
    'common/css/bootstrap-theme.css',
)

css_base = Bundle(
    'site/scss/base.scss',
    filters='scss',
    output='site/css/base.css',
)

def register_assets(app):
    """ Register Assets to the app """

    # Make Environment
    assets = Environment(app)

    # Register assets
    assets.register('js_common', js_common)
    assets.register('css_common', css_common)
    assets.register('css_base', css_base)

    # Init App
    assets.init_app(app)
