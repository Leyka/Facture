from flask.ext.assets import Bundle

app_layout_css = Bundle(
    'sass/milligram/milligram.sass',
    'sass/utils.sass',
    'sass/app.sass',
    filters=['sass', 'cssmin'],
    output='public/app.min.css'
)

public_layout_css = Bundle(
    'sass/milligram/milligram.sass',
    'sass/utils.sass',
    'sass/public.sass',
    filters=['sass', 'cssmin'],
    output='public/public.min.css'
)

lib_css = Bundle(
    'vendor/sweetalert.css',
    filters='cssmin',
    output='public/lib.min.css'
)

pdf_css = Bundle(
    'sass/milligram/_Grid.sass',
    'sass/milligram/_Table.sass',
    'sass/invoice_pdf.sass',
    filters=['sass', 'cssmin'],
    output='public/pdf.min.css'
)

app_js = Bundle(
    'js/*.js',
    filters='jsmin',
    output='public/app.min.js'
)

