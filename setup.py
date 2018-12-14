#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = "0.1.1"


packages = find_packages(
    where="src"
)


install_requirements = [
    "attrs>=18.2",
    "click>=7.0"
]


setup_requirements = [
    "bumpversion>=0.5",
    "pytest-runner>=4.2"
]


test_requirements = [
    "pytest>=4.0",
    "radixal>=0.1"
]


extra_requirements = {
    "mypy": [
        "mypy",
        "pytest-mypy"
    ],
    "flake8": [
        "flake8",
        "flake8-docstrings",
        "pytest-flake8",
    ],
    "coverage": [
        "coverage",
        "pytest-cov"
    ],
    "coveralls": [
        "python-coveralls"
    ]
}


classifiers = [
    "Development Status :: 4 - Beta"
    "Intended Audience :: Developers"
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7"
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]


setup(
    name="radick",
    version=version,
    packages=packages,
    package_dir={'': 'src'},
    url="https://github.com/phuntimes/radick",
    license="MIT License",
    author="Sean McVeigh",
    author_email="spmcveigh@gmail.com",
    description="click param types for integers with arbitrary radix",
    classifiers=classifiers,
    install_requires=install_requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require=extra_requirements
)
