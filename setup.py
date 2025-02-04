#!/usr/bin/env python
import os
from setuptools import setup, find_packages
from tabtools import version

# Import multiprocessing to prevent test run problem. In case of nosetests
# (not nose2) there is probles, for details see:
# https://groups.google.com/forum/#!msg/nose-users/fnJ-kAUbYHQ/_UsLN786ygcJ
# http://bugs.python.org/issue15881#msg170215w
try:
    import multiprocessing
except ImportError:
    pass


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""

install_requires = [
    l for l in read('requirements.txt').split('\n')
    if l and not l.startswith('#')
]

setup(
    name="tabtools",
    version=version,
    packages=find_packages(),
    # test_suite="nose2.collector.collector",
    test_suite="nose.collector",
    tests_require=["nose"],
    install_requires=install_requires,

    # metadata for upload to PyPI
    author="Kirill Pavlov",
    author_email="k@p99.io",
    url="https://github.com/slothai/tabtools",
    description="Tools for tab separated files manipulation in command line",
    long_description=read('README.rst'),
    entry_points={
        "console_scripts": [
            'ttcat = tabtools.scripts:ttcat',
            'tttail = tabtools.scripts:tttail',
            'ttsort = tabtools.scripts:ttsort',
            'ttmap = tabtools.scripts:ttmap',
            'ttreduce = tabtools.scripts:ttreduce',
            'ttpretty = tabtools.scripts:ttpretty',
            'ttplot = tabtools.scripts:ttplot',
        ]
    },
    # Full list:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
)
