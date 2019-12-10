from tabulate import tabulate

from pyhttptest.constants import (
    SLICE_TO_INDEX,
    PRINTER_HEADERS,
    PRINTER_HEADERS_DATA_KEYS
)
from pyhttptest.utils import extract_properties_values_from_json


def _slice_str_args(*args, slice_to=SLICE_TO_INDEX):
    """Given `str` arguments are sliced to the specified length.

    :param args: Arguments in `str` type.
    :param int slice_to(optional): Index to slice.

    :returns: Sliced arguments.
    :rtype: `tuple`
    """
    return tuple(
        str_value[:slice_to] for str_value in args
    )


def _format_data_as_tabular(list_data, headers=PRINTER_HEADERS):
    """Formats the data and put it into a table with headers
    on the top оf it.

    :param list|tuple|set list_data: Iterable of iterables.
    :param headers: Iterable of `str`.

    Example table output:

        ╒═════════════════════════╤═════════════╤══════════════════════════════════════════════════╤══════════════════════════════╕
        │                         │   Test name │ HTTP Response Status CodeHTTP Response Headers   │ HTTP Response Message Body   │
        ╞═════════════════════════╪═════════════╪══════════════════════════════════════════════════╪══════════════════════════════╡
        │ Test: Extract all users │         200 │ {Content-Type: application/json}                 │ {username: pyhttptest}       │
        ╘═════════════════════════╧═════════════╧══════════════════════════════════════════════════╧══════════════════════════════╛

    :returns: Data in tabular format.
    :rtype: `str`
    """
    return tabulate(
        list_data,
        headers,
        tablefmt='fancy_grid',
    )


def prepare_data_for_print(list_of_dicts):
    """Wrapper function responsible to take the data, push it
    through several processes to prepare it for print.

    :param list list_of_dicts: List of `dict` data.

    :returns: Data for print.
    :rtype: `str`
    """
    list_of_strs = []

    for _dict in list_of_dicts:
        args = extract_properties_values_from_json(
            _dict,
            PRINTER_HEADERS_DATA_KEYS
        )
        sliced_str_args = _slice_str_args(*args)
        list_of_strs.append(sliced_str_args)

    return _format_data_as_tabular(list_of_strs)
