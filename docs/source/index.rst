Selamat Datang 2 ApiNyaEr Documentation
=======================================

Overview
--------

ApiNyaEr adalah kompilasi api dari berbagai resource, seperti Luminai yang popular/sering di gunakan di whatsapp bot


.. attention ::

   This project is under active development. Expect frequent updates and improvements.


.. toctree::
   :hidden:
   :caption: Contents:

   client
   saavn/apinya/index



Installation
------------

Untuk menginstall ApiNyaEr, kamu bisa menggunakan pip:

.. code-block:: bash

   pip install ApiNyaEr

Penggunaan 
----------


.. important :: 

   All methods of the :obj:`~ApiNyaEr.ErApi` or :obj:`~ApiNyaEr.Lagunya` can be used asynchronously, allowing for non-blocking operations and improved performance in asynchronous environments.

To start using ApiNyaEr, follow these steps:

1. Import the ErApi module and initialize the client:

   .. code-block:: python

      from ApiNyaEr import ErApi

      apinya = ErApi()

2. Use the ErApi to make requests to the integrated APIs:

   .. code-block:: python

      res = await apinya.write("what the er")

      print(res)

3. You can use the :obj:`~ApiNyaEr.Lagunya` for making request for endpoint of saavn.dev

   .. code-block:: python 

      from ApiNyaEr import Lagunya

      api = Lagunya()

      r = await api.search("Gue Mah Apah Atuh")
      
      print(r)