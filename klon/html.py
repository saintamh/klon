#!/usr/bin/env python3

# standards
from urllib.parse import urljoin

# 3rd parties
import lxml.etree as ET


TAGS_WITH_URL_ATTRIBUTES = {
    'a': 'href',
    'area': 'href',
    'audio': 'src',
    'base': 'href',
    'blockquote': 'cite',
    'del': 'cite',
    'embed': 'src',
    'form': 'action',
    'frame': 'src',
    'iframe': 'src',
    'img': 'src',
    'input': 'src',
    'ins': 'cite',
    'link': 'href',
    'object': 'data',
    'script': 'src',
    'source': 'src',
    'track': 'src',
    'video': 'src',
}


XPATH_TAGS_WITH_URL_ATTRIBUTES = '//*[%s]' % ' or '.join(
    f'self::{tag}' for tag in sorted(TAGS_WITH_URL_ATTRIBUTES)
)


def parse_html_etree(html_str):
    return ET.HTML(html_str)


def make_all_urls_absolute(base_url, etree):
    """
    Modify all links in the given HTML etree to be absolute URLs, using the given `base_url` to resolve relative URLs.
    """
    print(XPATH_TAGS_WITH_URL_ATTRIBUTES)
    for node in etree.xpath(XPATH_TAGS_WITH_URL_ATTRIBUTES):
        attr = TAGS_WITH_URL_ATTRIBUTES[node.tag]
        value = node.get(attr)
        if value is not None:
            absolute_url = urljoin(base_url, value)
            if absolute_url != value:
                node.set(attr, absolute_url)
