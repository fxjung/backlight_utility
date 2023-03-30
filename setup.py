#!/usr/bin/env python
import os
import setuptools
import logging

log = logging.getLogger(__name__)


from setuptools import find_packages


with open("requirements.txt", "r") as f:
    reqs = f.readlines()

with open("requirements_dev.txt", "r") as f:
    dev_reqs = f.readlines()

test_reqs = [
    "pytest>=3",
]

setuptools.setup(
    name="backlight_utility",
    author="Felix Jung",
    author_email="jung@posteo.de",
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Screen brightness control utility for at least Thinkpad T490",
    entry_points={
        "console_scripts": [
            "backlight_utility=backlight_utility.cli:app",
        ],
    },
    packages=find_packages(include=["backlight_utility", "backlight_utility.*"]),
    # ext_modules=cythonize("ridepy/**/*.pyx", language='c++',),
    # ext_modules=cythonize(extensions, compiler_directives={"embedsignature": True}),
    install_requires=reqs,
    extras_require={"dev": dev_reqs},
    license="MIT license",
    keywords="backlight_utility",
    test_suite="tests",
    tests_require=test_reqs,
    url="https://github.com/fxjung/backlight_utility",
    version="0.1.0",
    zip_safe=False,
)
