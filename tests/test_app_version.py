#!/usr/bin/env nosetests -v
# coding=utf-8
"""
A unit test module of ``app_version``
"""
__author__ = 'Alisue <lambdalisue@hashnote.net>'
import inspect
from nose.tools import *
from app_version import get_string_version
from app_version import get_tuple_version
from app_version import get_versions


