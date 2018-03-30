# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class PyapogeeError(Exception):
    """A custom core Pyapogee exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(PyapogeeError, self).__init__(message)


class PyapogeeNotImplemented(PyapogeeError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(PyapogeeNotImplemented, self).__init__(message)


class PyapogeeApiError(PyapogeeError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Pyapogee API'
        else:
            message = 'Http response error from Pyapogee API. {0}'.format(message)

        super(PyapogeeAPIError, self).__init__(message)


class PyapogeeApiAuthError(PyapogeeAPIError):
    """A custom exception for API authentication errors"""
    pass


class PyapogeeMissingDependency(PyapogeeError):
    """A custom exception for missing dependencies."""
    pass


class PyapogeeWarning(Warning):
    """Base warning for Pyapogee."""
    pass


class PyapogeeUserWarning(UserWarning, PyapogeeWarning):
    """The primary warning class."""
    pass


class PyapogeeSkippedTestWarning(PyapogeeUserWarning):
    """A warning for when a test is skipped."""
    pass


class PyapogeeDeprecationWarning(PyapogeeUserWarning):
    """A warning for deprecated features."""
    pass

