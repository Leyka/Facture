from flask.ext import assets
from facture import app
import os

assets_env = assets.Environment(app)

assets_env.register(
    'common_css',
    assets.Bundle(
        'sass/*.sass',
        filters=['sass', 'cssmin'],
        output='public/global.css'
    )
)
