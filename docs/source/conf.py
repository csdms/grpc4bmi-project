# grpc4bmi-project
import datetime


project = "grpc4bmi-project"
author = "Community Surface Dynamics Modeling System"
this_year = datetime.date.today().year
copyright = f"{this_year}, {author}"
release = "0.1"

extensions = [
    "myst_parser",
]

myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "furo"
html_title = "CSDMS grpc4bmi project"
html_static_path = ["_static"]
