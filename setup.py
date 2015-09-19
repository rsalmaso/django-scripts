#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2007-2015, Raffaele Salmaso <raffaele@salmaso.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import absolute_import, division, print_function #, unicode_literals
import io
import os
from setuptools import setup
import django_scripts


setup(
    packages=["django_scripts"],
    name="django-scripts",
    version=django_scripts.__version__,
    description = io.open(os.path.join(os.path.dirname(__file__), "README.md"), "rU").read(),
    long_description="",
    author=django_scripts.__author__,
    author_email=django_scripts.__author_email__,
    url="https://bitbucket.org/rsalmaso/django-scripts",
    license="MIT License",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
        "Development Status :: 4 - Beta",
    ],
    entry_points={
        'console_scripts': [
            'dj = django_scripts.dj:main',
            'dj2 = django_scripts.dj:main',
            'dj3 = django_scripts.dj:main',
            'rs = django_scripts.rs:main',
            'rs2 = django_scripts.rs:main',
            'rs3 = django_scripts.rs:main',
        ],
    },
    include_package_data=True,
    install_requires=["stua"],
    zip_safe=False,
)
