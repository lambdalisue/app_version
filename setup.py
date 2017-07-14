# coding=utf-8
import sys
from setuptools import setup, find_packages

NAME = 'app_version'
VERSION = '0.2.1'


def read(filename):
    import os
    from io import open
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r', encoding='utf-8') as fi:
        return fi.read()


def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)


setup_extras = {}
if sys.version_info > (3,):
    setup_extras['use_2to3'] = True


setup(
    name=NAME,
    version=VERSION,
    description='A tiny utility to get application version from pkg_resouces',
    long_description=read('README.rst'),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
    keywords='application, version',
    author='Alisue',
    author_email='lambdalisue@hashnote.net',
    url='https://github.com/lambdalisue/%s' % NAME,
    download_url='https://github.com/lambdalisue/%s/tarball/master' % NAME,
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        '': ['LICENSE',
             'README.rst',
             'TEST.rst',
             'requirements.txt',
             'requirements-test.txt',
             'requirements-docs.txt'],
    },
    zip_safe=True,
    install_requires=readlist('requirements.txt'),
    **setup_extras
)
