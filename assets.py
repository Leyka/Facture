from flask.ext import assets
from facture import app

assets_env = assets.Environment(app)

assets_env.register(
    'common_css',
    assets.Bundle(
        'sass/layout.sass',
        filters=['sass', 'cssmin'],
        output='css/public.css'
    )
)

# Old
# import os
# from flask_assets import Bundle, Environment
# from webassets.loaders import PythonLoader as PythonAssetsLoader
# import assets
# from facture import app
#
# # Bundles
# common_css = Bundle(
#     'vendor/bootstrap/css/bootstrap.css',
#     Bundle(
#         'css/layout.sass',
#         filters='sass'
#     ),
#     filters='cssmin', output='public/css/common.css')
#
# # Register bundles in app environment
# assets_env = Environment(app)
# loader = PythonAssetsLoader(assets)
#
# for name, bundle in loader.load_bundles().iteritems():
#     assets_env.register(name, bundle)
