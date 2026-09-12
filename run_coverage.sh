#!/bin/bash
#
# @brief   gen_arm32asm
# @version 1.0.8
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_arm32asm
pylint gen_arm32asm > gen_arm32asm.report
echo "Done"
