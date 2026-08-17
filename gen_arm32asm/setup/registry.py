# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_arm32asm components for simplification of gen_arm32asm bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_arm32asm.core.service.iservice import IService
from gen_arm32asm.core.service.isubprocessor import ISubProcessor
from gen_arm32asm.infrastructure.cli.icli import ICLI
from gen_arm32asm.setup.bundle import GenARM32ASMBundle
from gen_arm32asm.setup.validator import GenARM32ASMBundleValidator
from gen_arm32asm.setup.keys import GenARM32ASMBundleKeys
from gen_arm32asm.setup.dependencies import GenARM32ASMBundleDependencies
from gen_arm32asm.setup.dep_validator import GenARM32ASMBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_arm32asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_arm32asm/blob/dev/LICENSE'
__version__ = '1.0.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenARM32ASMBundleRegistry:
    '''
        Encapsulates core gen_arm32asm components for simplification of gen_arm32asm bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_arm32asm bundle.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenARM32ASMBundleDependencies) -> GenARM32ASMBundle:
        '''
            Creates the gen_arm32asm bundle.

            :param dependencies: The gen_arm32asm bundle dependencies.
            :return: The gen_arm32asm bundle.
            :exceptions:
                | ATSValueError: The gen_arm32asm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_arm32asm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_arm32asm bundle must be provided and have proper values.
                | ATSTypeError:  The gen_arm32asm bundle must be an instance of GenARM32ASMBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenARM32ASMBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenARM32ASMBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenARM32ASMBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenARM32ASMBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenARM32ASMBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenARM32ASMBundle = GenARM32ASMBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenARM32ASMBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: The registry version.
            :exceptions: None.
        '''
        return __version__
