ANSIConv
========

Version: **1.0.0**

A Python module for converting ANSI coded text and converts it to either plain
text or HTML.

**Bitbucket Repo:** https://bitbucket.org/dhrrgn/ansiconv

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

:mod:`ansiconv` Package
=======================

.. automodule:: ansiconv
    :members:
    :undoc-members:
    :show-inheritance:
