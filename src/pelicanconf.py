#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Michael Hanke'
SITENAME = u'studyforrest.org'
SITESUBTITLE = u'A de-centralized mass-collaboration attempt'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

THEME = '../pelican-bootstrap3'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Psyinf lab', 'http://psychoinformatics.de'),
          ('NeuroDebian', 'http://neuro.debian.net'),
          ('PyMVPA', 'http://www.pymvpa.org'))

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/studyforrest'),
          ('github', 'http://github.com/hanke/gumpdata'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False

#FAVICON = '../pics/favicon.png'

BOOTSTRAP_NAVBAR_INVERSE = False
#BOOTSTRAP_THEME = 'united'

DOCUTIL_CSS = True
CUSTOM_CSS = 'css/forrest.css'

TYPOGRIFY = False

STATIC_PATHS = ['images', 'pics', 'css', 'js', 'data']

#MENUITEMS = [('First', 'crzy URL')]

#PLUGIN_PATH = '../pelican-plugins'
#PLUGINS = ['html_entity', ]

DISPLAY_PAGES_ON_MENU = True

DISPLAY_TAGS_INLINE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True


CC_LICENSE = 'CC-BY-SA'

ADDTHIS_PROFILE = 'ra-53a573780cc42d73'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

DISQUS_SITENAME = 'studyforrest'

#ABOUT_ME = "Some crap on me"
#AVARTAR = "img"

GOOGLE_ANALYTICS = "UA-46839658-1"


#TWITTER_USERNAME = 'studyforrest'
#TWITTER_WIDGET_ID = '435327568237965312'

# Tell Pelican to change the path to 'static/custom.css' in the output dir
#EXTRA_PATH_METADATA = {
#    'pages/challenge.rst': {'path': 'challenge.html'}
#}

WITH_FUTURE_DATES = False

SHOW_ARTICLE_AUTHOR = True
