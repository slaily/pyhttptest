import sys

from pyreqtest.constants import HTTP_METHOD_NAMES
from pyreqtest.exceptions import HTTPMethodNotSupportedError


def method_dispatcher(*args, **kwargs):
    """Try to dispatch to the right HTTP method handler.
    If an HTTP method isn't on the approved list, defer
    to the error handler. Otherwise, the HTTP Method is
    processed by the appropriate handler.

    :param args: Expect arguments in format (http_method, url).
    :param kwargs: Optional arguments like HTTP headers, cookies and etc.

    :returns: Result from the handler.
    :rtype: func
    """
    http_method, url = args

    if http_method not in HTTP_METHOD_NAMES:
        raise HTTPMethodNotSupportedError(http_method)

    handler = getattr(sys.modules[__name__], http_method)

    return handler(*args, **kwargs)
