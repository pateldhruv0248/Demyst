import unittest
from fixed_width_parser.src.parser import parse_fixed_width_line
from fixed_width_parser.src.utils import read_spec

class TestFixedWidthParser(unittest.TestCase):

    spec_file = "./fixed_width_parser/tests/test_data/spec.json"

    field_spec = read_spec(spec_file)

    def setUp(self):
        self.parser = parse_fixed_width_line

    def test_parse_line_with_special_characters(self):
        line = "456  WXYZ987654  23 251029384756   J@L    890       12345rq$ 52  345                 ABC12345678  "
        expected_output = [
            '456',
            'WXYZ987654',
            '23',
            '25',
            '1029384756',
            'J@L',
            '890',
            '12345rq$ 52',
            '345',
            'ABC12345678'
            ]
        self.assertEqual(self.parser(line, self.field_spec), expected_output)

    def test_parse_line_with_negative_numbers(self):
        line = "9086 IJKL112233  6  -61112233445   -NO    11156     45678        45678   90123       DEF987        "
        expected_output = [
            '9086',
            'IJKL112233',
            '6',
            '-6',
            '1112233445',
            '-NO',
            '11156',
            '45678',
            '45678   90123',
            'DEF987'
            ]
        self.assertEqual(self.parser(line, self.field_spec), expected_output)

    def test_parse_line_with_utf8_characters(self):
        line = "1234 你好世界  5678 こんにちは世界  9012 안녕하세요  3456"
        expected_output = [
            '1234',
            '你好世界  5678 こ',
            'んにち',
            'は世',
            '界  9012 안녕하세요',
            '3456',
            '',
            '',
            '',
            ''
            ]
        self.assertEqual(self.parser(line, self.field_spec), expected_output)

    def test_parse_line_with_only_white_spaces(self):
        line = "    " * 10
        expected_output = ['','','','','','','','','','']
        self.assertEqual(self.parser(line, self.field_spec), expected_output)
    
    def test_parse_line_with_empty_input(self):
        line = ""
        expected_output = ['','','','','','','','','','']
        self.assertEqual(self.parser(line, self.field_spec), expected_output)
        

if __name__ == '__main__':
    unittest.main()