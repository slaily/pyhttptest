import pytest

from pyreqtest import http
from pyreqtest.exceptions import HTTPMethodNotSupportedError


def test_method_dispatcher():
    with pytest.raises(HTTPMethodNotSupportedError) as exc:
        args = ('head', 'http://localhost:8080/users')
        http.method_dispatcher(*args)

    exception_message = "An HTTP method ('HEAD') is not supported by the application."

    assert exception_message == str(exc.value)
