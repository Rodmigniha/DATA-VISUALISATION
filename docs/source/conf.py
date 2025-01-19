import os
import sys
# Ensure that Sphinx can find and import the necessary Python 
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DATA-VIZ'
copyright = '2025, Rodrigue'
author = 'Rodrigue'

# The full version, including alpha/beta/rc tags
release = '0.1.0'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
     'sphinx.ext.autodoc',
     'sphinx.ext.viewcode',
     'sphinx.ext.napoleon',
     'sphinx.ext.githubpages'
]
# Add any paths that contain templates here, relative to this 
templates_path = ['_templates']

exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
html_static_path = ['_static']
