# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='elections',
    version=version,
    description='Ballot Management System',
    author='Brandon Smith',
    author_email='brandon@netsmith.net',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
