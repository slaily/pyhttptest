pyhttptest: HTTP tests over RESTful APIs✨
##########################################

Pissed about writing test scripts against your RESTFul APIs anytime?

Describe an HTTP Requests test cases in a simplest and widely used format JSON within a file.

Run one command and gain a summary report.

.. image:: https://www.dropbox.com/s/znlgozgcyyv98bd/pyhttptest-cli-table-of-results.png?raw=1
    :alt: pyhttptest in the command line
    :width: 100%
    :align: center


Installation
******************************************

Recommended installation method is to use ``pip``:

.. code-block:: bash

    $ pip install pyhttptest

Python version **3+** is required.


Usage
******************************************

.. code-block:: bash

    $ pyhttptest execute FILE

See also ``pyhttptest --help``.


Examples
******************************************

Single test case
------------------------------------------

Create a .json file and define a test case like an example:

``FILE: HTTP_GET.json``

.. code-block:: json

    {
      "name": "TEST: List all users",
      "verb": "GET",
      "endpoint": "users",
      "host": "https://github.com",
      "headers": {
        "Accept-Language": "en-US"
      },
      "query_string": {
        "limit": 5
      }
    }

Execute a test case:

.. code-block:: bash

    $ pyhttptest execute FILE_PATH/HTTP_GET.json

Result:

.. image:: https://www.dropbox.com/s/algkq1lswqpfx53/pyhttptest-cli.png?raw=1
    :alt: pyhttptest in the command line
    :width: 100%
    :align: center

Мultiple test cases
------------------------------------------

Create a .json file and define a test cases like an example:

``FILE: requests.json``

.. code-block:: json

    [
      {
        "name":"TEST: List all users",
        "verb":"GET",
        "endpoint":"api/v1/users",
        "host":"http://localhost:8085/",
        "headers":{
           "Accept-Language":"en-US"
        },
        "query_string":{
           "limit":1
        }
      },
      {
        "name":"TEST: Add a new user",
        "verb":"POST",
        "endpoint":"api/v1/users",
        "host":"http://localhost:8085/",
        "payload":{
           "username":"pyhttptest",
           "email":"admin@pyhttptest.com"
        }
      },
      {
        "name":"TEST: Modify an existing user",
        "verb":"PUT",
        "endpoint":"api/v1/users/XeEsscGqweEttXsgY",
        "host":"http://localhost:8085/",
        "payload":{
           "username":"pyhttptest"
        }
      },
      {
        "name":"TEST: Delete an existing user",
        "verb":"DELETE",
        "endpoint":"api/v1/users/XeEsscGqweEttXsgY",
        "host":"http://localhost:8085/"
      }
    ]

Execute a test case:

.. code-block:: bash

    $ pyhttptest execute FILE_PATH/requests.json

Result:

.. image:: https://www.dropbox.com/s/znlgozgcyyv98bd/pyhttptest-cli-table-of-results.png?raw=1
    :alt: pyhttptest in the command line
    :width: 100%
    :align: center

Dependencies
******************************************

Under the hood, pyhttptest uses these amazing libraries:

* `ijson <https://pypi.org/project/ijson/>`_
  — Iterative JSON parser with a standard Python iterator interface
* `jsonschema <https://python-jsonschema.readthedocs.io/en/stable/>`_
  — An implementation of JSON Schema validation for Python
* `Requests <https://python-requests.org>`_
  — Python HTTP library for humans
* `tabulate <https://pypi.org/project/tabulate/>`_
  — Pretty-print tabular data
* `click <https://click.palletsprojects.com/>`_
  — Composable command line interface toolkit


Contributing
******************************************

See `CONTRIBUTING <https://github.com/slaily/pyhttptest/blob/master/CONTRIBUTING.rst>`_.


Changelog
******************************************

See `CHANGELOG <https://github.com/slaily/pyhttptest/blob/master/CHANGELOG.rst>`_.


Licence
******************************************

BSD-3-Clause: `LICENSE <https://github.com/slaily/pyhttptest/blob/master/LICENSE>`_.


Authors
******************************************

`Iliyan Slavov`_

.. _Iliyan Slavov: https://www.linkedin.com/in/iliyan-slavov-03478a157/
