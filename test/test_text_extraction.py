#!/usr/bin/env python3

# 3rd parties
import pytest

# klon
from klon import extract_text, parse_html_etree


@pytest.mark.parametrize(
    'html, expected_default, expected_multiline',
    [
        (
            '<p>This is a   <b>test!</b></p>   And it works.',
            'This is a test! And it works.',
            'This is a test!\n\nAnd it works.',
        ),
        (
            '<ul><li>one<li>two</ul>',
            'one two',
            'one\n\ntwo',
        ),
    ]
)
def test_extract_text(html, expected_default, expected_multiline):
    etree = parse_html_etree(html)
    assert extract_text(etree) == expected_default
    assert extract_text(etree, multiline=True) == expected_multiline


# include non-content tags (both for single- and multi-line extraction)
# include comments
