import pytest
from examples.common_api import gram_to_kilogram, kilogram_to_gram
from examples.ui_class import show_ui


def test_gram_to_kilogram():
    assert gram_to_kilogram(1000) == 1


def test_kilogram_to_gram():
    assert kilogram_to_gram(1) == 1000


def test_ui_class():
    assert show_ui(10000) is True


def test_gram_to_kilogram_dict_type():
    with pytest.raises(TypeError):
        gram_to_kilogram({"a": 1, "b": 2})


def test_gram_to_kilogram_list_type():
    with pytest.raises(TypeError):
        gram_to_kilogram([1, 2, 3])
