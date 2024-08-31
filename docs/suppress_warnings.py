# suppress_warnings.py

import warnings
from sphinx.application import Sphinx

def ignore_warnings(app: Sphinx, what, name, obj, *args, **kwargs):
    # Suppress warnings related to specific message patterns
    warnings.filterwarnings('ignore', category=UserWarning, message='.*version.*')

def setup(app: Sphinx):
    app.connect('warn', ignore_warnings)
