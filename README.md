[![Build Status](https://travis-ci.org/saintamh/klon.svg?branch=master)](https://travis-ci.org/saintamh/klon)
[![PyPI version](https://badge.fury.io/py/klon.svg)](https://pypi.org/project/klon/)

Klon is a collection of utilities for building ElementTrees.

```python
from klon import build_etree

etree = build_etree(
    'html',
    [
        'head',
        ['title', 'Test Document'],
    ],
    [
        'body',
        ['h1#title', 'This is a test'],
        ['img', {'src': 'https://website.com/image'}],
    ]
)
```
