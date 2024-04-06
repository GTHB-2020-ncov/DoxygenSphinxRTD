# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# # 当前目录的上一级目录是根目录
# root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# # 添加 modules 目录到 Python 模块搜索路径
# sys.path.insert(0, os.path.join(root_path, 'modules'))

# sys.path.insert(0, os.path.abspath('../modules'))
# sys.path.insert(0, os.path.abspath('../markdowns'))
# sys.path.insert(0, os.path.abspath('../rsts'))

# -- Project information -----------------------------------------------------

project = 'test_doc'
copyright = '2024, lh'
author = 'lh'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output






    
extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "tasklist",
    "deflist",
    "dollarmath",
]

templates_path = ['_templates']
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '../build', '../markdowns', '../rsts']

language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'analytics_anonymize_ip': False,
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_logo = "./_static/机器人.png"
html_static_path = ['_static']
html_js_files = [
    'my_custom.js',
]

