#!/usr/bin/env/python

from setuptools import setup, find_packages


setup(
    name="sgm",
    author="...",
    classifiers=[],
    packages=find_packages(),
    install_requires=[
        'cython==0.29.7',
        'tqdm',
        'numpy',
        'pandas',
        'lap @ git+https://github.com/nowfred/lap.git@v0.5.0#egg=lap',
        'lapjv @ git+https://github.com/nowfred/lapjv.git@v1.4.1#egg=lapjv'
    ],
    version="1.0.2"
)