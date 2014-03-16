"""Settings for pelican."""

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
#THEME = 'notmyidea'
THEME = "../../pelican-themes/tuxlite_tbs"
#THEME = "../pelican-themes/Just-Read"
#THEME = "../pelican-themes/bootlex"
#THEME = "../pelican-themes/syte"
#THEME = "../pelican-themes/dev-random"  # gives error
#THEME = "../pelican-themes/dev-random2" # gives error

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

AUTHOR = 'David Verelst'
SITENAME = 'dada-blog'
SITEURL = 'http://davidovitch.github.com/dada-blog'
GITHUB_URL = 'https://github.com/davidovitch'
FEED_DOMAIN = SITEURL
#FEED_ATOM = 'feeds/all.atom.xml'
FEED_RSS = 'feeds/all.rss.xml'
FEED_MAX_ITEMS = 20

WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
#GOOGLE_ANALYTICS = 'XX-XXXXXXX-XX'
DISQUS_SITENAME = 'dada-blog'
#TWITTER_USERNAME = 'username'

# A list of the extensions that the Markdown processor will use. Refer to the
# extensions chapter in the Python-Markdown documentation for a complete list
# of supported extensions.
MD_EXTENSIONS = (['codehilite','extra'])

# List of templates that are used directly to render content. Typically direct
# templates are used to generate index pages for collections of content
# (e.g. tags and category index pages).
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))

SOCIAL = (('Github',    'https://github.com/davidovitch'),
          ('Bitbucket', 'https://bitbucket.org/davidovitch'),
          ('Gittip',    'https://www.gittip.com/davidovitch/'), )

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Numfocus', 'http://numfocus.org/'),
          ('SciPy', 'http://www.scipy.org/'),
          ('Spyder', 'http://code.google.com/p/spyderlib/'),
          ('Gittip', 'https://www.gittip.com') )

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
    ('About', '{0}/about.html'.format(SITEURL)),
    )


