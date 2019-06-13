#!/usr/bin/env python
from distutils.core import setup
setup(
        name='Benzinga Python Client',
        version='0.6',
        description='Python Client Library for Benzinga Data',
        author='Benzinga Developers',
        author_email='dev@benzinga.com',
        url='https://github.com/Benzinga/benzinga-python-client',
        packages= ["Benzinga Python Client"],
        install_requires=['requests'],
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
)