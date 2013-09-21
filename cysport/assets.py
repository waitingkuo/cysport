from flask.ext.assets import Bundle, Environment

js_common = Bundle(
    'common/js/jquery.js',
    'common/js/bootstrap.js',
)

css_common = Bundle(
    'common/css/bootstrap.css',
    #'common/css/bootstrap-theme.css',
)

css_base = Bundle(
    'site/scss/base.scss',
    filters='scss',
    output='site/css/base.css',
)

css_index = Bundle(
    'site/scss/index.scss',
    filters='scss',
    output='site/css/index.css',
)

css_product_line = Bundle(
    'site/scss/product-line.scss',
    filters='scss',
    output='site/css/product-line.css',
)

def register_assets(app):
    """ Register Assets to the app """

    # Make Environment
    assets = Environment(app)

    # Register assets
    assets.register('js_common', js_common)
    assets.register('css_common', css_common)
    assets.register('css_base', css_base)
    assets.register('css_index', css_index)
    assets.register('css_product_line', css_product_line)

    # Init App
    assets.init_app(app)
