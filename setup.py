#
# Copyright (c) 2016 GigaSpaces Technologies Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

import sys

from setuptools import setup, find_packages

_PACKAGE_NAME = 'cloudify-aria-extensions'
_PYTHON_SUPPORTED_VERSIONS = [(2, 6), (2, 7)]

if (sys.version_info[0], sys.version_info[1]) not in _PYTHON_SUPPORTED_VERSIONS:
    raise NotImplementedError('{0} Package support Python version 2.6 & 2.7 Only'.format(_PACKAGE_NAME))

setup(
    name=_PACKAGE_NAME,
    version='4.0a13',
    description='Integration of Cloudify with ARIA',
    author='Gigaspaces',
    author_email='cosmo-admin@gigaspaces.com',
    license='LICENSE',
    package_dir={
        'aria_extension_cloudify': 'parser/aria_extension_cloudify',
        'old_parser_components': 'parser/old_parser_components'},
    packages=find_packages(include=['cloudify_aria_adapters*']) +
             find_packages(where='parser',
                           include=['aria_extension_cloudify*',
                                    'old_parser_components*']),
    install_requires=['aria==0.1.0'],
    entry_points={
        'aria_extension': [
            'adapter = cloudify_aria_adapters.context_adapter',
        ],
    }
)
