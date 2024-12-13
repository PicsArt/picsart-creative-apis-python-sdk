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

**Option 1: Using Default Session**

If the :code:`PICSART_API_KEY` environment variable is set, you can quickly create a client:

.. code-block:: python

    import picsart_sdk
    from picsart_sdk.clients import ApiClient

    client: RemoveBackgroundClient = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

**Option 2: Creating a Session Manually**

You can also create a session manually and pass the API key directly:

.. code-block:: python

    import picsart_sdk
    from picsart_sdk.clients import ApiClient

    session = picsart_sdk.Session(api_key="YOUR_API_KEY")
    client: RemoveBackgroundClient = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

**Remove the background of an image**

After acquiring the client, you can call specific methods of that client. In the case of :code:`RemoveBackgroundClient`,
you can call :code:`remove_background` method.

.. code-block:: python

    from picsart_sdk.api_responses import ApiResponse
    ...

    response: ApiResponse = client.remove_background(image_path="./file.jpg")
    print(response.data.url)

The image without background will be available in the Picsart CDN at the URL from :code:`response.data.url`.
