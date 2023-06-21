# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pivot_table/__init__.py
from pivot_table import __version__ as version

setup(
	name='pivot_table',
	version=version,
	description='Pivot Tables using PivotTable.js',
	author='vijaywm',
	author_email='vijay_wm@yahoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
