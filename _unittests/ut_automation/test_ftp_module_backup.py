#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
import warnings

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip______
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip______

try:
    import pyensae as skip_____
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip_____

try:
    import pymmails as skip___
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymmails",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymmails as skip___

try:
    import pyrsslocal as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyrsslocal",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyrsslocal as skip__

try:
    import pymyinstall as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymyinstall as skip_


from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.automation import ftp_list_modules


class TestFtpBackup(unittest.TestCase):

    def test_ftp_backup(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "CS_FTPLOGIN" in os.environ:
            mod = ftp_list_modules()
            fLOG(mod)
            assert len(mod) > 0
        else:
            for k, v in sorted(os.environ.items()):
                fLOG(k, v)
            warnings.warn(
                "You need to setup CS_FTPSITE, CS_FTPLOGIN, CS_FTPPASSWORD")


if __name__ == "__main__":
    unittest.main()
