# This file is part of utils.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (http://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
# See the LICENSE file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

try:
    # For now, ensure that backtrace has been imported if somebody
    # is relying on it from a lsst.utils import. Treat it as an optional
    # import.
    import lsst.cpputils.backtrace
except ImportError:
    pass

from .._forwarded import isEnabled
