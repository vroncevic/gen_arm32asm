# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the gen_arm32asm bundle.
'''

from __future__ import annotations

from os.path import abspath, dirname, join

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_arm32asm.setup.bundle import GenARM32ASMBundle
from gen_arm32asm.setup.options import GenARM32ASMBundleOptions
from gen_arm32asm.setup.registry import GenARM32ASMBundleRegistry
from gen_arm32asm.setup.dependencies import GenARM32ASMBundleDependencies
from gen_arm32asm.setup.opt_validator import GenARM32ASMBundleOptionsValidator
from gen_arm32asm.setup.keys import GenARM32ASMBundleKeys
from gen_arm32asm.core.service.engine import Service
from gen_arm32asm.infrastructure.subprocessor import SubProcessor
from gen_arm32asm.infrastructure.cli.engine import CLI
from gen_arm32asm.infrastructure.cli.setup.bundle import CLIBundle
from gen_arm32asm.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_arm32asm.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_arm32asm.infrastructure.command.command import CommandBundle
from gen_arm32asm.infrastructure.command.gen_pro_command_definition import GenProCommandDefinition
from gen_arm32asm.infrastructure.command.gen_pro_command_executor import GenProCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_arm32asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_arm32asm/blob/dev/LICENSE'
__version__ = '1.0.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenARM32ASMBundleFactory:
    '''
        Factory for creating the gen_arm32asm bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_arm32asm info file.
            :methods:
                | create_bundle - Creates the gen_arm32asm bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    _info_file: str = join(
        dirname(dirname(abspath(__file__))), 'infrastructure', 'config', 'gen_arm32asm.cfg'
    )

    @classmethod
    def create_bundle(cls, options: GenARM32ASMBundleOptions | None = None) -> GenARM32ASMBundle:
        '''
            Creates the gen_arm32asm bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_arm32asm bundle.
            :return: The gen_arm32asm bundle.
            :exceptions:
                | ATSValueError: The gen_arm32asm bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_arm32asm bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_arm32asm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_arm32asm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_arm32asm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_arm32asm bundle must be an instance of GenARM32ASMBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenARM32ASMBundleOptionsValidator.validate(options)

        info_file = options.get(GenARM32ASMBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_pro_definition: GenProCommandDefinition = GenProCommandDefinition()

        gen_pro_bundle: CommandBundle = CommandBundle(
            definition=gen_pro_definition,
            executor=GenProCommandExecutor(gen_pro_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_pro_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenARM32ASMBundleRegistry.create_bundle(
            dependencies=GenARM32ASMBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
