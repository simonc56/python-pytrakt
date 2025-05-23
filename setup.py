from setuptools import setup

import trakt

__author__ = 'Elan Ruusamäe, Jon Nappi'

with open('README.rst') as f:
    readme = f.read()
with open('requirements.txt') as f:
    requires = [line.strip() for line in f if line.strip()]

packages = ['trakt', 'trakt.auth']
description = ('Pythonic abstraction layer for easier scripting of the '
               'Trakt.tv REST API.')

setup(
    name='pytrakt',
    version=trakt.__version__,
    description=description,
    long_description=readme,
    author='Elan Ruusamäe',
    author_email='glen@pld-linux.org',
    url='https://github.com/glensc/python-pytrakt',
    packages=packages,
    install_requires=requires,
    license='Apache 2.0',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Freely Distributable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ]
)
