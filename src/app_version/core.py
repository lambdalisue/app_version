# coding=utf-8
"""
app_version

Get version information from ``setup.py`` via ``pkg_resources``.

The concept is taken from this answer

http://stackoverflow.com/a/17638236

written by Martijn Pietersp
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
__all__ = ('get_string_version', 'get_tuple_version', 'get_versions')
import os
import inspect
from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound


DEFAULT_STRING_NOT_FOUND = 'Please install this application with setup.py'
DEFAULT_TUPLE_NOT_FOUND = (0, 0, 0)


def get_string_version(name, default=DEFAULT_STRING_NOT_FOUND,
                       allow_ambiguous=False):
    """
    Get string version from installed package information.
    
    It will return :attr:`default` value when the named package is not
    installed.

    Parameters
    -----------
    name : string
        An application name used to install via setuptools.
    default : string
        A default returning value used when the named application is not
        installed yet
    allow_ambiguous : boolean
        ``True`` for allowing ambiguous version information.

    Returns
    --------
    string
        A version string or not found message (:attr:`default`)

    Examples
    --------
    >>> get_string_version('app_version', allow_ambiguous=True)
    '0.1.0'
    >>> get_string_version('distribution_which_is_not_installed')
    'Please install this application with setup.py'
    """
    # get filename of callar
    callar = inspect.getouterframes(inspect.currentframe())[1][1]
    if callar.startswith('<doctest'):
        # called from doctest, find written script file
        callar = inspect.getouterframes(inspect.currentframe())[-1][1]
    # get version info from distribution
    try: 
        di = get_distribution(name)
        installed_directory = os.path.join(di.location, name)
        if not callar.startswith(installed_directory) and not allow_ambiguous:
            # not installed, but there is another version that *is*
            raise DistributionNotFound
    except DistributionNotFound:
        return default
    else:
        return di.version


def get_tuple_version(name, default=DEFAULT_TUPLE_NOT_FOUND,
                      allow_ambiguous=False):
    """
    Get tuple version from installed package information for easy handling.
    
    It will return :attr:`default` value when the named package is not
    installed.

    Parameters
    -----------
    name : string
        An application name used to install via setuptools.
    default : tuple
        A default returning value used when the named application is not
        installed yet
    allow_ambiguous : boolean
        ``True`` for allowing ambiguous version information.

    Returns
    --------
    string
        A version tuple

    Examples
    --------
    >>> get_tuple_version('app_version', allow_ambiguous=True)
    (0, 1, 0)
    >>> get_tuple_version('distribution_which_is_not_installed')
    (0, 0, 0)
    """
    from tolerance.decorators import tolerate
    version = get_string_version(name, default=default,
                                 allow_ambiguous=allow_ambiguous)
    # convert string version to tuple version
    # prefer integer for easy handling
    if isinstance(version, tuple):
        # not found
        return version
    return tuple(map(tolerate(lambda x: x)(int), version.split('.')))


def get_versions(name,
                 default_string=DEFAULT_STRING_NOT_FOUND,
                 default_tuple=DEFAULT_TUPLE_NOT_FOUND,
                 allow_ambiguous=False):
    """
    Get string and tuple versions from installed package information
    
    It will return :attr:`default_string` and :attr:`default_tuple` values when
    the named package is not installed.

    Parameters
    -----------
    name : string
        An application name used to install via setuptools.
    default : string
        A default returning value used when the named application is not
        installed yet
    default_tuple : tuple
        A default returning value used when the named application is not
        installed yet
    allow_ambiguous : boolean
        ``True`` for allowing ambiguous version information.

    Returns
    --------
    tuple
        A version string and version tuple

    Examples
    --------
    >>> __version__, VERSION = get_versions('app_version', allow_ambiguous=True)
    >>> __version__
    '0.1.0'
    >>> VERSION
    (0, 1, 0)
    >>> __version__, VERSION = get_versions('distribution_which_is_not_installed')
    >>> __version__
    'Please install this application with setup.py'
    >>> VERSION
    (0, 0, 0)
    """
    version_string = get_string_version(name, default_string, allow_ambiguous)
    version_tuple = get_tuple_version(name, default_tuple, allow_ambiguous)
    return version_string, version_tuple


if __name__ == '__main__':
    import doctest; doctest.testmod()
