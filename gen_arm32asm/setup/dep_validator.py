# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for the gen_arm32asm bundle dependencies.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.validation.check_type import istype
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.validation.check_value import not_none

from gen_arm32asm.setup.dependencies import GenARM32ASMBundleDependencies
from gen_arm32asm.setup.keys import GenARM32ASMBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_arm32asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_arm32asm/blob/dev/LICENSE'
__version__ = '1.0.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenARM32ASMBundleDependenciesValidator:
    '''
        Validator for the gen_arm32asm bundle dependencies.

        It defines:

            :methods:
                | validate - Validates the gen_arm32asm bundle dependencies.
                | is_valid - Checks if the gen_arm32asm bundle dependencies is valid.
    '''

    @classmethod
    def validate(cls, dependencies: GenARM32ASMBundleDependencies) -> None:
        '''
            Validates the gen_arm32asm bundle dependencies.

            :param dependencies: The gen_arm32asm bundle dependencies to be validated.
            :exceptions:
                | ATSValueError: The gen_arm32asm bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_arm32asm bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'gen_arm32asm_bundle_dependencies_validator::validate(...)'
        msg_dependencies_none: str = 'the gen_arm32asm bundle dependencies must be provided'
        msg_dependencies_istype: str = 'the gen_arm32asm bundle dependencies must be a Mapping'

        not_none(dependencies, ctx, msg_dependencies_none)
        istype(dependencies, Mapping, ctx, msg_dependencies_istype)

        for attr_name, expected_type in GenARM32ASMBundleKeys.get_dependency_to_type().items():
            msg_attr_name_none: str = f'the {attr_name.replace("_", " ")} must be provided'
            msg_attr_name_istype: str = f'the {attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'

            attribute = dependencies.get(attr_name)

            not_none(attribute, ctx, msg_attr_name_none)
            istype(attribute, expected_type, ctx, msg_attr_name_istype)

    @classmethod
    def is_valid(cls, genarm32asmbundledependencies: GenARM32ASMBundleDependencies) -> bool:
        '''
            Checks if the genarm32asmbundledependencies is valid.

            :param genarm32asmbundledependencies: The genarm32asmbundledependencies to be checked.
            :return: True if valid, False otherwise.
        '''
        try:
            cls.validate(genarm32asmbundledependencies)
            return True

        except (ATSValueError, ATSTypeError):
            return False
