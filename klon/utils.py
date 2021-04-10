#!/usr/bin/env python3

# standards
from typing import Any, Union, no_type_check

# 3rd parties
import lxml.etree as ET


Element = Union[ET._Element]  # this is exported, and can be used for type annotations


@no_type_check  # until lxml-stubs improves
def detach(node: Element, *, reattach_tail: bool = True) -> Element:
    parent = node.getparent()
    if parent is None:
        raise Exception('Node has no parent')
    if reattach_tail and node.tail:
        prev = node.getprevious()
        if prev is not None:
            prev.text = (prev.text + node.tail) if prev.text else node.tail
        else:
            parent = node.getparent()
            parent.text = (parent.text + node.tail) if parent.text else node.tail
    parent.remove(node)
    return node


def is_element(obj: Any) -> bool:
    return isinstance(obj, ET._Element)


def tostring(etree: Union[Element, ET._ElementUnicodeResult], **kwargs):
    if isinstance(etree, ET._ElementUnicodeResult):
        return str(etree)
    else:
        return ET.tostring(etree, **kwargs)
