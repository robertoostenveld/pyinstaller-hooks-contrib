# ------------------------------------------------------------------
# Copyright (c) 2023 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

"""
Pylibmagic contains data files (libmagic compiled and configurations) required to use the python-magic package.
"""

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files("pylibmagic")
