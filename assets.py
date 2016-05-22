from flask.ext import assets
from facture import app

assets_env = assets.Environment(app)

assets_env.register(
    'app_css',
    assets.Bundle(
        'sass/milligram/milligram.sass',
        'sass/*.sass',
        filters=['sass', 'cssmin'],
        output='public/app.css'
    )
)

assets_env.register(
    'lib_css',
    assets.Bundle(
        'vendor/sweetalert/sweetalert.css',
        filters='cssmin',
        output='public/lib.css'
    )
)

assets_env.register(
    'app_js',
    assets.Bundle(
        'js/*.js',
        filters='jsmin',
        output='public/app.js'
    )
)
