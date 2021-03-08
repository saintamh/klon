#!/usr/bin/env python3

# standards
from typing import Any, Union

# 3rd parties
import lxml.etree as ET


Element = Union[ET._Element]  # this is exported, and can be used for type annotations


def detach(node: Element, *, reattach_tail: bool = True) -> Element:
    if reattach_tail and node.tail:
        prev = node.getprevious()
        if prev is not None:
            prev.text = (prev.text or '') + node.tail
        else:
            parent = node.getparent()
            parent.text = (parent.text or '') + node.tail
    node.getparent().remove(node)
    return node


def is_element(obj: Any) -> bool:
    return isinstance(obj, ET._Element)


def tostring(etree: Union[Element, ET._ElementUnicodeResult], **kwargs):
    if isinstance(etree, ET._ElementUnicodeResult):
        return str(etree)
    else:
        return ET.tostring(etree, **kwargs)
