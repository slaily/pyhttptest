import pytest


def test_load_json_from_file():
    json_dict = load_json_from_file('../data/test_data.json')

    assert isinstance(json_dict, dict)
