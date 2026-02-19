# Copyright 2009-2015 MongoDB, Inc.
# Copyright (c) 2025, James Westover. All rights reserved. (Python 3.12+ modernization)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you
# may not use this file except in compliance with the License.  You
# may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.  See the License for the specific language governing
# permissions and limitations under the License.

"""Utility functions and definitions for Python 3.12+ compatibility.

This module was originally a Python 2/3 compatibility layer. It has been
modernized to support only Python 3.12+.
"""

import codecs
import _thread as thread
import sys
from io import BytesIO as StringIO

MAXSIZE = sys.maxsize

imap = map


def b(s):
    """Convert string to bytes using latin-1 encoding.

    BSON and socket operations deal in binary data. In Python 3 that means
    instances of `bytes`.
    """
    return codecs.latin_1_encode(s)[0]


def bytes_from_hex(h):
    """Convert hex string to bytes."""
    return bytes.fromhex(h)


def iteritems(d):
    """Return iterator over dict items."""
    return iter(d.items())


def itervalues(d):
    """Return iterator over dict values."""
    return iter(d.values())


def reraise(exctype, value, trace=None):
    """Re-raise an exception with a new traceback."""
    raise exctype(str(value)).with_traceback(trace)


def _unicode(s):
    """Return string as-is (no-op in Python 3)."""
    return s


text_type = str
string_type = str
integer_types = int
