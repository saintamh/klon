#!/usr/bin/env python3

from .build import build_etree
from .html import make_all_urls_absolute, parse_html_etree
from .text import extract_text
from .utils import detach, is_etree, tostring
