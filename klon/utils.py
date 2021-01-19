#!/usr/bin/env python3

# 3rd parties
import lxml.etree as ET


def is_etree(obj):
    return isinstance(obj, ET._Element)  # pylint: disable=protected-access


def tostring(etree, **kwargs):
    return ET.tostring(etree, **kwargs)
