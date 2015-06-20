#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Your Name"
SITENAME = "Your site's name"
SITEURL = "http://yoursite.tld"

TIMEZONE = 'Europe/Paris'
GOOGLE_ANALYTICS = ""

DEFAULT_LANG = u'en'

THEME = "/path/to/vareid"

# Feed generation disabled
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Set following variable to true if you want document-relative URLs (when developing)
RELATIVE_URLS = True

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

CATEGORY_URL = '{slug}/index.html'
CATEGORY_SAVE_AS = '{slug}/index.html'

PAGE_URL = '{slug}/index.html'
PAGE_SAVE_AS = '{slug}/index.html'

# Disable output
TAG_URL = ''
TAG_SAVE_AS = ''
TAGS_URL = ''
TAGS_SAVE_AS = ''
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_URL = ''
AUTHORS_SAVE_AS = ''

# Custom navigation link array for displaying links in the header
NAVIGATION_LINKS = [
    #{"name": "Home", "url": ""},
    #{"name": "Blog", "url": "blog/"},
    #{"name": "About", "url": "about/"},
]

PLUGIN_PATHS = ('/Path/to/pelican-plugins',)
PLUGINS = ['assets']

ASSET_CONFIG = (('less_bin', 'lessc'), )
