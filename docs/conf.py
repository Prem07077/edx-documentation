# Shared configuration for edX docs.

import datetime
import os
import sys
from pathlib import Path


# What release line is this? Use "master" for master, and the release name
# on release branches. Zebrawood should have "zebrawood".
release_line = "master"

# The slug that is used by ReadTheDocs for this version of the projects.
project_version = "latest" if (release_line == "master") else f"open-release-{release_line}.master"

# on_rtd is whether we are on readthedocs.io, this line of code grabbed from docs.readthedocs.io
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# OK, this is gross: I don't know of a way to find out what builder is running,
# so let's examine the command line, and take the word after -b.
try:
    the_builder = sys.argv[sys.argv.index("-b") + 1]
except ValueError:
    the_builder = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'sphinx.ext.graphviz',
    'sphinx_reredirects',
]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

html_context = {}

if on_rtd:
    html_context["on_rtd"] = on_rtd
    html_context["google_analytics_id"] = ''
    html_context["disqus_shortname"] = 'edx'
    html_context["github_base_account"] = 'edx'
    html_context["github_project"] = 'edx-documentation'

html_theme = 'sphinx_book_theme'
path_to_docs = '/'.join(Path.cwd().parts[-3:])

# html_theme_path = []
html_theme_options = {
    "repository_url": "https://github.com/Prem07077/edx-documentation",
    "repository_branch": "master",
    "path_to_docs": path_to_docs,
    "home_page_in_toc": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "navigation_with_keys": False,
    # Please don't change unless you know what you're doing.
    "extra_footer": """
        <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">
            <img
                alt="Creative Commons License"
                style="border-width:0"
                src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png"/>
        </a>
        <br>
        These works by
            <a
                xmlns:cc="https://creativecommons.org/ns#"
                href="https://openedx.org"
                property="cc:attributionName"
                rel="cc:attributionURL"
            >The Axim Collaborative</a>
        are licensed under a
            <a
                rel="license"
                href="https://creativecommons.org/licenses/by-sa/4.0/"
            >Creative Commons Attribution-ShareAlike 4.0 International License</a>.
    """
}
html_theme_options['navigation_depth'] = 3

html_logo = "https://logos.openedx.org/open-edx-logo-color.png"
html_favicon = "https://logos.openedx.org/open-edx-favicon.ico"

# Help and Feedback links. These are customized for the category and audience
# of the book. Add a line to the book's conf.py like this:
#
# set_audience(PARTNER, COURSE_TEAMS)
#

# Categories
PARTNER = object()
OPENEDX = object()

# Audiences
COURSE_TEAMS = object()
LEARNERS = object()
RESEARCHERS = object()
DEVELOPERS = object()

HELP_LINKS = {
    (PARTNER, COURSE_TEAMS): {
        'help_url': None, #"https://partners.edx.org/forums/partner-forums",
        'help_link_text': None,
    },
    (PARTNER, LEARNERS): {
        'help_url': "https://support.edx.org",
        'help_link_text': "Contact Support",
    },
    (PARTNER, RESEARCHERS): {
        'help_url': "http://edx.readthedocs.io/projects/devdata/en/latest/front_matter/preface.html#resources-for-researchers",
        'help_link_text': "Get Help",
    },
    (PARTNER, DEVELOPERS): {
        'help_url': "https://open.edx.org/getting-help",
        'help_link_text': "Get Help",
    },
    (OPENEDX, LEARNERS): {
        'help_url': None,
        'help_link_text': None,
    },
    (OPENEDX, COURSE_TEAMS): {
        'help_url': "https://open.edx.org/getting-help",
        'help_link_text': "Get Help",
    },
    (OPENEDX, DEVELOPERS): {
        'help_url': "https://open.edx.org/getting-help",
        'help_link_text': "Get Help",
    },
}

# Defaults for the help links.
html_context.update({
    'help_url': None,
    'help_link_text': None,
    'feedback_form_link_text': "Give Doc Feedback",
})

def set_audience(category, audience):
    """Used from specific conf.py files to set the audience for a book."""
    help_data = HELP_LINKS.get((category, audience))
    if help_data:
        html_context.update(help_data)

# General information about the project.

print(html_context)

copyright = '{year}, The Axim Collaborative'.format(year=datetime.datetime.now().year)

# Intersphinx manages the connections between books.
# Normally the references in a book are downloaded from readthedocs. But you
# can also provide a local file to look in. It's easier to fix broken
# references between books if you can do a local build and use the local
# reference files. These helper functions are for both reducing the repetition
# in the mapping dictionary, and for optionally specifying a local file to look
# in if it exists.
#
# We often use the same directory to build two books (edX vs Open edX). In
# those cases, only use ism_location for one book, not both, or we'll be
# looking for A's references in an index built for B.
#
# openedx_rtd_url is for books that are branched and built for specific Open
# edX releases. edx_rtd_url is for books that are not.

def edx_rtd_url(slug):
    """Make a RTD URL for a book that doesn't branch for each release."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/latest/"

def openedx_rtd_url(slug):
    """Make a RTD URL for a book that branches for each release."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/{project_version}/"

def ism_location(dir_name):
    """Calculate the intersphinx_mapping location to use for a book.

    `dir_name` is the directory name under edx-documentation/en_us for the book.

    """
    objects_inv = f"../../{dir_name}/build/html/objects.inv"
    if os.path.exists(objects_inv):
        return (objects_inv, None)
    else:
        return None

intersphinx_mapping = {
    "opencoursestaff": (openedx_rtd_url("open-edx-building-and-running-a-course"), ism_location("open_edx_course_authors")),
    "data": (edx_rtd_url("devdata"), ism_location("data")),
    "partnercoursestaff": (edx_rtd_url("edx-partner-course-staff"), ism_location("course_authors")),
    "insights": (edx_rtd_url("edx-insights"), None),
    "xblockapi": (edx_rtd_url("xblock"), None),
    "xblocktutorial": (edx_rtd_url("xblock-tutorial"), ism_location("xblock-tutorial")),
    "installation": (openedx_rtd_url("edx-installing-configuring-and-running"), ism_location("install_operations")),
    "olx": (edx_rtd_url("edx-open-learning-xml"), ism_location("olx")),
    "openlearners": (openedx_rtd_url("open-edx-learner-guide"), ism_location("open_edx_students")),
    "opendevelopers": (edx_rtd_url("edx-developer-guide"), ism_location("developers")),
    "opendataapi": (edx_rtd_url("edx-data-analytics-api"), None),
    # "openreleasenotes": (edx_rtd_url("edx-release-notes"), ism_location("release_notes")),
    # "openengagements": (edx_rtd_url("edx-engagements"), ism_location("engagements")),
    # "opencommerce": (edx_rtd_url("edx-commerce"), None),
}