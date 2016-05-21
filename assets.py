from flask.ext import assets
from facture import app

assets_env = assets.Environment(app)

assets_env.register(
    'common_css',
    assets.Bundle(
        'sass/layout.sass',
        filters=['sass', 'cssmin'],
        output='public/global.css'
    )
)

assets_env.register(
    'common_js',
    assets.Bundle(
        'js/*.js',
        filters='jsmin',
        output='public/app.js'
    )
)
