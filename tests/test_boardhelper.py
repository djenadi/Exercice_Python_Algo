import unittest
import os
import sys

# Dev path config
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from boardhelper import BoardHelper


test_file_name = "tray_test_file"

ONE_SQUARE = "3.0x\n"\
             "..0.0...0.\n"\
             ".0........\n"\
             "..0.0...0.\n"

ONE_SQUARE_OUTPUT = "..0.0xxx0.\n"\
                    ".0...xxx..\n"\
                    "..0.0xxx0.\n"

NO_SQUARE = "2.0x\n"\
            "00\n"\
            "00\n"

NO_SQUARE_OUTPUT = "00\n"\
                   "00\n"

TWO_EQUAL_SQUARES = "3-/P\n"\
                    "--/\n"\
                    "---\n"\
                    "/--\n"

TWO_EQUAL_SQUARES_OUTPUT = "PP/\n"\
                           "PP-\n"\
                           "/--\n"

INVALID_MAP = "6-/P\n"\
              "--/\n"\
              "AZ-\n"\
              "/--\n"


class TestBoardHelper(unittest.TestCase):

    def generate_tray_file(self, content):
        tray_file = open(test_file_name, "w")
        tray_file.write(content)
        tray_file.close()

    # test basic case
    def test_fill_biggest_square_one_square_case(self):
        self.generate_tray_file(ONE_SQUARE)
        try_helper = BoardHelper(test_file_name)
        assert try_helper.fill_biggest_square() == ONE_SQUARE_OUTPUT

    # test no square found
    def test_fill_biggest_square_no_square_case(self):
        self.generate_tray_file(NO_SQUARE)
        try_helper = BoardHelper(test_file_name)
        assert try_helper.fill_biggest_square() == NO_SQUARE_OUTPUT

    # test two equal square, should return upper left one
    def test_fill_biggest_square_two_equale_squares_case(self):
        self.generate_tray_file(TWO_EQUAL_SQUARES)
        try_helper = BoardHelper(test_file_name)
        assert try_helper.fill_biggest_square() == TWO_EQUAL_SQUARES_OUTPUT

    def test_invalidMap__ase(self):
        self.generate_tray_file(INVALID_MAP)
        with self.assertRaisesRegex(Exception, 'map error'):
            try_helper = BoardHelper(test_file_name)
            try_helper.fill_biggest_square()

    def tearDown(self):
        try:
            os.remove(test_file_name)
        except Exception as err:
            print(err)
