import cProfile
import argparse
from boardhelper import BoardHelper

parser = argparse.ArgumentParser(description='Fill the biggest square in the board with the given fill char', )
parser.add_argument(
    'filesnames',
    help='Files names that should be processed',
    nargs='*')
parser.add_argument(
    '-p',
    '--run_profiler',
    help='Run profiler',
    action='store_true')


args = parser.parse_args()


def process_files():
    for file_name in args.filesnames:
        try:
            try_helper = BoardHelper(file_name)
            print(try_helper.fill_biggest_square())
        except Exception as err:
            print(f"{err}")


if args.run_profiler:
    cProfile.run('process_files()')
else:
    process_files()
