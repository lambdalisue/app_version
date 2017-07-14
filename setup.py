# coding=utf-8
from setuptools import setup, find_packages

NAME = 'app_version'


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


setup(
    name=NAME,
    use_scm_version=True,
    description='A tiny utility to get application version from pkg_resouces',
    long_description=read('README.rst'),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ),
    keywords='application, version',
    author='Alisue',
    author_email='lambdalisue@hashnote.net',
    url='https://github.com/lambdalisue/%s' % NAME,
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    setup_requires=['setuptools_scm', 'pytest-runner'],
    tests_require=readlist('requirements-test.txt'),
    install_requires=readlist('requirements.txt'),
)
