[![Build Status](https://travis-ci.org/saintamh/klon.svg?branch=master)](https://travis-ci.org/saintamh/klon)
[![PyPI version](https://badge.fury.io/py/klon.svg)](https://pypi.org/project/klon/)

Klon is a collection of Python utilities for manipulating ElementTrees. It's a
thin-ish, transparent wrapper around the [lxml.etree](https://lxml.de/api/)
module.


### klon.build_etree

Source code: [klon/build.py](klon/build.py)

A utility for building element trees using list and string literals.

```python
>>> from klon import build_etree
>>> etree = build_etree(
...     'html',
...     [
...         'head',
...         ['title', 'Test Document'],
...     ],
...     [
...         'body',
...         ['h1#title', 'This is a test'],
...         ['a', {'href': '/page'}, ['img', {'src': 'image.jpg'}]],
...         [
...             'p.text',
...             'This is a text',
...             ['br'],
...             'This is a tail',
...         ],
...     ],
... )
```

Nested lists are translated to nested elements:

- the first element in the list must be a string, and becomes the tag name
- optionally, the second element can be a dict, specifying tag attributes
- any other elements become the tag's children

As a convenience, the `id` and `class` attributes can be set directly from the
tag name string, using CSS-like syntax: `tag#id` and `tag.class`.


### klon.tostring

Source code: [klon/utils.py](klon/utils.py)

A thin wrapper around [lxml.etree.tostring](https://lxml.de/api/lxml.etree-module.html#tostring).

```python
>>> from klon import tostring
>>> print(tostring(etree, pretty_print=True))
<html>
  <head>
    <title>Test Document</title>
  </head>
  <body>
    <h1 id="title">This is a test</h1>
    <a href="/page">
      <img src="image.jpg"/>
    </a>
    <p class="text">This is a text<br/>This is a tail</p>
  </body>
</html>
```

The main difference with the underlying LXML function is that `encoding=str` by
default, i.e. it produces strings by default, rather than bytes.



### klon.extract_text

Source code: [klon/text.py](klon/text.py)

Extracts all text from the given node and its descendants.

By default, all contiguous whitespace is normalized to a single ASCII space,
and so the output will always be a single line of text. However if
`multiline=True` is specified, paragraph-breaking tags are preserved, in the
same way that a web browser would. Other whitespace is still normalized, but
the output now contains both ASCII spaces and ASCII newlines.

```python
>>> from klon import extract_text

>>> body = etree.find('body')  # using the same example etree defined above
>>> print(tostring(body, pretty_print=True))
<body>
  <h1 id="title">This is a test</h1>
  <a href="/page">
    <img src="image.jpg"/>
  </a>
  <p class="text">This is a text<br/>This is a tail</p>
</body>

>>> extract_text(body)
'This is a test This is a text This is a tail'

>>> extract_text(body, multiline=True)
'This is a test\n\nThis is a text\nThis is a tail'
```

Note that the `<p>` tag translates to a double newline, while the `<br>` tag
translates to a single `\n`, mimicking how a browser renders them.


### klon.detach

Source code: [klon/utils.py](klon/utils.py)

Takes one node as argument, and removes it from its tree. Takes care to
preserve the node's `tail` text by reattaching it to the correct position in
the tree.

```python
>>> from klon import detach

>>> print(tostring(body, pretty_print=True))
<body>
  <h1 id="title">This is a test</h1>
  <a href="/page">
    <img src="image.jpg"/>
  </a>
  <p class="text">This is a text<br/>This is a tail</p>
</body>

>>> br = detach(body.xpath('.//br')[0])

>>> print(tostring(body, pretty_print=True))
<body>
  <h1 id="title">This is a test</h1>
  <a href="/page">
    <img src="image.jpg"/>
  </a>
  <p class="text">This is a textThis is a tail</p>
</body>
```

Note that `This is a tail`, which was the `tail` of the `<br>` node, has been
preserved, in this case by appending it to the `text` of its parent node.


### klon.make_all_urls_absolute

Source code: [klon/html.py](klon/html.py)

Takes a URL and a document etree, and modifies the etree in place to convert
all relative URLs to absolute ones, using the given URL as a base. All standard
tag attributes that specify a URL (e.g. `<a href="...">`, `<img src="...">`,
`<form action="...">` etc) are converted.

```python
>>> from klon import make_all_urls_absolute

>>> print(tostring(body.find('a')))
<a href="/page"><img src="image.jpg"/></a>

>>> make_all_urls_absolute('https://site.com/path/', etree)

>>> print(tostring(body.find('a')))
<a href="https://site.com/page"><img src="https://site.com/path/image.jpg"/></a>
```


### klon.parse_form

Source code: [klon/forms.py](klon/forms.py)

Takes an ElementTree whose root is a `<form>` node, and returns a
`requests.Request` that corresponds to the request that would be sent by a
browser if the form was submitted.

```python
>>> from klon import parse_form

>>> form = build_etree(
...     'form',
...     {'method': 'POST', 'action': '/publish'},
...     [
...         'div',
...         ['input', {'name': 'title', 'value': 'Some title'}],
...     ],
...     [
...         'select',
...         {'name': 'kind'},
...         ['option', {'value': 'comment'}, 'Comment'],
...         ['option', {'value': 'question', 'selected': 'yes'}, 'Question'],
...     ],
... )

>>> request = parse_form(form, base_url='https://web.site/')
>>> request.url
'https://web.site/publish'
>>> request.method
'POST'
>>> request.data
{'title': 'Some title', 'kind': 'question'}
```