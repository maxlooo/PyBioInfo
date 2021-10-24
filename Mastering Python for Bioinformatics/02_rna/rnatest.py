#!/usr/bin/env python3

from subprocess import getstatusoutput
import os

def main() -> None:
    # PRG = './rna.py'
    test_good_input1()

"""
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
INPUT1 = './tests/inputs/input1.txt'
INPUT2 = './tests/inputs/input2.txt'
INPUT3 = './tests/inputs/input3.txt'
"""

# --------------------------------------------------
def test_good_input1() -> None:
    """ Runs on good input """
    prog = './rna.py'
    input1 = './tests/inputs/input1.txt'
    out_dir = 'out'
    """try:

        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)
    """

    retval, out = getstatusoutput(f'{prog} {input1}')
    # assert retval == 0
    print(out)

    """ assert out == 'Done, wrote 1 sequence in 2 files to directory "out".'
    assert os.path.isdir(out_dir)
    out_file = os.path.join(out_dir, 'input1.txt')
    assert os.path.isfile(out_file)
    assert open(out_file).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'
    """

"""    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)
"""

# --------------------------------------------------
if __name__ == '__main__':
    main()

