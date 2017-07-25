docstringtest
-------------

|build-status| |coverage| |docs| |license|

.. |build-status| image:: https://travis-ci.org/jakelever/docstringtest.svg?branch=master
   :target: https://travis-ci.org/jakelever/docstringtest
   :alt: Travis CI status

.. |coverage| image:: https://coveralls.io/repos/github/jakelever/docstringtest/badge.svg?branch=master
   :target: https://coveralls.io/github/jakelever/docstringtest?branch=master
   :alt: Coverage status
   
.. |docs| image:: https://readthedocs.org/projects/docstringtest/badge/
   :target: http://docstringtest.readthedocs.io/
   :alt: Documentation status
   
.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT license

docstringtest is a small package for regression testing of docstrings in Python code. It checks that all appropriate methods and functions are using ReST docstrings with parameter information so that nice documentation can be generated. This format looks like:

.. code-block:: python
   def example_function(varA,varB):
      """
      This function does nothing

      :param varA: The first variable
      :param varB: The second variable
      :type varA: The type of the first variable
      :type varB: The type of the second variable
      """
      pass

It makes it easy to check that the docstrings match with the current parameters so that documentation doesn't become out-of-step with the code. 
