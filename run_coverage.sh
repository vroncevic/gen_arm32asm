#!/bin/bash
#
# @brief   gen_arm32asm
# @version v3.1.0
# @date    Sun Jun 30 09:25:12 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 run_coverage.py
python3 ats_coverage.py -n gen_arm32asm
echo "Done"
