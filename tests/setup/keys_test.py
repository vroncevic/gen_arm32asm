# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenARM32ASMBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_arm32asm.setup.keys import GenARM32ASMBundleKeys


class TestGenARM32ASMBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenARM32ASMBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenARM32ASMBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenARM32ASMBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenARM32ASMBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenARM32ASMBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenARM32ASMBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenARM32ASMBundleKeys.OPTION_INFO_FILE, opts)
