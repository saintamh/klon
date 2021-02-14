#!/usr/bin/env python3

from .build import build_etree
from .html import extract_js_str, make_all_urls_absolute, parse_html_etree
from .text import extract_text, normalize_spaces
from .utils import Element, detach, is_element, tostring
