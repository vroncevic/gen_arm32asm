# -*- coding: UTF-8 -*-

'''
Module
    main.py
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
    Main entry point for Task Code Generator CLI.
'''

from __future__ import annotations

from sys import exit as sys_exit

from gen_arm32asm.engine import GenARM32ASM
from gen_arm32asm.setup.factory import GenARM32ASMBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_arm32asm'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_arm32asm/blob/dev/LICENSE'
__version__ = '1.0.8'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Bootstraps and runs the gen_arm32asm with required adapters.

        :return: True if successful, False otherwise.
        :exceptions: None
    '''
    gen_arm32asm: GenARM32ASM = GenARM32ASM(GenARM32ASMBundleFactory.create_bundle())

    return gen_arm32asm.process()


if __name__ == '__main__':
    '''
        Entry point for gen_arm32asm execution.

        :exit code: 0 if successful, 1 otherwise.
        :exceptions: None
    '''
    sys_exit(0 if main() else 1)
