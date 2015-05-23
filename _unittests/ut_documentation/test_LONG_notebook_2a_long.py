#-*- coding: utf-8 -*-
"""
@brief      test log(time=19s)
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper

try:
    import pyensae
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
    import pyensae

try:
    import pymmails
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
    import pymmails

from pyquickhelper import fLOG, get_temp_folder
from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a, unittest_raise_exception_notebook


class TestNotebookRunner2a_long (unittest.TestCase):

    def test_notebook_runner_2a_long(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            # skip travis and R
            return

        temp = get_temp_folder(__file__, "temp_notebook2a_long_")
        keepnote = ls_notebooks("2a")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "python_r" in n,
                                fLOG=fLOG,
                                clean_function=clean_function_1a)
        unittest_raise_exception_notebook(res, fLOG)

if __name__ == "__main__":
    unittest.main()