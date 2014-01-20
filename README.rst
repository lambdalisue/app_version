app_version
==========================
.. image:: https://secure.travis-ci.org/lambdalisue/app_version.png?branch=master
    :target: http://travis-ci.org/lambdalisue/app_version
    :alt: Build status

.. image:: https://coveralls.io/repos/lambdalisue/app_version/badge.png?branch=master
    :target: https://coveralls.io/r/lambdalisue/app_version/
    :alt: Coverage

.. image:: https://pypip.in/d/app_version/badge.png
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Downloads

.. image:: https://pypip.in/v/app_version/badge.png
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Latest version

.. image:: https://pypip.in/wheel/app_version/badge.png
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Wheel Status

.. image:: https://pypip.in/egg/app_version/badge.png
    :target: https://pypi.python.org/pypi/app_version/
    :alt: Egg Status

.. image:: https://pypip.in/license/app_version/badge.png
    :target: https://pypi.python.org/pypi/app_version/
    :alt: License

Do you write the version information on ``setup.py`` and ``__init__.py``?
This tiny application allow you to access version information of ``setup.py``
from ``__init__.py``.

Based on `this post <http://stackoverflow.com/questions/17583443/what-is-the-correct-way-to-share-package-version-with-setup-py-and-the-package/17638236#17638236>`_, I write this tiny application for convinience.

Check
`online documentation <http://python-app_version.readthedocs.org/en/latest/>`_
for more details.

Installation
------------
Use pip_ like::

    $ pip install app_version

.. _pip: https://pypi.python.org/pypi/pip

Usage
-----
The following code is an example ``__init__.py``.

.. code-block:: python

    # coding: utf-8
    __all__ = ('__version__', 'VERSION')
    from app_version import get_versions
    __version__, VERSION = get_versions('your app name')
    
Then you can access the version string with ``__version__`` and version tuple
with ``VERSION``.
The version tuple is useful for comparing versions like

.. code-block:: python

    >>> VERSION = (0, 1, 2)
    >>> VERSION > (0, 1, 0)
    True
    >>> VERSION > (0, 1, 1)
    True
    >>> VERSION > (0, 1, 2)
    False