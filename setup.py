#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt", "r") as requirements_txt:
    requirements = requirements_txt.read().split("\n")

setup_requirements = ["pytest-runner", ]

test_requirements = ["pytest", ]

setup(
    author="Moritz Federspiel",
    author_email="mo.fe@gmx.net",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Utilities to manage qnap ts-251",
    entry_points={
        "console_scripts": [
            "qnap_home=qnap_home.cli:cli",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="qnap_home",
    name="qnap_home",
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/mofe23/qnap_home",
    version="0.1.0",
    zip_safe=False,
)
