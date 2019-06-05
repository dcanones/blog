#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

#########################################################################################
#

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

#########################################################################################
# METADATA

AUTHOR = 'David Adrián Cañones Castellano'
SITENAME = 'David Adrián Cañones'
SITESUBTITLE = '&#x1F52C; Data Scientist | &#x1F916; Machine Learning Engineer | &#x1F4B9; MBA'

#########################################################################################
# PATHS

SITEURL = ''
PATH = 'content'

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATHS = ['images', 'static', 'extra', 'downloads']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#########################################################################################
# FEEDS

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#########################################################################################
# LINKS

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/dcanones'),
          ('github', 'https://github.com/dcanones'),
          ('instagram', 'https://www.instagram.com/david_acc'),
          ('youtube', 'https://www.youtube.com/channel/UCbV9N2A5yqk6yIWyFHZB0bA'),
          ('envelope', 'mailto:davidarcano+hiring@gmail.com'),
          ('twitch', 'https://twitch.tv/dcanones'))

#########################################################################################
# CONTENT

DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
TYPOGRIFY = True

#########################################################################################
# THEME

THEME_PATH = os.path.join(BASE_PATH, 'themes')
THEME = os.path.join(THEME_PATH, 'pelican-clean-blog-master')
DISPLAY_PAGES_ON_MENU = True
HEADER_COVER = 'images/main_header/city.jpg'
CSS_OVERRIDE = 'static/css/custom.css'

COLOR_SCHEME_CSS = 'github.css'

#########################################################################################
# PLUGINS

PLUGIN_BASE = os.path.join(BASE_PATH, 'plugins')
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = [PLUGIN_BASE]
PLUGINS = ['pelican-ipynb-master.markup']
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True
