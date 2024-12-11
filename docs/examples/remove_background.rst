Remove Background
=================

This page explains how to use the Picsart Creative APIs Python SDK to remove the background from an image.
Please refer to the `API documentation <https://docs.picsart.io/reference/image-remove-background>`_ for the full list of the features and their possible values and to the API Reference :ref:`remove_background_client` for the SDK usage.

Simple use case for Remove Background
-------------------------------------

You can easily remove the background from an image using a file or URL.

Example:
~~~~~~~~

.. code-block:: python

   import picsart_sdk
   from picsart_sdk.clients.client_factory import ApiClient

   client = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

   response1 = client.remove_background(image_path="./file.jpg")
   response2 = client.remove_background(image_url="https://domain.com/image.jpg")
   print(response1.data.url)
   print(response2.data.url)


More Complex Case
-----------------

If you want to apply additional features to the background removal process, you can pass optional parameters supported by the API.

Refer to the official API documentation for details: `Remove Background <https://docs.picsart.io/reference/image-remove-background>`_.

Example:
~~~~~~~~

.. code-block:: python

   import picsart_sdk
   from picsart_sdk.clients.client_factory import ApiClient

   client = picsart_sdk.client(ApiClient.REMOVE_BACKGROUND)

   response = client.remove_background(
       image_url="https://domain.com/image.jpg",
       stroke_size=2,
       stroke_color="red"
   )
   print(response.data.url)
