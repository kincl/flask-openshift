#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='example',
      version='1.0',
      description='Example flask script',
      author='Jason Kincl',
      packages=find_packages(),
      install_requires=["gunicorn"],
     )
