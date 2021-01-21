#!/usr/bin/env python3

# standards
from typing import Any

# 3rd parties
import lxml.etree as ET


def detach(node: ET._Element) -> ET._Element:
    node.getparent().remove(node)
    return node


def is_etree(obj: Any) -> bool:
    return isinstance(obj, ET._Element)


def tostring(etree: ET._Element, **kwargs):
    return ET.tostring(etree, **kwargs)
