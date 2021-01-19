#!/usr/bin/env python3

# 3rd parties
import pytest

# klon
from klon import extract_text, parse_html_etree


@pytest.mark.parametrize(
    'html, expected_default, expected_multiline, expected_unnormalised',
    [
        (
            '<p>This is a   <b>test!</b></p>   And it works.',
            'This is a test! And it works.',
            'This is a test!\n\nAnd it works.',
            'This is a   test!   And it works.',
        ),
    ]
)
def test_extract_text(html, expected_default, expected_multiline, expected_unnormalised):
    etree = parse_html_etree(html)
    assert extract_text(etree) == expected_default
    assert extract_text(etree, multiline=True) == expected_multiline
    assert extract_text(etree, normalise_spaces=False) == expected_unnormalised


# include non-content tags (both for single- and multi-line extraction)
# include comments
