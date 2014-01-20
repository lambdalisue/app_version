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

DEFAULT_STRING_NOT_FOUND = 'Please install this application with setup.py'
DEFAULT_TUPLE_NOT_FOUND = (0, 0, 0)

def get_string_version(name, default=DEFAULT_STRING_NOT_FOUND):
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

    Returns
    --------
    string
        A version string or not found message (:attr:`default`)

    Examples
    --------
    >>> expected_version_string = '0.1.0'
    >>> get_string_version('app_version') == expected_version_string
    True
    >>> get_string_version('distribution_which_is_not_installed')
    'Please install this application with setup.py'
    """
    import os
    from pkg_resources import get_distribution
    from pkg_resources import DistributionNotFound
    # Reference: 
    #   http://stackoverflow.com/a/17638236
    # get version information from setup.py
    try: 
        _dist = get_distribution(name)
        if not __file__.startswith(os.path.join(_dist.location, name)):
            # not installed, but there is another version that *is*
            raise DistributionNotFound
    except DistributionNotFound:
        return default
    else:
        return _dist.version


def get_tuple_version(name, default=DEFAULT_TUPLE_NOT_FOUND):
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

    Returns
    --------
    string
        A version tuple

    Examples
    --------
    >>> expected_version_tuple = (0, 1, 0)
    >>> get_tuple_version('app_version') == expected_version_tuple
    True
    >>> get_tuple_version('distribution_which_is_not_installed')
    (0, 0, 0)
    """
    from tolerance.decorators import tolerate
    version = get_string_version(name, default=default)
    # convert string version to tuple version
    # prefer integer for easy handling
    if isinstance(version, tuple):
        # not found
        return version
    return tuple(map(tolerate(lambda x: x)(int), version.split('.')))


def get_versions(name,
                 default_string=DEFAULT_STRING_NOT_FOUND,
                 default_tuple=DEFAULT_TUPLE_NOT_FOUND):
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

    Returns
    --------
    tuple
        A version string and version tuple

    Examples
    --------
    >>> expected_version_string = '0.1.0'
    >>> expected_version_tuple = (0, 1, 0)
    >>> __version__, VERSION = get_versions('app_version')
    >>> __version__ == expected_version_string
    True
    >>> VERSION == expected_version_tuple
    True
    >>> __version__, VERSION = get_versions('distribution_which_is_not_installed')
    >>> __version__
    'Please install this application with setup.py'
    >>> VERSION
    (0, 0, 0)
    """
    version_string = get_string_version(name, default_string)
    version_tuple = get_tuple_version(name, default_tuple)
    return version_string, version_tuple


if __name__ == '__main__':
    import doctest; doctest.testmod()
