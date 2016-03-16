"""Settings related to CSS and JS compression."""

PIPELINE_CSS = {
    'pages': {
        'source_filenames': (
            'pages/css/styles.css',
        ),
        'output_filename': 'pages.css'
    },
    'common': {
        'source_filenames': (
            'common/css/bootstrap-3.2.0.css',
            'common/css/font-awesome-4.1.0/css/font-awesome.css',
         ),
        'output_filename': 'common.css'
    },
    'management': {
        'source_filenames': (
            'management/css/management.css',
         ),
        'output_filename': 'management.css'
    },
}


# NOTE: JS compression has been verified with Uglify only.
#       The default Yuglify compressor does not compress
#       Bootstrap files correctly.
#
PIPELINE_JS = {
    'chicory': {
        'source_filenames': (
            'endless_pagination/js/endless-pagination.js',
        ),
        'output_filename': 'chicory.js'
    },
    'common': {
        'source_filenames': (
            'common/js/jquery-1.11.1.js',
            'common/js/jquery.cookie-1.4.1.js',
            'common/js/bootstrap-3.2.0.js',
        ),
        'output_filename': 'common.js'
    },
}
