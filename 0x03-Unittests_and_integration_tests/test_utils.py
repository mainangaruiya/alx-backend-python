!/usr/bin/env python3
"""A module for testing the utils module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import the access_nested_map function from your utils module

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
    	self.assertEqual(access_nested_map(nested_map, path), expected_result)

if __name__ == '__main__':
    unittest.main()