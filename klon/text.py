#!/usr/bin/env python3

# standards
import re


BLOCK_TAGS = frozenset([
    # This list taken from https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements
    'address', 'article', 'aside', 'blockquote', 'details', 'dialog', 'dd', 'div', 'dl', 'dt', 'fieldset', 'figcaption', 'figure',
    'figcaption', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hgroup', 'hr', 'li', 'main', 'nav', 'ol', 'p',
    'pre', 'section', 'table', 'ul'
])


NON_CONTENT_TAGS = frozenset([
    'head', 'script', 'style',
])


def extract_text(etree, normalise_spaces=True, multiline=False):
    if etree is None:
        return None
    text = ''.join(_walk(etree, multiline))
    if normalise_spaces:
        if multiline:
            text = re.sub(
                r'\s+',
                lambda m: '\n\n' if '\n\n' in m.group() else '\n' if '\n' in m.group() else ' ',
                text
            ).strip()
        else:
            text = re.sub(r'\s+', ' ', text).strip()
    return text


def _walk(node, multiline):
    if node.tag in NON_CONTENT_TAGS:
        return

    if multiline:
        if node.tag == 'br':
            yield '\n'
        elif node.tag in BLOCK_TAGS:
            yield '\n\n'

    if node.text:
        yield node.text
    for child in node:
        yield from _walk(child, multiline)

    if multiline and node.tag in BLOCK_TAGS:
        yield '\n\n'
    if node.tail:
        yield node.tail
