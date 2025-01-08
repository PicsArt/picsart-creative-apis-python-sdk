Quickstart
==========

This guide details the steps needed to install or update the **Picsart Creative APIs Python SDK** (referred further as **Picsart Python SDK**)

Installation
------------

To use Picsart Python SDK, you first need to install it and its dependencies.

.. _quickstart_install_python:

Install or update Python
~~~~~~~~~~~~~~~~~~~~~~~~

Before installing Picsart Python SDK, install Python 3.9 or later.

For information about how to get the latest version of Python, see the official
`Python documentation <https://www.python.org/downloads/>`_.

Install Picsart Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the latest `picsart-sdk` release via :command:`pip`::

    pip install picsart-sdk

If your project requires a specific version of picsart-sdk, or has compatibility concerns with
certain versions, you may provide constraints when installing::

    # Install picsart-sdk version 1.0 specifically
    pip install picsart-sdk==1.0.0

.. note::

   The latest development version of picsart-sdk is on `GitHub <https://github.com/PicsArt/picsart-creative-apis-python-sdk>`_.

Configuration
~~~~~~~~~~~~~

In order to use the Picsart Python SDK, you need to obtain an API KEY from `picsart.io <https://picsart.io/>`_ portal.

The framework will automatically look for the API KEY in the `PICSART_API_KEY` environment variable.
If the environment variable isn't set, you will have to pass it programmatically. Refer the section below.

Using Picsart Python SDK
~~~~~~~~~~~~~~~~~~~~~~~~

Create a Client
^^^^^^^^^^^^^^^

**Option 1: Using environment variable for the API Key**

If the :code:`PICSART_API_KEY` environment variable is set, you can quickly create a client:

.. code-block:: python

    import picsart_sdk
    from picsart_sdk import PicsartAPI
    from picsart_sdk.clients import RemoveBackgroundClient

    client: RemoveBackgroundClient = picsart_sdk.client(PicsartAPI.REMOVE_BACKGROUND)

**Option 2: Passing the API Key manually**

You can also pass the API key directly to the API client:

.. code-block:: python

    import picsart_sdk
    from picsart_sdk import PicsartAPI
    from picsart_sdk.clients import RemoveBackgroundClient

    client: RemoveBackgroundClient = picsart_sdk.client(
        PicsartAPI.REMOVE_BACKGROUND,
        api_key="YOUR_API_KEY"
    )


.. note::

   We recommend always using Python type hinting, such as :code:`upload_client: UploadClient = picsart_sdk.client(...)`, to fully leverage IDE autocompletion and improve code readability.

**Remove the background of an image**

After acquiring the client, you can call specific methods of that client. In the case of :code:`RemoveBackgroundClient`,
you can call :code:`remove_background` method.

.. code-block:: python

    from picsart_sdk.api_responses import ApiResponse
    ...

    response: ApiResponse = client.remove_background(image_path="./file.jpg")
    print(response.data.url)

The image without background will be available in the Picsart CDN at the URL from :code:`response.data.url`.

.. note::

    You can find an extensive list of code snippets in the :code:`examples` folder from the `GitHub repo <https://github.com/PicsArt/picsart-creative-apis-python-sdk>`_.

Debugging
~~~~~~~~~

You can enable extra logging providing the following environment variables:

* :code:`PICSART_SDK_LOGGING_LEVEL`: Controls the logging level. Possible values: :code:`CRITICAL`, :code:`ERROR`, :code:`WARNING`, :code:`INFO`, :code:`DEBUG`, :code:`NOTSET`. If :code:`PICSART_SDK_LOGGING_LEVEL` is not provided or contains an invalid value, logging will be disabled.
* :code:`PICSART_SDK_LOG_HTTP_CALLS`: Enables logging of HTTP calls made to the Picsart API. Possible values: :code:`true` or :code:`false`.
* :code:`PICSART_SDK_LOG_HTTP_CALLS_HEADERS`: Logs the HTTP headers used in API calls. Possible values: :code:`true` or :code:`false`. **Note**: Enabling this will log sensitive information, including the :code:`PICSART_API_KEY`.

Other environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :code:`PICSART_SDK_DEFAULT_HTTP_TIMEOUT_SECONDS`: Control the HTTP timeout in seconds for the API calls. These value is only for the client. If the timeout is happening in the backend infrastructure you can still get a timeout error.
