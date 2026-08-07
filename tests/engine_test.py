# -*- coding: UTF-8 -*-

'''
Module
    test_engine.py
Info
    Unit tests for GenARM32ASM engine.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.factory import ContextBundleFactory
from ats_utilities.exceptions import ATSValueError

from gen_arm32asm.engine import GenARM32ASM
from gen_arm32asm.setup.bundle import GenARM32ASMBundle
from gen_arm32asm.setup.factory import GenARM32ASMBundleFactory
from gen_arm32asm.core.service.iservice import IService
from gen_arm32asm.core.service.isubprocessor import ISubProcessor
from gen_arm32asm.infrastructure.cli.icli import ICLI


class DummyService(IService):
    def execute(self, *, params: object) -> object:
        return None
    def is_initialized(self) -> bool:
        return True
    def __str__(self) -> str:
        return 'DummyService'


class DummySubProcessor(ISubProcessor):
    def run(self, *, params: object) -> dict[str, object]:
        return {}
    def is_initialized(self) -> bool:
        return True
    def __str__(self) -> str:
        return 'DummySubProcessor'


class DummyCLI(ICLI):
    def __init__(self, return_code: int = 0, stderr: str = '') -> None:
        self.return_code = return_code
        self.stderr = stderr

    def run(self) -> dict[str, object]:
        return {'returncode': self.return_code, 'stderr': self.stderr}

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return 'DummyCLI'


class TestGenARM32ASM(unittest.TestCase):
    def test_engine_init_success(self) -> None:
        bundle = GenARM32ASMBundleFactory.create_bundle()
        engine = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())

    def test_engine_init_fail_validation(self) -> None:
        engine = GenARM32ASM(None)
        self.assertFalse(engine.is_initialized())

    def test_engine_process_success(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_arm32asm/infrastructure/config/gen_arm32asm.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI(return_code=0)

        bundle = GenARM32ASMBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertTrue(engine.process())

    def test_engine_process_cli_failure(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_arm32asm/infrastructure/config/gen_arm32asm.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI(return_code=1, stderr='CLI error')

        bundle = GenARM32ASMBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_not_initialized(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_arm32asm/infrastructure/config/gen_arm32asm.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        # Force base option_manager initialization to return False
        mock_base.option_manager.is_initialized = Mock(return_value=False)

        bundle = GenARM32ASMBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenARM32ASM(bundle)
        self.assertFalse(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_exception(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_arm32asm/infrastructure/config/gen_arm32asm.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        
        dummy_cli = DummyCLI()
        dummy_cli.run = Mock(side_effect=Exception('Unexpected error'))

        bundle = GenARM32ASMBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    def test_engine_process_validation_exception(self) -> None:
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_arm32asm/infrastructure/config/gen_arm32asm.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()
        dummy_cli.run = Mock(side_effect=ATSValueError('Validation error in run'))

        bundle = GenARM32ASMBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenARM32ASM(bundle)
        self.assertTrue(engine.is_initialized())
        self.assertFalse(engine.process())

    @patch('gen_arm32asm.setup.validator.GenARM32ASMBundleValidator.validate')
    def test_engine_init_generic_exception(self, mock_validate: Mock) -> None:
        mock_validate.side_effect = Exception('Unexpected generic validation error')
        
        context_bundle = ContextBundleFactory.create_bundle()
        mock_base = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file='gen_arm32asm/infrastructure/config/gen_arm32asm.cfg',
                use_generator=True,
                context_bundle=context_bundle
            )
        )
        
        dummy_service = DummyService()
        dummy_subprocessor = DummySubProcessor()
        dummy_cli = DummyCLI()

        bundle = GenARM32ASMBundle(
            base=mock_base,
            service=dummy_service,
            subprocessor=dummy_subprocessor,
            cli=dummy_cli
        )

        engine = GenARM32ASM(bundle)
        self.assertFalse(engine.is_initialized())
