#!/usr/bin/env python

import re

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'orderdesk',
]

requires = []

version = ''
with open('orderdesk/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='orderdesk-python',
    version=version,
    description='Python client for the OrderDesk API.',
    author='Todd Etzel',
    author_email='todd.etzel@gmail.com',
    url='https://github.com/toddetzel/orderdesk-python',
    packages=packages,
    package_dir={'orderdesk': 'orderdesk'},
    include_package_data=True,
    install_requires=requires,
)
