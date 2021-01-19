#!/usr/bin/env python3

# standards
from pathlib import Path
import re
import setuptools


LONG_DESCRIPTION = (Path(__file__).parent / 'README.md').read_text('UTF-8')


KLON_VERSION = re.search(
    r"KLON_VERSION = \'(.+)\'",
    (Path(__file__).parent / 'klon' / 'version.py').read_text('UTF-8'),
).group(1)


setuptools.setup(
    name='klon',
    version=KLON_VERSION,
    author='Hervé Saint-Amand',
    author_email='klon@saintamh.org',
    description='Utilities for building ElementTrees',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/saintamh/klon/',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Text Processing :: Markup :: XML',
    ],
)
