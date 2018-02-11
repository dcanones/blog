#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'David Adrián Cañones Castellano'
SITENAME = 'David Adrián Cañones'
SITESUBTITLE = 'Data Science | Machine Learning | AI | Entrepreneurship'
SITEURL = 'http://localhost:8000'

PATH = 'content'
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

STATIC_PATHS = ['images', 'static', 'extra', 'downloads']
EXTRA_PATH_METADATA = {'extra/favicon.ico':{'path':'favicon.ico'}}

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Articles URLS

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Pages URLS

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

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
          ('envelope','mailto:davidarcano+hiring@gmail.com'),
          ('twitch', 'https://twitch.tv/dcanones'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme config
THEME_PATH = os.path.join(BASE_PATH, 'themes')
THEME = os.path.join(THEME_PATH, 'pelican-clean-blog')
DISPLAY_PAGES_ON_MENU = True
HEADER_COVER = '/images/main_header/shanghai.jpg'
CSS_OVERRIDE = 'static/css/custom_style.css'

#GOOGLE_ANALYTICS = 'UA-93362002-1'
#DISQUS_SITENAME = "davidadrian-cc"

COLOR_SCHEME_CSS = 'monokai.css'

# Plugin config
PLUGIN_BASE = os.path.join(BASE_PATH, 'plugins')
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = [PLUGIN_BASE]
PLUGINS = ['pelican-ipynb.markup']
IPYNB_USE_META_SUMMARY = True
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_IGNORE_CSS = True

# Delete output while developing
DELETE_OUTPUT_DIRECTORY = True

# Typogrify

TYPOGRIFY = True