import pytest

from pyreqtest import core


def test_load_json_from_file():
    json_dict = core.load_json_from_file('data/test_data.json')

    assert isinstance(json_dict, dict)
