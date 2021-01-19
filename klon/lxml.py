#!/usr/bin/env python3

# 3rd parties
#
# NB we require `lxml` here, but this file is not loaded by default when you load `klon`, so you don't need to have LXML installed
# to use this library unless you specifically import `klon.lxml`
#
import lxml.etree

# klon
from .klon import Klon


class LxmlKlon(Klon):

    @classmethod
    def _create_element(cls, tag, attrib):
        return lxml.etree.Element(tag, attrib)

    @classmethod
    def _is_element(cls, obj):
        return isinstance(obj, lxml.etree._Element)  # pylint: disable=protected-access

    @classmethod
    def tostring(cls, etree, **kwargs):
        return lxml.etree.tostring(etree, **kwargs)


build_etree = LxmlKlon.build_etree  # it's a function, pylint: disable=invalid-name
