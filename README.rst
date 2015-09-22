install
=======

::

    pip install ilio


usage
=====

.. code:: python

    from ilio import read, write

    content = read('filename')
    write('filename', content)

    # there is fread=read and fwrite=write so you can import them
    # from ilio import fread, fwrite
