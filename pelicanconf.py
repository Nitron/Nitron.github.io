#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Christopher Williams'
SITENAME = u'Christopher Williams'
SITEURL = 'http://christopher-williams.net'
GITHUB_URL = 'http://github.com/Nitron/'

TIMEZONE = 'America/New_York'

PLUGIN_PATH = 'plugins/'
PLUGINS = (
	'code_include',
)

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Marco\'s Modern Life', 'http://marcosmodernlife.com/'),
	  ('My GPG Key', 'christopher_williams.asc'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/williacb'),
          ('github', 'http://github.com/Nitron'),
	  ('bitbucket', 'http://bitbucket.org/nitron'),
	  ('linkedin', 'http://www.linkedin.com/in/cwilliams1013'),
	  ('google+', 'https://plus.google.com/105480770411888666744/posts'),
)

FILES_TO_COPY = (('extra/CNAME', 'CNAME'),
		 ('extra/christopher_williams.asc', 'christopher_williams.asc'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme settings
THEME = 'themes/waterspill-en'
SUPPRESS_CATEGORIES_ON_MENU = True
GOOGLE_ANALYTICS = 'UA-3121244-2'
