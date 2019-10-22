pyreqtest: HTTP tests over RESTful APIs✨
#########################################

Pissed about writing test scripts against your RESTFul APIs anytime?
Describe an HTTP Requests test cases in a simplest and widely used format JSON within a file.
Run one command and gain a summary report.

.. image:: https://www.dropbox.com/s/xas6p7mwv400xjz/pyreqtest-cline.png?raw=1
    :alt: pyreqtest in the command line
    :width: 100%
    :align: center


Installation
-------------

Recommended installation method is to use ``pip``:

.. code-block:: bash

    $ pip install pyreqtest

Python version **3+** is required.


Usage
-------------------

.. code-block:: bash

    $ pyreqtest execute FILE

See also ``pyreqtest --help``.


Examples
--------

Create a .json file and define a test case like an example:

``FILE: GET_USERS.json``

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

    $ pyreqtest execute FILE_PATH/GET_USERS.json


Dependencies
~~~~~~~~~~~~

Under the hood, HTTPie uses these two amazing libraries:

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
------------

See `CONTRIBUTING.rst <https://github.com/slaily/pyreqtest/CONTRIBUTING.rst>`_.


Change log
----------

See `CHANGELOG <https://github.com/slaily/pyreqtest/blob/master/CHANGELOG>`_.


Licence
-------

BSD-3-Clause: `LICENSE <https://github.com/slaily/pyreqtest/blob/master/LICENSE>`_.


Authors
-------

`Iliyan Slavov`_

.. _Iliyan Slavov: https://www.linkedin.com/in/iliyan-slavov-03478a157/
