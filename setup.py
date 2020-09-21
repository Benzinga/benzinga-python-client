#!/usr/bin/env python
with open("README.md", "r") as fh:
    long_description = fh.read()
import setuptools
setuptools.setup(
        name='benzinga',
        version='1.17',
        description='Python Client Library for Benzinga Data',
        author='Benzinga Developers',
        author_email='dev@benzinga.com',
        url='https://github.com/Benzinga/benzinga-python-client',
        packages=["benzinga"],
        install_requires=['requests',
                          "structlog",
                          "urllib3==1.25.10"],
        long_description = long_description,
        long_description_content_type="text/markdown",
        classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
)