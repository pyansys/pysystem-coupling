"""Sphinx documentation configuration file."""
from datetime import datetime
import os

from ansys_sphinx_theme import (
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_version_match,
    latex,
    pyansys_logo_black,
    watermark,
)
import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey

from ansys.systemcoupling.core import __version__

# Project information
project = "ansys-systemcoupling-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "Ansys Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "nocname.com")

# use the default pyansys logo
html_short_title = html_title = "PySystemCoupling"
html_theme = "ansys_sphinx_theme"
html_logo = pyansys_logo_black

html_context = {
    "github_user": "pyansys",
    "github_repo": "pysystem-coupling",
    "github_version": "main",
    "doc_path": "doc/source",
}

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/pyansys/pysystem-coupling",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "use_edit_page_button": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com"),
    ],
    "navigation_depth": -1,
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
}

# Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinxemoji.sphinxemoji",
    "sphinx_gallery.gen_gallery",
]

# We can't build the gallery on GitHub as it requires full System Coupling
# runs (involving Fluent, MAPDL, etc). Therefore we "pre-build" the
# gallery locally as a development activity and commit the files in
# doc/source/examples that are generated by Sphinx Gallery.
#
# The original intention was that the GitHub doc build would then simply
# build from all the rst files in doc/source, completely avoiding the
# gallery build either by excluding "gen_gallery" or setting the
# "plot_gallery" option to False. This *almost* works, but the
# thumbnail page is not generated correctly.
#
# Instead, we keep "gen_gallery" and fool Sphinx Gallery into thinking that
# the examples are up to date by monkey patching the md5sum_is_current check.
# This runs the gallery generation, ensuring that it is done correctly,
# but avoids running the examples.
#
# This was suggested at:
#    https://github.com/sphinx-gallery/sphinx-gallery/issues/704

# The default is *not* to rebuild the gallery so, to build locally, ensure
# PYSYC_BUILD_SPHINX_GALLERY is set and then commit any resultant changes
# in doc/source/examples as required.

if os.environ.get("PYSYC_BUILD_SPHINX_GALLERY") is None:
    sphinx_gallery.gen_rst.md5sum_is_current = lambda *a, **k: True

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# Favicon
html_favicon = ansys_favicon

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Copy button customization ---------------------------------------------------
# exclude traditional Python prompts from the copied code
copybutton_prompt_text = r">>> ?|\.\.\. "
copybutton_prompt_is_regexp = True

assert os.environ.get("PYSYC_DOC_BUILD_VERSION"), "PYSYC_DOC_BUILD_VERSION is not set!"


def make_replacements_for_versioned_class_refs(names):
    # returns Sphinx "substitutions" of the form
    # .. |<NAME>_ROOT_CLASS_REF| replace:: :class:`<name>_root<..path to <name>_root module>`

    api_path = (
        f"ansys.systemcoupling.core.adaptor.api_{os.environ['PYSYC_DOC_BUILD_VERSION']}"
    )

    name_root = lambda n: f"{n.lower()}_root"
    make_subst_name = lambda n: f"{n.upper()}_ROOT_CLASS_REF"
    make_class_ref = (
        lambda n: f"{name_root(n)}<{api_path}.{name_root(n)}.{name_root(n)}>"
    )

    make_subst = (
        lambda n: f".. |{make_subst_name(n)}| replace:: :class:`{make_class_ref(n)}`"
    )

    return "\n".join(make_subst(n) for n in names)


rst_epilog = make_replacements_for_versioned_class_refs(("CASE", "SETUP", "SOLUTION"))

# -- Sphinx Gallery Options ---------------------------------------------------
sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": ["../../examples/"],
    # path where to save gallery generated examples
    "gallery_dirs": ["examples"],
    # Pattern to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": None,
    # Modules for which function level galleries are created.  In
    "doc_module": "ansys-systemcoupling-core",
    "ignore_pattern": "flycheck*",
    "thumbnail_size": (350, 350),
    # "reset_modules_order": "after",
    # "reset_modules": (_stop_fluent_container),
    # "plot_gallery": False,
    # Suppress config comments like "sphinx_gallery_thumbnail_path" from being rendered
    "remove_config_comments": True,
}


# additional logos for the latex coverpage
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]

# change the preamble of latex with customized title page
# variables are the title of pdf, watermark
latex_elements = {"preamble": latex.generate_preamble(html_title)}
