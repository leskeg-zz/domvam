from django_assets import Bundle, register



js = Bundle(
        '/static/js/jquery-1.11.1.js', 
        '/static/js/jquery-ui-1.11.1.js', 
        'django_ajax/js/jquery.ajax.min.js',
        '/static/js/filter_links.js', 
        '/static/js/script.js', 
        '/static/js/jquery-migrate-1.2.1.js', 
        '/static/js/jquery.ba-bbq.js', 
        '/static/js/jquery.maskedinput.js',
        'http://api-maps.yandex.ru/2.1/?lang=ru_RU',


            filters='uglifyjs', output='gen/packed.js')
css = Bundle(
            '/static/css/styles.css',
            # '/static/css/styles2.css',
            filters='cssmin', output='gen/packed.css')



register('js_all', js)
register('css_all', css)
