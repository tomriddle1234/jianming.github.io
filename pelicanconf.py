#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Text config
AUTHOR = u'Jianming'
SITENAME = u'vfxware'
SITEURL = 'http://vfxware.com'
GITHUB_URL = 'http://github.com/tomriddle1234'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'en'

# Looks
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = "slate"
CUSTOM_CSS = 'static/custom.css'
PYGMENTS_STYLE = 'monokai'
DISPLAY_CATEGORIES_ON_MENU = False

# Comment configuration
DISQUS_SITENAME = u"vfxware"

# Make configuration
PATH = 'content'
STATIC_PATHS = [u"img",u"extra"]
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

# Plugins configuration
PLUGIN_PATHS = ["plugins","/home/tom/src/pelican-plugins"]

PLUGINS = ["sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),)
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ((u'WeChat', 'weixin://contacts/profile/tomriddle_jianming'),)
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
