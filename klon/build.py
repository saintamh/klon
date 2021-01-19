#!/usr/bin/env python3

# standards
import re

# 3rd parties
import lxml.etree as ET

# klon
from .utils import is_etree


def build_etree(tag, *args):
    if not isinstance(tag, str):
        raise ValueError(f'Tag must be a str, got {tag!r}')
    attrib, args = _compile_attrib(*args)
    tag, attrib = _parse_css_style_tags(tag, attrib)
    element = ET.Element(tag, attrib)
    _append_children(element, args)
    return element


def _compile_attrib(*args):
    attrib = {}
    if len(args) > 0 and isinstance(args[0], dict):
        attrib.update(args[0])
        args = args[1:]
    return attrib, args


def _parse_css_style_tags(tag, attrib):
    match = re.search(r'^(.+?)(\#|\.)(.+)', tag)
    if match:
        tag, key, value = match.groups()
        key = {'#': 'id', '.': 'class'}[key]
        attrib[key] = value
    return tag, attrib


def _append_children(element, args):
    text_anchor = None
    for child in args:
        if child in (None, (), []):
            pass
        elif isinstance(child, str):
            if text_anchor is None:
                element.text = (element.text or '') + child
            else:
                text_anchor.tail = (text_anchor.tail or '') + child
        else:
            if not is_etree(child):
                child = build_etree(*child)
            element.append(child)
            text_anchor = child
