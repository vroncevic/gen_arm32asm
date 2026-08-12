# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenARM32ASMBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_arm32asm.setup.bundle import GenARM32ASMBundle
from gen_arm32asm.setup.factory import GenARM32ASMBundleFactory


class TestGenARM32ASMBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenARM32ASMBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenARM32ASMBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_arm32asm/infrastructure/config/gen_arm32asm.cfg'}
        bundle = GenARM32ASMBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenARM32ASMBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenARM32ASMBundleFactory.create_bundle(options)
