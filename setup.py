#!/usr/bin/env python
# flake8: ignore=E501
#
# Copyright 2012 Canonical Ltd.  This software is licensed under the
# GNU General Public License version 3 (see the file LICENSE).

import os
import subprocess
import sys
import json
from setuptools import setup, find_packages


curdir = os.path.dirname(__file__)
version_cache = os.path.join(curdir, 'charmtools', 'VERSION')
version_script = os.path.join(curdir, 'charmtools', 'git_version.py')
version_raw = subprocess.check_output([sys.executable, version_script,
                                       '--format=json']).strip()
if sys.version_info >= (3, 0):
    version_raw = version_raw.decode('UTF-8')
version = json.loads(version_raw)['version']
if version == 'unknown':
    # during install; use cached VERSION
    with open(version_cache, 'r') as fh:
        version_raw = fh.read()
    version = json.loads(version_raw)['version']
else:
    # during build; update cached VERSION
    with open(version_cache, 'w') as fh:
        fh.write(version_raw)

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fh:
    readme = fh.read()


setup(
    name='charm-tools',
    version=version,
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'launchpadlib<1.11',
        'cheetah3>=3.0.0',
        'pyyaml>=3.11,<4.3',
        'requests<=2.20.1',
        'libcharmstore',
        'blessings<=1.6',
        'ruamel.yaml<=0.10.23',
        'pathspec<=0.3.4',
        'otherstuf<=1.1.0',
        # 'path.py<=8.1.2',
        'path.py>=10.5',
        'pip>=1.5.4',
        # 'jujubundlelib',
        'virtualenv>=1.11.4',
        'colander<=1.7.0',
        'jsonschema<=2.5.1',
        'secretstorage<2.4',
        'dict2colander==0.2',
    ],
    include_package_data=True,
    maintainer='Marco Ceppi',
    maintainer_email='marco@ceppi.net',
    description=('Tools for maintaining Juju charms'),
    long_description=readme,
    license='GPL v3',
    url='https://github.com/juju/charm-tools',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'charm-add = charmtools.generate:main',
            'charm-build = charmtools.build.builder:main',
            'charm-create = charmtools.create:main',
            'charm-help = charmtools.cli:usage',
            'charm-layers = charmtools.build.builder:inspect',
            'charm-proof = charmtools.proof:main',
            'charm-pull-source = charmtools.pullsource:main',
            'charm-version = charmtools.version:main',
        ],
        'charmtools.templates': [
            'bash = charmtools.templates.bash:BashCharmTemplate',
            'reactive-python = charmtools.templates.reactive_python:ReactivePythonCharmTemplate',
            'reactive-bash = charmtools.templates.reactive_bash:ReactiveBashCharmTemplate',
            'python-basic = charmtools.templates.python:PythonCharmTemplate',
            'python = charmtools.templates.python_services'
            ':PythonServicesCharmTemplate',
            'ansible = charmtools.templates.ansible:AnsibleCharmTemplate',
            'chef = charmtools.templates.chef:ChefCharmTemplate',
            'powershell = charmtools.templates.powershell:PowerShellCharmTemplate',
        ]
    },
)
