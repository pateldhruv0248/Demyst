import unittest
import json
from unittest.mock import mock_open, patch
from utils import read_spec

class TestReadSpec(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"field1": "value1"}')
    def test_read_spec_success(self, mock_file):
        spec_file_path = "dummy_path.json"
        expected_result = {"field1": "value1"}
        result = read_spec(spec_file_path)
        self.assertEqual(result, expected_result)
        mock_file.assert_called_once_with(spec_file_path, "r")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_spec_file_not_found(self, mock_file):
        spec_file_path = "non_existent_file.json"
        result = read_spec(spec_file_path)
        self.assertIsNone(result)
        mock_file.assert_called_once_with(spec_file_path, "r")

    @patch("builtins.open", new_callable=mock_open, read_data='not a json')
    def test_read_spec_invalid_json(self, mock_file):
        spec_file_path = "invalid_json.json"
        result = read_spec(spec_file_path)
        self.assertIsNone(result)
        mock_file.assert_called_once_with(spec_file_path, "r")

if __name__ == "__main__":
    unittest.main()