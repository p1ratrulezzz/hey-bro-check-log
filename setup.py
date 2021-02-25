# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

# dephell made a fucking duplicate .rst README...

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.md')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    long_description_content_type='text/markdown',
    name='heybrochecklog',
    version='1.3.2',
    description='A python tool for evaluating and working with EAC/XLD rip logs.',
    python_requires='==3.*,>=3.5.0',
    project_urls={"repository": "https://github.com/ligh7s/hey-bro-check-log"},
    author='lights',
    author_email='lights@tutanota.de',
    license='Apache-2.0',
    keywords='logchecker eac xld',
    entry_points={
        "console_scripts": ["heybrochecklog = heybrochecklog.__main__:runner"]
    },
    packages=[
        'heybrochecklog', 'heybrochecklog.markup', 'heybrochecklog.resources',
        'heybrochecklog.score', 'heybrochecklog.score.modules',
        'scripts.eac95_builder'
    ],
    package_dir={"": "."},
    package_data={
        "heybrochecklog.resources": [
            "*.db", "*.json", "eac/*.json", "eac95/*.json"
        ]
    },
    install_requires=['chardet==3.*,>=3.0.4', 'eac_logchecker'],
    extras_require={"dev": ["pytest==5.*,>=5.3.5"]},
)
