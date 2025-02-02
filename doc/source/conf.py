import os
import sys
sys.path.insert(0, os.path.abspath('../memengine'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MemEngine'
copyright = '2025, Zeyu Zhang'
author = 'Zeyu Zhang'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_book_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# html_logo = '_static/logo.png'
html_favicon = '_static/logo.png'
html_title = "MemEngine v%s Document" % release

html_theme_options = {
    'repository_url': 'https://github.com/nuster1128/MemEngine',
    'use_repository_button': True
}