# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenARM32ASMBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_arm32asm.setup.opt_validator import GenARM32ASMBundleOptionsValidator


class TestGenARM32ASMBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenARM32ASMBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenARM32ASMBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenARM32ASMBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenARM32ASMBundleOptionsValidator.validate(options)
