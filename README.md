Orange3 Statsmodels Add-on
==========================

This is a Statsmodels add-on for [Orange3](http://orange.biolab.si).
It provides several widgets wrapping the Statsmodels functions and making it possible
to specify models using R-like formulae.


Installation
------------

To install the add-on from source run

    pip install .


Usage
-----

After the installation, the widget from this add-on is registered with Orange. To run Orange from the terminal,
use

    orange-canvas

or

    python -m Orange.canvas

The new widget appears in the toolbox bar under the section Statsmodels.

![screenshot](https://github.com/biolab/orange3-example-addon/blob/master/screenshot.png)


Development
-----------

I develop on Windows and use the [uv](https://docs.astral.sh/uv/) package manager.
My workflow is as follows.

First I create an isolated virtual env in the project directory:

    uv venv
    .\.venv\Scripts\activate

Then I install Orange _into this environment_ following instructions from the site:

    uv pip install PyQt5 PyQtWebEngine
    uv pip install orange3

At this point I can run Orange for testing purposes with

    python -m Orange.canvas

provided the dev environment is active.

To register this add-on with Orange, but keep the code in the development directory
(do not copy it to Python's site-packages directory), I run

    uv pip install -e .

In this way I can edit the source code, and after restarting Orange test my changes.

Documentation / widget help can be built by running

    make html htmlhelp

from the doc directory.
