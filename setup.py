#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip
from pip._internal.req import parse_requirements

# try: # for pip >= 10
#     from pip._internal.req import parse_requirements
# except ImportError: # for pip <= 9.0.3
#     from pip.req import parse_requirements

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

## workaround derived from: https://github.com/pypa/pip/issues/7645#issuecomment-578210649
parsed_requirements = parse_requirements(
    'requirements_dev.txt', # FIXME
    session='workaround'
)

parsed_test_requirements = parse_requirements(
    'requirements_dev.txt',
    session='workaround'
)


requirements = [str(ir.requirement) for ir in parsed_requirements]
test_requirements = [str(tr.requirement) for tr in parsed_test_requirements]


setup(
    name='onestopshop',
    version='0.1.0',
    description="Tools for work",
    long_description=readme + '\n\n' + history,
    author="Eric Johnson",
    author_email='edj36@cornell.edu',
    url='https://github.com/edj36/onestopshop',
    # packages=[
    #     'onestopshop',
    # ],
    packages=find_packages('src', exclude=['test']),
    # package_dir={'onestopshop':
    #              'onestopshop'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    # keywords='onestopshop',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
