import os
import sys
sys.path.insert(0, os.path.abspath('..'))
project = 'ApiNyaEr'
copyright = '2025, ErNewDev0a'
author = 'ErRickow'
release = '1.4'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo","sphinx.ext.viewcode","sphinx.ext.autodoc","sphinx_copybutton","sphinx_rtd_dark_mode"]

default_dark_mode = True
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

latex_engine = 'xelatex'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
autosectionlabel_prefix_document = True
hoverxref_auto_ref = True
hoverxref_roles = [
    'term',
]
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_logo = "logo.png"
html_show_sphinx=False
html_show_copyright=False
copybutton_prompt_text = ">>> "
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")