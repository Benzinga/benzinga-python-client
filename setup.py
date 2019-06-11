#!/usr/bin/env python
from distutils.core import setup
setup(
        name='Benzinga Data Client',
        version='0.5',
        description='Python Client Library for Benzinga Data',
        author='Benzinga Developers',
        author_email='dev@benzinga.com',
        url='https://github.com/Benzinga/benzinga-python-client',
        packages= ["Benzinga Data Client"],
        install_requires=['requests'] )