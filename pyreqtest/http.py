import sys

import requests

from pyreqtest import constants
from pyreqtest.logger import logger
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

    if http_method not in constants.HTTP_METHOD_NAMES:
        raise HTTPMethodNotSupportedError(http_method)

    handler = getattr(sys.modules[__name__], http_method)

    return handler(*args, **kwargs)


def get(*args, **kwargs):
    """Sends an HTTP GET request.

    :param args: URL argument on the first index(args[1]).
    :param kwargs: Optional arguments that ``requests.get`` takes.

    :returns: :class:`Response` object or `None` if an error occurred.
    :rtype: :class:`requests.Response` or `None`
    """
    url = args[1]
    kwargs.setdefault('allow_redirects', True)

    try:
        return requests.get(url, **kwargs)
    except Exception as exc:
        logger.exception(str(exc))

    return None
