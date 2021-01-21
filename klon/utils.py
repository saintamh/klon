#!/usr/bin/env python3

# standards
from typing import Any

# 3rd parties
import lxml.etree

Element = lxml.etree._Element  # pylint: disable=protected-access


def detach(node: Element) -> Element:
    node.getparent().remove(node)
    return node


def is_etree(obj: Any) -> bool:
    return isinstance(obj, Element)


def tostring(etree: Element, **kwargs):
    return lxml.etree.tostring(etree, **kwargs)
