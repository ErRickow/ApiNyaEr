Welcum 2 ApiNyaEr Documentation
===============================

Overview
--------

ApiNyaEr is a compilation of APIs from various resources, such as Luminai, which is popular and often used in WhatsApp bots.

.. attention ::

   This project is currently in active development, with updates and improvements released frequently.


.. toctree::
   :hidden:
   :caption: Contents:

   client
   saavn/apinya/index



Installation
------------

To install ApiNyaEr, simply run the following pip command to install it from PyPI:

.. code-block:: bash

   pip install ApiNyaEr

Usage 
-----


.. important :: 

   All methods of the :obj:`~ApiNyaEr.ErApi` or :obj:`~ApiNyaEr.Musiknya` can be used asynchronously, allowing for non-blocking operations and improved performance in asynchronous environments.

To start using ApiNyaEr, follow these steps:

1. Import the ErApi module and initialize the client:

   .. code-block:: python

      from ApiNyaEr import ErApi

      apinya = ErApi()

2. Use the ErApi to make requests to the integrated APIs:

   .. code-block:: python

      res = await apinya.write("what the er")

      print(res)

3. You can use the :obj:`~ApiNyaEr.Musiknya` for making request for endpoint of saavn.dev

   .. code-block:: python 

      from ApiNyaEr import Musiknya

      api = Musiknya()

      r = await api.search("Gue Mah Apah Atuh")
      
      print(r)