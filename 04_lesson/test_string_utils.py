import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для функции capitalize


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("земля", "Земля"),
    ("c-3PO", "C-3PO"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# Тесты для функции trim


@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "skypro"),
    ("",""),
    ("skypro","skypro"),
    ("     ", ""),
    ("       java", "java"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("skypro", "skypro"),
    ("", ""),
    ("None", "None"),
    ("12345", "12345"),
    ("26 июня 2026", "26 июня 2026"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Тесты для функции contains


@pytest.mark.parametrize("str1, str2, result", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "P", True),
    ("SkyPro", "o", True),
    ("SkyPro", "Pro", True),
])
def test_contains_positive(str1, str2, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.parametrize("str1, str2, result", [
    ("SkyPro", "U", False),
    ("SkyPro", "z", False),
    ("", "a", False),
    ("abc", "", False),
])
def test_contains_negative(str1, str2, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(str1, str2)
    assert res == result


# Тесты для функции delete_symbol


@pytest.mark.parametrize("input_txt, symbol, expected", [
    ("SkyPro", "S", "kyPro"),
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "ro", "SkyP"),
    ("12345", "4", "1235"),
    ("SkyPro", "x", "SkyPro"),
    ("banana", "a", "bnn"),
])
def test_delete_symbol_positive(input_txt, symbol, expected):
    stringUtils = StringUtils()
    assert stringUtils.delete_symbol(input_txt, symbol, expected) == expected


@pytest.mark.parametrize("input_txt, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("SkyPro", "X", "SkyPro"),
    ("SkyPro forever", "ax", "SkyPro forever"),
    ("12345", "6", "12345"),
    ("", "x", ""),
    ("  ", "x", "  "),
    ("   ", "  ", "   "),
])
def test_delete_symbol_negative(input_txt, symbol, expected):
    stringUtils = StringUtils()
    assert stringUtils.delete_symbol(input_txt, symbol, expected) == expected
    result = StringUtils()
    assert result is None
