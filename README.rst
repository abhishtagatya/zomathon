zomathon
========

.. image:: https://badge.fury.io/py/zomathon.svg
    :target: https://badge.fury.io/py/zomathon


Python Module for the Zomato API.

About the Zomato API
--------------------

.. figure:: http://knowstartup.com/wp-content/uploads/2015/09/logo-300x212.png
   :alt: zomato

See the official API documentation for more information.

https://developers.zomato.com/api

Install
-------

::

   $ pip3 install zomathon


Only pip3 is supported for now. If you don’t have pip installed on your
system

::

   $ git clone https://github.com/abhishtagatya/zomathon
   $ cd zomathon
   $ python3 setup.py install

Getting Started
---------------

Usage :

::

   import os
   import sys
   import json

   from zomathon import ZomatoAPI

   API_KEY = os.environ.get('ZOMATO_API_KEY')
   zom = ZomatoAPI(API_KEY)

   # For complete help on the module
   help(zom)

Make sure to check out ``example/basic_usage.py`` for demonstrations :

::

   $ python3 example/basic_usage.py

Or check out the interactive documentation over at `Zomato Documentation <https://developers.zomato.com/documentation>`__.

Authors
-------

-  Abhishta Gatya - Initial Work

License
-------

This project is licensed under the MIT License - see the `LICENSE <https://github.com/abhishtagatya/zomathon/blob/master/LICENSE>`__. file
for details
