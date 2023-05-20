# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath('..'))
import rail

for rail_path in rail.__path__:
    sys.path.insert(0, rail_path)

print(sys.path)
    

# Use unittest mock module to shield some modules away from docs building.
# This way one does not need to install them when dealing with the doc.
from unittest.mock import MagicMock

MOCK_MODULES = [
    'qp',
    'qp.factory',
    'qp.pdf_gen',
    'qp.metrics',
    'qp.metrics.pit',
    'qp.plotting',
    'qp.utils',
    'flexcode',
    'flexzboost',
    'flexcode.regression_models',
    'flexcode.loss_functions',
    'flexcode.basis_functions',
    'fsps',
    'gal_pop_model_components',
]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = MagicMock()

sys.modules['flexcode'].regression_models.XGBoost = MagicMock
sys.modules['flexcode'].loss_functions.cde_loss = MagicMock

# -- Project information -----------------------------------------------------

project = 'RAIL'
copyright = '2019-2021, LSST DESC RAIL Contributors'
author = 'LSST DESC RAIL Contributors'

# The short X.Y version
from rail.core import _version
version = "%i.%i" % (_version.version_tuple[0], _version.version_tuple[1])
# The full version, including alpha/beta/rc tags
release = _version.version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'setup.rst',
                    'source/index_body.rst', 'api/rail.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Allow NB to fail
nbsphinx_allow_errors = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {'prev_next_buttons_location': None,
                      'collapse_navigation': False,
                      'titles_only': False}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/notebooks.css',
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'raildoc'


# -- Options for Autodoc--------------------------------------------------
# Autodoc collects docstrings and builds API pages
# from sphinxcontrib.apidoc import main as apidoc_main

def run_apidoc(_):
    os.system('ln -s ../examples')

    import rail
    from rail.core import RailEnv
    
    from sphinx.ext.apidoc import main as apidoc_main
    cur_dir = os.path.normpath(os.path.dirname(__file__))
    output_path = os.path.join(cur_dir, 'api')

    for full_path in rail.__path__:
        paramlist = ['--separate', '--implicit-namespaces', '--no-toc', '-M', '-o', output_path, '-f', full_path]
        print(f"running {paramlist}")
        apidoc_main(paramlist)

    RailEnv.do_api_rst()


def setup(app):
    app.connect('builder-inited', run_apidoc)


