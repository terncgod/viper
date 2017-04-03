# -*- coding: utf-8 -*-
# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

from viper.core.ui import console
try:
    from unittest import mock
except ImportError:
    # Python2
    import mock
import sys


class TestCommands:

    def test_init(self):
        instance = console.Console()
        assert isinstance(instance, console.Console)

    def test_start(self):
        instance = console.Console()
        if sys.version_info <= (3, 0):
            in_fct = 'viper.core.ui.console.input'
        else:
            in_fct = 'builtins.input'
        with mock.patch(in_fct, return_value='exit'):
            instance.start()
