# -*- coding: UTF-8 -*-

'''
Module
    test_engine.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_arm32asm is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_arm32asm is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Unit tests for main engine (GenARM32ASM) and GenARM32ASMBundle.
'''

import unittest
from unittest.mock import MagicMock, patch
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.option.ioption_parser import IOptionManager
from gen_arm32asm.engine import GenARM32ASM
from gen_arm32asm.gen_arm32asm_bundle import GenARM32ASMBundle
from gen_arm32asm.domain.ports.isubprocessor import ISubProcessor
from gen_arm32asm.domain.ports.iservice import IService
from gen_arm32asm.infrastructure.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_arm32asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_arm32asm/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Development'


class TestEngine(unittest.TestCase):
    '''
        Defines engine and bundle unit tests.
    '''

    def test_default_init(self) -> None:
        '''
            Tests default constructor initialization of gen_arm32asm.
        '''
        engine: GenARM32ASM = GenARM32ASM()
        self.assertTrue(engine.is_initialized())
        self.assertIsNotNone(engine._cli)

    @patch.object(GenARM32ASM, "_info_file", "invalid/path/gen_arm32asm.cfg")
    def test_init_not_initialized(self) -> None:
        '''
            Tests initialization fails when config is invalid.
        '''
        engine: GenARM32ASM = GenARM32ASM()
        self.assertFalse(engine.is_initialized())

    @patch('gen_arm32asm.engine.CLI', side_effect=Exception("Unexpected error"))
    def test_init_unexpected_exception(self, mock_cli: MagicMock) -> None:
        '''
            Tests initialization catches unexpected exception.
        '''
        engine: GenARM32ASM = GenARM32ASM()
        self.assertFalse(engine.is_initialized())

    def test_init_component_not_initialized(self) -> None:
        '''
            Tests engine is not initialized if one component is uninitialized.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = False
        
        bundle: GenARM32ASMBundle = GenARM32ASMBundle(cli=mock_cli)
        engine: GenARM32ASM = GenARM32ASM(bundle)
        self.assertFalse(engine.is_initialized())

    def test_process_unexpected_exception(self) -> None:
        '''
            Tests engine process catches unexpected exception.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = Exception("Unexpected error")

        bundle: GenARM32ASMBundle = GenARM32ASMBundle(cli=mock_cli)
        engine: GenARM32ASM = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_expected_exception(self) -> None:
        '''
            Tests engine process catches expected exception.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = ATSValueError("Expected error")

        bundle: GenARM32ASMBundle = GenARM32ASMBundle(cli=mock_cli)
        engine: GenARM32ASM = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_bundle_validation_failures(self) -> None:
        '''
            Tests GenARM32ASMBundle validate raises error when fields are None.
        '''
        # subprocessor is None
        bundle1: GenARM32ASMBundle = GenARM32ASMBundle(subprocessor=None)
        with self.assertRaises(ATSValueError) as ctx:
            bundle1.validate()
        self.assertEqual(str(ctx.exception), 'subprocessor must be provided.')

        # service is None
        bundle2: GenARM32ASMBundle = GenARM32ASMBundle(
            subprocessor=MagicMock(spec=ISubProcessor),
            service=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle2.validate()
        self.assertEqual(str(ctx.exception), 'service must be provided.')

        # parser is None
        bundle3: GenARM32ASMBundle = GenARM32ASMBundle(
            subprocessor=MagicMock(spec=ISubProcessor),
            service=MagicMock(spec=IService),
            parser=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle3.validate()
        self.assertEqual(str(ctx.exception), 'parser must be provided.')

        # cli is None
        bundle4: GenARM32ASMBundle = GenARM32ASMBundle(
            subprocessor=MagicMock(spec=ISubProcessor),
            service=MagicMock(spec=IService),
            parser=MagicMock(spec=IOptionManager),
            cli=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle4.validate()
        self.assertEqual(str(ctx.exception), 'cli must be provided.')

        # Valid bundle does not raise error
        bundle_valid: GenARM32ASMBundle = GenARM32ASMBundle(
            subprocessor=MagicMock(spec=ISubProcessor),
            service=MagicMock(spec=IService),
            parser=MagicMock(spec=IOptionManager),
            cli=MagicMock(spec=ICLI)
        )
        bundle_valid.validate()

    def test_bundle_merge_and_to_dict(self) -> None:
        '''
            Tests GenARM32ASMBundle merge and to_dict methods.
        '''
        sub1: MagicMock = MagicMock(spec=ISubProcessor)
        srv2: MagicMock = MagicMock(spec=IService)

        bundle1: GenARM32ASMBundle = GenARM32ASMBundle(subprocessor=sub1)
        bundle2: GenARM32ASMBundle = GenARM32ASMBundle(service=srv2)

        bundle1.merge(bundle2)
        self.assertEqual(bundle1.subprocessor, sub1)
        self.assertEqual(bundle1.service, srv2)

        d: dict = bundle1.to_dict()
        self.assertEqual(d["subprocessor"], sub1)
        self.assertEqual(d["service"], srv2)

    def test_process_success(self) -> None:
        '''
            Tests successful command processing with output details.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 0, "stdout": "Success"}

        bundle: GenARM32ASMBundle = GenARM32ASMBundle(cli=mock_cli)
        engine: GenARM32ASM = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_success_default_stdout(self) -> None:
        '''
            Tests successful command processing with empty stdout.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 0, "stdout": None}

        bundle: GenARM32ASMBundle = GenARM32ASMBundle(cli=mock_cli)
        engine: GenARM32ASM = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_failure_code(self) -> None:
        '''
            Tests failed command processing handling.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.return_value = {"returncode": 1, "stderr": "Failed"}

        bundle: GenARM32ASMBundle = GenARM32ASMBundle(cli=mock_cli)
        engine: GenARM32ASM = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())

        engine.process()
        mock_cli.run.assert_called_once()

    @patch.object(GenARM32ASM, "_info_file", "invalid/path/gen_arm32asm.cfg")
    def test_process_not_initialized(self) -> None:
        '''
            Tests processing fails immediately if engine is uninitialized.
        '''
        engine: GenARM32ASM = GenARM32ASM()
        self.assertFalse(engine.is_initialized())
        
        engine.process()

    def test_str_repr(self) -> None:
        '''
            Tests engine string representation.
        '''
        engine: GenARM32ASM = GenARM32ASM()
        engine_str: str = str(engine)
        self.assertIsNotNone(engine_str)
        self.assertIsInstance(engine_str, str)
        self.assertNotEqual(engine_str, "")
