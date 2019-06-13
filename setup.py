#!/usr/bin/env python
import setuptools
setuptools.setup(
        name='benzinga',
        version='1.0.0',
        description='Python Client Library for Benzinga Data',
        author='Benzinga Developers',
        author_email='dev@benzinga.com',
        url='https://github.com/Benzinga/benzinga-python-client',
        packages= ["benzinga"],
        install_requires=['requests'],
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
)