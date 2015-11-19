# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='schools',
    version=version,
    description='ERP for Schools, Colleges and Other Acedemic Institutions',
    author='Frappe Technologies',
    author_email='info@frappe.io',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
