PIPELINE_CSS = {
    'standard': {
        'source_filenames': (
            'css/bootstrap.css',
            'css/bootstrap-responsive.css',
            'css/font-awesome.css',
        ),
        'output_filename': 'css/s-min.css',
    }
}

PIPELINE_JS = {
    'standard': {
        'source_filenames': (
            'js/libs/bootstrap.js',
        ),
        'output_filename': 'js/s-min.js',
    }
}

# We need this because of our global scoping
PIPELINE_DISABLE_WRAPPER = True

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

# This requires lessc to be installed.
# See https://connect.ucern.com/docs/DOC-258394
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

# Provide django-pipeline with the path to the less binary (in the virtuale env)
# This is being overriden in local_settings.py for local deployments
# This only applies to environments where less was installed with the fabfile
PIPELINE_LESS_BINARY = '/opt/.virtualenvs/mysite/bin lessc'
