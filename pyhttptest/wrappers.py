from pyhttptest import core


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

    return response_content
