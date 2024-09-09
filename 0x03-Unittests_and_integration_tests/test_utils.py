import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json
from utils import access_nested_map, get_json, memoize
import unittest.mock


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({"a": 1}, ("b",)),
        ({"a": {"b": 2}}, ("a", "c")),
        ({}, ("a",)),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @unittest.mock.patch('utils.requests.get')
    def test_get_json(self, mock_get):
        mock_get.return_value.json.return_value = {"key": "value"}
        result = get_json("http://example.com")
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("http://example.com")


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def memoized_method(self):
                return self.a_method()

        test_instance = TestClass()
        with unittest.mock.patch.object(test_instance, 'a_method', wraps=test_instance.a_method) as mock_method:
            result1 = test_instance.memoized_method
            result2 = test_instance.memoized_method
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
