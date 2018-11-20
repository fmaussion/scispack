# A simple scientific python package template

**scispack** stands for "simple scientific package" or "super scientific
package" depending on your current mood.

It was written for the University of Innsbruck's
[scientific programming](http://fabienmaussion.info/scientific_programming)
lecture as a package template for the assignments.

It is an extended version of the
[sampleproject](https://github.com/pypa/sampleproject) package, maintained by
the [Python Packaging Authority](https://packaging.python.org/). My
template doesn't include some of the overhead recommended for larger projects
targeting to be published on [PyPi](https://pypi.org/): instead, the focus is
put on standard recommendations for package structure, development and testing.

This package provides a standard python library (``>>> import scispack``) as
well as a command line interface (``$ scispack --help``). Of course you can
skip the command line part easily by changing the ``entry_points`` in
``setup.py``.

## HowTo

Download the template, either downloading it (green button top-right) or
by cloning it (if you know `git` already). From the package root directory
you should be able to use all the "functionalities", such as:

    >>> from scispack import area_of_circle
    >>> area_of_circle(12.)
    452.3893421169302

What you probably want to do, however, is to try to install it using pip:

    $ pip install .

This will install the package in your conda or pip environment and make it
available everywhere. Also, it will give you access to the command line
interface.

If you use this template for your own package, you should start with renaming
all appearances of ``scispack`` in the project and then install your new
package in development mode:

    $ pip install -e .

This is much more flexible than ``pip install .``: instead of copying the
package in your python PATH, ``pip install -e`` will create symbolic links
to this folder, thus making all your changes available right away.

## Command line interface

The example ``setup.py`` shows how to add a so-called "entry point" for
a script to be used as a command line program. After installation,
just type:

    $ scispack --help

To see the many functionalities it has to offer.

## Testing

I recommend to use [pytest](https://docs.pytest.org) for testing. To test
the package, do:

    $ pytest .

From the package root directory.

## Package structure

#### Directory root (``./``)

- ``.gitignore``: for git users only
- ``LICENSE.txt``: [always](https://help.github.com/articles/licensing-a-epository/) license your code
- ``README.md``: this page
- ``setup.py``: this is what makes your package insallable by ``pip``. It
  contains a set of simple instructions regarding e.g. the name of the package,
  its version number, or where to find command line scripts
  
#### The actual package (``./scispack``)

- ``__init__.py``: tells python that the directory is a package and enables
  the  "dotted module names"  import syntax. It is often empty,fla but here
  we added some entry points to the package's API and the version string.
- ``cfg.py``, ``utils.py`` and ``cli.py``: the modules
- ``cli.py``: entry point for the command line interface 
- ``cfg.py``: container module for the package parameters and constants

#### The tests (``./scispack/tests``)

One test file pro module. Their name has to start with ``test_`` in order
to be detected by pytest.

## License

With the exception of the ``setup.py`` file which was adapted from the
[sampleproject](https://github.com/pypa/sampleproject) package, all the
code in this repository is dedicated to the public domain.
