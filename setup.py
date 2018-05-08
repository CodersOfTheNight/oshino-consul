#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

from oshino_consul.version import get_version


setup(name="oshino_consul",
      version=get_version(),
      description="Agent for retrieving consul stats",
      author="zaibacu",
      packages=["oshino_consul"],
      install_requires=["oshino"],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=["pytest-runner"]
      )
