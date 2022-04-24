# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
    
setup(
    name='dl621',
    version='0.1.2',
    description='A simple library to download e621 images with embedded tags',
    long_description=readme,
    author='Ella Jameson',
    author_email='ellagjameson@gmail.com',
    url='https://github.com/nimaid/python-dl621',
    license=license,
    install_requires=["imgtag>=0.1.1"],
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'e621-dl = dl621.core:run',
        ]
    }
)

