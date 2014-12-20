#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jianming'
SITENAME = u'vfxware'
SITEURL = 'http://vfxware.com'
GITHUB_URL = 'http://github.com/tomriddle1234'


#this is for development only
RELATIVE_URLS = True

THEME = "pelican-bootstrap3"
DISPLAY_CATEGORIES_ON_MENU = False

DISQUS_SITENAME = u"vfxware"

PATH = 'content'
STATIC_PATHS = [u"img"]

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

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
#RELATIVE_URLS = True
