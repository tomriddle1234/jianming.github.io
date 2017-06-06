#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jianming Guo'
SITENAME = u'VFXWARE Blog'
SITEURL = 'http://blog.vfxware.com'

SITETITLE = 'VFXWARE'
SITESUBTITLE = 'Visual Innovations'
SITEDESCRIPTION = 'VFXWARE, the growing creative partner devotes itself on Visual Innovations.'
SITELOGO = 'img/sitelogo.png'
FAVICON = 'img/favicon.ico'


STATIC_PATHS = ['img','images', 'extra']

BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'

MAIN_MENU = True


PLUGIN_PATHS = ["plugins","/home/tom/src/pelican-plugins"]

DISQUS_SITENAME = 'vfxware'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Enable i18n plugin.
PLUGINS = ['sitemap', 'post_stats']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}


# Enable Jinja2 i18n extension used to parse translations.
#JINJA_ENVIRONMENT = {'extensions':['jinja2.ext.i18n']}

THEME = "Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Portfolio', 'http://portfolio.vfxware.com/'),)

# Social widget
SOCIAL = ( ('bitbucket', 'https://bitbucket.org/jianming_tom'),
           ('github', 'https://github.com/tomriddle1234'),
           ('google','https://plus.google.com/105506953324481647126'))


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_LESS = True
