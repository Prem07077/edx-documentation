import datetime
import os
import sys
from pathlib import Path

# Define the release line and project version
release_line = "master"
project_version = "latest" if (release_line == "master") else f"open-release-{release_line}.master"

# Check if we are on ReadTheDocs
# Set the version and release based on the release line
version = "1.0"  # Short version string, e.g., "1.0"
release = "1.0.0"  # Full version string, e.g., "1.0.0"

if release_line == "master":
    version = "latest"
    release = "latest"
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Determine the builder
try:
    the_builder = sys.argv[sys.argv.index("-b") + 1]
except ValueError:
    the_builder = None

# Add the path to the en_us directory
source_dir = os.path.join(Path.cwd(), 'en_us')
sys.path.insert(0, source_dir)

# Sphinx configuration
master_doc = 'index'
source_suffix = '.rst'
pygments_style = 'sphinx'

# Sphinx extensions
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

# HTML output options
html_context = {}
if on_rtd:
    html_context["on_rtd"] = on_rtd
    html_context["google_analytics_id"] = ''
    html_context["disqus_shortname"] = 'edx'
    html_context["github_base_account"] = 'edx'
    html_context["github_project"] = 'edx-documentation'

html_theme = 'sphinx_book_theme'
path_to_docs = '/'.join(Path.cwd().parts[-3:])

html_theme_options = {
    "repository_url": "https://github.com/Prem07077/edx-documentation",
    "repository_branch": "master",
    "path_to_docs": path_to_docs,
    "home_page_in_toc": True,
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "navigation_with_keys": False,
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

# Help and Feedback links
PARTNER = object()
OPENEDX = object()

COURSE_TEAMS = object()
LEARNERS = object()
RESEARCHERS = object()
DEVELOPERS = object()

HELP_LINKS = {
    (PARTNER, COURSE_TEAMS): {
        'help_url': None,
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

# General information about the project
copyright = '{year}, The Axim Collaborative'.format(year=datetime.datetime.now().year)

# Intersphinx mapping
def edx_rtd_url(slug):
    """Make a RTD URL for a book that doesn't branch for each release."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/latest/"

def openedx_rtd_url(slug):
    """Make a RTD URL for a book that branches for each release."""
    return f"https://edx.readthedocs.io/projects/{slug}/en/{project_version}/"

def ism_location(dir_name):
    """Calculate the intersphinx_mapping location to use for a book."""
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
