Project for Adding Data to DOCX
=================================

About
-----

This project is designed to add information to an existing `.docx` document. The data is provided in the form of a dictionary and is then inserted into the document using the `sbi_special_docx_master` module along with the `python-docx` library. A predefined data structure is used during the process.

Features
--------

- **DOCX Processing:** Automates the editing and formatting of DOCX documents.
- **Flexible Configuration:** Easily customize processing parameters to suit your specific needs.
- **Seamless Integration:** Integrates smoothly with other services and workflows thanks to its open architecture.
- **Extensibility:** A clear and modular code structure allows you to add new features or modify existing ones with ease.

Table of Contents
-----------------

- `Installation`_
- `Usage`_
- `Main Components`_

Installation
------------

The project is available on the Python Package Index (PyPI), making installation simple and straightforward.
To install, run:

.. code-block:: python

    pip install sbi-special-docx-master


Main Components
---------------

1. ``sbi_special_docx_master``

   This module contains the ``AddDocx`` class, which allows you to add textual information, images, and headers to a `.docx` document.

Usage
-----

Imports:

.. code-block:: python

   from sbi_special_docx_master import AddDocx
   from docx import Document

Loading an existing `.docx` document:

.. code-block:: python

   add_file = "Your_file.docx"
   doc = Document(add_file)

Creating a dictionary with information:

.. code-block:: python

   info_dict = {
       'separate_information_relations': [
           {
               'content': 'str',
               'images': [
                   {
                       'file': '<Base64>'
                   }
               ],
               'title': 'str'
           },
           {
               'content': 'str',
               'images': [
                   {
                       'file': int
                   }
               ],
               'title': 'str'
           }
       ]
   }

Adding data to the document:

.. code-block:: python

   spec = AddDocx(doc, info_dict)

Generating a bytes stream of the document:

.. code-block:: python

    io_doc = spec.save_io()

Generating and saving the `.docx` document:

.. code-block:: python

   spec.save('my_file.docx')

Retrieving the document object:

.. code-block:: python

    doc = spec.document

Generating a bytes stream of the document:

.. code-block:: python

    io_doc = spec.save_io()


Check whether the addition operation was successful:

.. code-block:: python

    doc_suc = spec.has_succeeded


