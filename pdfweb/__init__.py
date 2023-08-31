import os
from .defaults import *
from .pdftoweb import *
from .webtopdf import *


# CREATE BASE OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_base']):
    os.mkdir(DEFAULTS['folders']['output_base'])


# PDFTOWEB: CREATE OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_pdftoweb']):
    os.mkdir(DEFAULTS['folders']['output_pdftoweb'])


# PDFTOWEB: CREATE TEMP DOCX OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_pdftoweb_temp']):
    os.mkdir(DEFAULTS['folders']['output_pdftoweb_temp'])


# PDFTOWEB: CREATE FINAL HTML OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_pdftoweb_final']):
    os.mkdir(DEFAULTS['folders']['output_pdftoweb_final'])


# WEBTOPDF: CREATE OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_webtopdf']):
    os.mkdir(DEFAULTS['folders']['output_webtopdf'])


# WEBTOPDF: CREATE TEMP PDF OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_webtopdf_temp']):
    os.mkdir(DEFAULTS['folders']['output_webtopdf_temp'])


# WEBTOPDF: CREATE FINAL PDF OUTPUT FOLDER
if not os.path.exists(DEFAULTS['folders']['output_webtopdf_final']):
    os.mkdir(DEFAULTS['folders']['output_webtopdf_final'])
