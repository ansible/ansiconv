# -*- coding: utf-8 -*-
import sys, os

sys.path.insert(0, os.path.abspath('..'))
extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'ANSIConv'
copyright = u'2013, Daniel Horrigan'
version = '1.0.0'
release = ''

exclude_patterns = ['_build']

pygments_style = 'sphinx'


sys.path.append(os.path.abspath('_themes'))
html_theme = 'flask_small'
html_theme_options = {
    'github_fork': False,
    'index_logo': False
}
html_theme_path = ['_themes']
html_static_path = ['_static']
html_show_sourcelink = False
htmlhelp_basename = 'ansiconvdoc'


latex_elements = {}
latex_documents = [
    ('index', 'ansiconv.tex', u'ANSIConv Documentation', u'Author', 'manual'),
]


man_pages = [
    ('index', 'ansiconv', u'ANSIConv Documentation', [u'Dan Horrigan'], 1)
]


texinfo_documents = [
    ('index', 'ansiconv', u'ANSIConv Documentation', u'Dan Horrigan', 'ansiconv',
        'A Python module for converting ANSI coded text and converts it to either plain text or HTML.', 'Miscellaneous'),
]


epub_title = u'ANSIConv'
epub_author = u'Dan Horrigan'
epub_publisher = u'Dan Horrigan'
epub_copyright = u'2013, Dan Horrigan'
