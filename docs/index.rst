ANSIConv
========

**Bitbucket Repo:** https://bitbucket.org/dhrrgn/ansiconv

Version: **1.0.0**

A Python module for converting ANSI coded text and converts it to either plain
text or HTML.

Install
-------

**From PyPI**

.. code-block:: none

    $ pip install ansiconv

**From Git**

.. code-block:: none

    $ git clone https://bitbucket.org/dhrrgn/ansiconv.git
    $ cd ansiconv
    $ python setup.py install

Example
--------

.. code-block:: python

    import ansiconv

    txt = open('foo.txt', 'r').read()

    plain = ansiconv.to_plain(txt)
    html = ansiconv.to_html(txt)
    css = ansiconv.base_css()

    html_file = open("foo.html", "w")
    html_file.write("""
    <html>
      <head><style>{0}</style></head>
      <body>
        <pre class="ansi_fore ansi_back">{1}</pre>
      </body>
    </html>
    """.format(css, html))

CSS Styles
----------

When converting to HTML, it uses ``span`` elements and added ``classes`` to them.
The following are the classes used, along with their base styles (when using ``ansiconv.base_css()``):

.. code-block:: css

    .ansi_fore { color: #FFFFFF; }
    .ansi_back { background-color: #000000; }
    .ansi1 { font-weight: bold; }
    .ansi3 { font-weight: italic; }
    .ansi4 { text-decoration: underline; }
    .ansi9 { text-decoration: line-through; }
    .ansi30 { color: #000000; }
    .ansi31 { color: #FF0000; }
    .ansi32 { color: #00FF00; }
    .ansi33 { color: #FFFF00; }
    .ansi34 { color: #0000FF; }
    .ansi35 { color: #FF00FF; }
    .ansi36 { color: #00FFFF; }
    .ansi37 { color: #FFFFFF; }
    .ansi40 { background-color: #000000; }
    .ansi41 { background-color: #FF0000; }
    .ansi42 { background-color: #00FF00; }
    .ansi43 { background-color: #FFFF00; }
    .ansi44 { background-color: #0000FF; }
    .ansi45 { background-color: #FF00FF; }
    .ansi46 { background-color: #00FFFF; }
    .ansi47 { background-color: #FFFFFF; }


:mod:`ansiconv` Module
=======================

.. automodule:: ansiconv
    :members:
    :undoc-members:
    :show-inheritance:
