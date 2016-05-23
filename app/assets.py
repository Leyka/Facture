from flask.ext.assets import Bundle

app_css = Bundle(
    'sass/milligram/milligram.sass',
    'sass/*.sass',
    filters=['sass', 'cssmin'],
    output='public/app.css'
)

lib_css = Bundle(
    'vendor/sweetalert/sweetalert.css',
    filters='cssmin',
    output='public/lib.css'
)

app_js = Bundle(
    'js/*.js',
    filters='jsmin',
    output='public/app.js'
)

