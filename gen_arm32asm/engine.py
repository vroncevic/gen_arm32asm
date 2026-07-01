# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Main engine orchestrator class for Task Code Generator CLI.
'''

from typing import Any, override
from os.path import dirname, realpath
from ats_utilities.base.engine import Base
from ats_utilities.base.component_bundle import BaseComponentBundle
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_arm32asm.gen_arm32asm_bundle import GenARM32ASMBundle
from gen_arm32asm.domain.ports.iservice import IService
from gen_arm32asm.application.service import Service
from gen_arm32asm.domain.ports.isubprocessor import ISubProcessor
from gen_arm32asm.infrastructure.subprocessor import SubProcessor
from gen_arm32asm.infrastructure.icli_command import ICLICommand
from gen_arm32asm.infrastructure.cli_bundle import CLIBundle
from gen_arm32asm.infrastructure.gen_pro_command import GenProCommand
from gen_arm32asm.infrastructure.icli import ICLI
from gen_arm32asm.infrastructure.cli import CLI

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_arm32asm'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_arm32asm/blob/dev/LICENSE'
__version__: str = '1.0.5'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class GenARM32ASM(Base):
    '''
        Engine orchestrating the initialization and execution of gen_arm32asm.

        It defines:

            :attributes:
                | _info_file - Path to the info file.
                | _cli - Adapter for command line user interface.
            :methods:
                | __init__ - Initializes the GenARM32ASM engine with adapters and services.
                | run - Starts the gen_arm32asm.
    '''

    _info_file: str = 'infrastructure/config/gen_arm32asm.cfg'

    def __init__(self, component_bundle: GenARM32ASMBundle | None = None) -> None:
        '''
            Initializes the GenARM32ASM engine with adapters and services.

            :param component_bundle: GenARM32ASM bundle containing adapters and services | None.
            :type component_bundle: <GenARM32ASMBundle | None>
            :exceptions: None.
        '''
        current_dir: str = dirname(realpath(__file__))
        super().__init__(BaseComponentBundle(info_file=f'{current_dir}/{self._info_file}', use_generator=True))

        try:
            if not self._is_initialized:
                raise ATSValueError(f'failed to initialize engine with {current_dir}/{self._info_file}')

            # Mark as not initialized (waiting for other components to be initialized)
            self._is_initialized = False

            # Use provided component bundle or use default adapters
            bundle: GenARM32ASMBundle = component_bundle or GenARM32ASMBundle()

            # Initialization of primary adapter (Generator)
            # Generator for generating project structure
            # Force default implementation of generator if not provided by bundle
            generator: IGenerator = bundle.generator or self._generator

            # Initialization of option manager adapter (Adapter for options parsing)
            parser: IOptionManager = bundle.parser or self._options_parser

            # Initialization of secondary adapter (Service)
            # Sub processor for execution of other tools/commands
            # Force default implementation of sub processor if not provided by bundle
            subprocessor: ISubProcessor = bundle.subprocessor or SubProcessor(generator=generator)

            # Injecting adapter into the application service (Orchestration)
            # Force default implementation of service if not provided by bundle
            service: IService = bundle.service or Service(subprocessor=subprocessor)

            # Setting up CLI command strategies (Command strategies for CLI)
            commands: list[ICLICommand] = [GenProCommand()]

            # Setting up primary adapter (CLI interface)
            cli_bundle: CLIBundle = CLIBundle(service=service, parser=parser, commands=commands)
            self._cli: ICLI = bundle.cli or CLI(cli_bundle)

            # Mark as initialized (all components initialized)
            self._is_initialized = all([
                component.is_initialized() for component in [
                    generator, parser, subprocessor, service, self._cli
                ] if component
            ])
            self._reporter.success(["✅ gen_arm32asm: engine initialized successfully."])

        except (ATSValueError, ValueError) as exc:
            self._reporter.error([f'❌ gen_arm32asm: {exc}'])
        except Exception as exc:
            self._reporter.error([f'❌ gen_arm32asm unexpected exception: {exc}'])

    @override
    def process(self) -> None:
        '''
            Starts the CLI adapter to run the tool command.

            :exceptions: None.
        '''
        result: dict[str, Any] = {}

        try:
            if self.is_initialized():
                self._reporter.success(["🔥 Starting execution command..."])
                result = self._cli.run()
                self._reporter.success(["✅ Execution finished!"])

                if result.get("returncode") != 0:
                    self._reporter.error([f'❌ gen_arm32asm: {result.get("stderr")}'])
                    self._reporter.error([f'❌ gen_arm32asm: exiting with error.'])
                else:
                    self._reporter.success([f'✅ gen_arm32asm: {result.get("stdout") or 'done!'}'])
                    self._reporter.success([f'✅ gen_arm32asm: exiting successfully.'])
            else:
                self._reporter.error([f'❌ gen_arm32asm: engine not initialized.'])
                
        except (ATSValueError, ValueError) as exc:
            self._reporter.error([f'❌ gen_arm32asm: {exc}'])
        except Exception as exc:
            self._reporter.error([f'❌ gen_arm32asm unexpected exception: {exc}'])
