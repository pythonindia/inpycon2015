import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = '/blog'
OUTPUT_PATH = 'output/blog'
PAGE_URL = '../{slug}.html'
PAGE_SAVE_AS = '../{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
THEME = 'theme/blog'
#ARTICLE_PATHS = ['blog']