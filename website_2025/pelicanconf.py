from markdown.extensions.toc import slugify_unicode
from dataclasses import dataclass

AUTHOR = 'PyCon Israel Team'
SITENAME = 'PyCon Israel 2025'
BIDI_DIR = dict(en='ltr', he='rtl')
SITEURL = ""

EVENT_CLAIM = (
    "PyCon Israel is a conference dedicated to the Python "
    "programming language, related technologies, and their use."
)

HEADER_BACKGROUND = "pycon-2024-panel.jpg"

BLOG_TITLE = "Updates"
BLOG_ALL = "All Updates"
BLOG_SLUG = "updates"
SPONSORS_TITLE = "Sponsors and Partners"
PAST_CONFS_TITLE = "Past PyCon Israel Conferences"
PAST_CONF_YEARS = [2024, 2023, 2022, 2021, 2019, 2018]
PAST_CONF_BASE_URL = "https://pycon.org.il/"

PATH = "content"
ARTICLE_PATHS = ['blog']

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'slugify': slugify_unicode,
        },
    },
    'output_format': 'html5',
}
# Blogroll
LINKS = (
    # ("PyCon Israel 2023", "https://pycon.org.il/2023"),
    # ("PyCon Israel 2022", "https://pycon.org.il/2022"),
    # ("PyCon Israel 2021", "https://pycon.org.il/2021"),
    # ("PyCon Israel 2019", "https://pycon.org.il/2019"),
    # ("PyCon Israel 2018", "https://pycon.org.il/2018"),
    # ("PyCon Israel 2016", "https://pycon.org.il/2016"),
#    ("Python.org", "https://www.python.org/"),
#    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/pyconil/"),
    ("youtube", "https://www.youtube.com/@PyConIsrael"),
    ("facebook", "https://www.facebook.com/pyconisrael/"),
    ("linkedin", "https://www.linkedin.com/company/pycon-israel/"),
    ("mastodon", "https://tooot.im/@pyconil/"),
    ("github", "https://github.com/Hamakor/pycon-il-2025"),
)
SOCIAL_IN_FOOTER = True

class PYCON:
    YEAR = 2025
    DATES = {
        'en': "September 9, 2025",
        'he': "9 בספטמבר 2025",
    }
    TECH_DATE = "2025-09-09"
    LOCATION = {
        'en': "Cinema City, Gelilot",
        'he': "סינמה סיטי, גלילות",
    }
    SPONSORSHIP_AVAILABLE = True

# PyConIL-flex style sponsors
SPONSOR_LEVELS = {
    '10-diamond': {
        'class': "sp-diamond",
        'name': {"en": "Diamond Sponsors", "he": "חסות יהלום" },
        },
    '20-gold': {
        'class': "sp-gold",
        'name': {"en": "Gold Sponsors", "he": "חסות זהב" },
        },
    '30-silver': {
        'class': "sp-silver",
        'name': {"en": "Silver Sponsors", "he": "חסות כסף" },
        },
    '40-friends': {
        'class': "sp-friends",
        'name': {"en": "Friend Sponsors", "he": "חסות ידידים" },
        },
    '50-partners': {
        'class': "sp-partner",
        'name': {"en": "Community Partners", "he": "שותפים וקהילה" },
        },
}

DEFAULT_PAGINATION = False
DISABLE_URL_HASH = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = "themes/PyCon-Israel-peliconf"
# STYLESHEET_URL = "/theme/css/pycon-israel-2024.css"
BRANDING_LINK = (
    None,  # Use None for language-preserving link to home
    'PyCon Israel 2025',
    'PyConIL.png',
)


@dataclass
class Button:
    href: str
    label: dict[str, str]
    active: bool = True
    tooltip: dict[str, str] = None


EVENT_CTA_BUTTONS = (
    # Button(href='https://cfp.pycon.org.il/pycon-2025/cfp', active=False,
    #        label={'en': 'Propose Content', 'he': 'הגשת הצעות תוכן'},
    #        tooltip={'en': 'The call for proposals is closed', 'he': 'הקריאה להצעות כבר נסגרה'}),
    Button(href='pages/schedule.html', active=True,
           label={'en': 'Agenda', 'he': 'תוכנית הכנס'}),
    Button(href='mailto:sponsors@pycon.org.il?subject=Sponsorship',
           label={'en': 'Become a Sponsor', 'he': 'יצירת קשר לחסויות'}),
    Button(href='https://ti.to/hamakor/pycon2025/', active=True,
           label={'en': 'Buy Tickets', 'he': 'קניית כרטיסים'}),
)
# The optional related events
RELATED_EVENTS_TITLE = dict(
    en="Related Events",
    he="אירועים קשורים",
)
RELATED_EVENTS = [
    dict(
        title={'en': 'PyCon Israel Workshops', 'he': 'סדנאות פייקון ישראל'},
        when={'en': '10.9, 09:00 and 13:00', 'he': '10.9, 9:00 ו־13:00'},
        where={
            'en': 'Reichman University, Psychology Building, Seminar room 101',
            'he': 'אוניברסיטת רייכמן, בניין פסיכולוגיה, חדר סמינרים 101'},
        description={
            'en': """
            Long sessions of intense learning by guided work,
            in small classes of up to 25 students. To attend, you need
            to buy a ticket.""",
            'he': """
            סשנים ארוכים של לימוד מעמיק דרך עבודה מודרכת,
            בכיתות קטנות של עד כ־25 תלמידות ותלמידים.
            כדי לההשתתף, יש לרכוש כרטיס.""",
        },
        map="https://www.openstreetmap.org/way/365951344",
    ),
    dict(
        title={'en': 'CFP Workshop', 'he': 'סדנת CFP'},
        when={'en': '21.4 17:30', 'he': '21.4 17:30'},
        where={
            'en': 'Bluevine, Yigal Alon 94 Tel Aviv, Floor 24',
            'he': 'משרדי Bluevine, יגאל אלון 94 תל אביב, קומה 24'},
        description={
            'en': """
            The workshop included talks and personal discussions,
            to help potential submitters become successful speakers.
            See you at the conference, and next year!""",
            'he': """
            הסדנה כללה הרצאות ושיחות פרטניות, כדי לעזור למגישות ומגישים פוטנציאליים
            להגיע להרצאה מוצלחת בכנס. להתראות בכנס, ובשנה הבאה!""",
        },
        map="https://www.openstreetmap.org/#map=18/32.068870/34.793530",
    ),
]

SOCIAL_LINKS = [
    # Peliconf version of social links
    # 1. The social name
    # 2. The social link
    # 3. The icon (get the name from materialdesignicons.com)
    # 4. A boolean, True if you want to hide the social name (and show only the icon)
    # Temporarily, just keep what we have:
    (name, link, name, True) for (name, link) in SOCIAL
]

# Peliconf: make menu
DISPLAY_PAGES_ON_MENU = True

# Additional links that will be placed in the footer navigation
# Remember that you can put pages in the footer navigation using the :nav: footer meta
FOOTER_LINKS_TITLE = {
    'en': 'Past conferences:',
    'he': 'כנסים משנים קודמות:',
}
FOOTER_LINKS = [
    (str(year), f'{PAST_CONF_BASE_URL}{year}/')
    for year in PAST_CONF_YEARS
]

IMAGE_PROCESS = {}

PLUGINS = ['i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# INDEX_SAVE_AS = 'blog_index.html'

def get_page_number(page):
    field = page.metadata.get('page_number', None)
    return int(field) if field else 0

PAGE_ORDER_BY = get_page_number
PAGE_SELECTION_FILTER = get_page_number

I18N_SUBSITES = {
    'he': {
        'SITENAME': 'פייקון ישראל 2025',
        'EVENT_CLAIM': (
            'פייקון ישראל הוא כנס המוקדש לשפת התכנות פייתון, '
            'לטכנולוגיות הקשורות אליה, ולשימוש בהן'
        ),
        'BLOG_TITLE': 'עדכונים',
        'BLOG_ALL': 'כל העדכונים',
        'PAST_CONFS_TITLE': "כנסי פייקון ישראל קודמים",
        'SPONSORS_TITLE': "חסויות ושותפים",

    }
}
I18N_UNTRANSLATED_ARTICLES = 'keep'
I18N_UNTRANSLATED_PAGES = 'keep'

LANGUAGE_NAMES = {
    'en': "English",
    'he': "עברית",
}

COPYRIGHT_YEAR = 2025
COPYRIGHT_NAME = "Hamakor and individual contributors"
COPYRIGHT = f"© Copyright {COPYRIGHT_YEAR} {COPYRIGHT_NAME}"
