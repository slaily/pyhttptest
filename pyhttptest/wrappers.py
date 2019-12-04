from pyhttptest import core
from pyhttptest.printer import prepare_data_for_print


def execute_single_test_scenario(json_data):
    """Wrapper function that comprises functionalities
    to execute a single test scenario.

    :param dict json_data: An arbitrary data.

    :returns: Result of the test scenario.
    :rtype: `dict'
    """
    required_args, optional_kwargs = core.extract_json_data(json_data)
    http_method, url = core.prepare_request_args(*required_args)
    response = core.send_http_request(http_method, url)
    response_content = core.extract_http_response_content(response)
    # Add a JSON property 'name' in the content
    response_content['name'] = json_data['name']

    return [response_content]


def execute_multiple_test_scenarios(list_of_dicts):
    """Wrapper function that comprises functionality
    to execute multiple tests scenarios.

    :param list list_of_dicts: List with values of type `dict`.

    :returns: Results of the tests scenarios.
    :rtype: `list'
    """
    results = [
        execute_single_test_scenario(json_data) for json_data in list_of_dicts
    ]

    return results


# ===========================
# CLI
# ===========================


def _execute(file):
    """Wrapper function that executes single or multiple
    test scenarios according to the content from file.

    :param str file_path: Optional file path.

    :returns: Text output with the result.
    :rtype: `str'
    """
    try:
        list_of_content = core.load_content_from_json_file(file)
        # Actually, the zeroth index contains the content
        content = list_of_content[0]

        # Depends on a type of the content loaded from the file,
        # the business logic for single or multiple test scenarios
        # is executed.
        if isinstance(content, dict):
            list_of_result = execute_single_test_scenario(content)
        elif isinstance(content, list):
            list_of_result = execute_multiple_test_scenarios(content)
        else:
            return 'The content from the file is not correctly formatted.'

        output_for_print = prepare_data_for_print(list_of_result)
    except Exception as exc:
        return str(exc)

    return output_for_print
