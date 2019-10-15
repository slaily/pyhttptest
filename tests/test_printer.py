from pyreqtest import printer


def test_slice_str_args():
    dummy_str = '''
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    when an unknown printer took a galley of type and scrambled it to make a type
    specimen book.
    '''
    sliced_dummy_str, = printer._slice_str_args(dummy_str)

    assert len(sliced_dummy_str) == 100


def test_format_data_as_tabular():
    data = (
        'Test: Extract all users',
        '200',
        '{Content-Type: application/json}',
        '{username: pyreqtest}'
    )
    tabular_data = printer._format_data_as_tabular(*data)

    assert 'HTTP Response Headers' in tabular_data


def test_process_data_for_print():
    test_kwargs = {
        'name': 'Test: process data for print',
        'status_code': '200',
        'headers': '{Content-Type: application/json}',
        'body': 'Lorem Ipsum'
    }
    data_for_print = printer.prepare_data_for_print(**test_kwargs)

    assert 'HTTP Response Status Code' in data_for_print
