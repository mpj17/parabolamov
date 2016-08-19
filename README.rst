==============
Parabola movie
==============

A small Python script that I built to play with ``matplotlib``
and ``moviepy``. The first two dozen lines (the complex bit)
create a series of ``matplotlib.pyplot.figure`` instances,
returned by the ``figures()`` generator. The last two dozen lines
converts the figures into ``moviepy.editor.ImageClip`` instances,
and concatenates them together into `the movie
<https://www.youtube.com/watch?v=9LbsDH4KXk4>`_ ``foo.mp4``.

Requirements
============

This is a Python 3 project that only requires products on
PyPI. Clone this project, turn the directory into a Python 3
virtual environment, install its dependencies, and run the
script::

   $ git clone https://github.com/mpj17/parabolamov
   $ cd parabolamov
   $ virtualenv -ppython3 .
   $ . ./bin/activate
   (parabolamov)$ pip install matplotlib numpy moviepy
   (parabolamov)$ python parabolamov.py
