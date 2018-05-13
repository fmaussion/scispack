# A simple scientific python package template

**scispack** stands for "simple scientific package" or "super scientific
package" depending on your mood today.

It was written for the University of Innsbruck's
[scientific programming](http://fabienmaussion.info/scientific_programming)
lecture as a package template for the assignments.

It is an extended version of the
[sampleproject](https://github.com/pypa/sampleproject) package, maintained by
the [Python Packaging Authority](https://packaging.python.org/). My
template doesn't include some of the overhead recommended for larger projects
targeting to be published on [PyPi](https://pypi.org/): instead, the focus is
put on standard recommendations for package structure, development and testing.

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
a script to be used as a command line programm. After installation,
just type:

    $ scispack --help

To see the many functionalities it has to offer.

## Testing

I recommend to use [pytest](https://docs.pytest.org) for testing. To test
the package, do:

    $ pytest .

From the package root directory.

## Package structure



## License

With the exception of the ``setup.py`` file which was adapted from the
[sampleproject](https://github.com/pypa/sampleproject) package, all the
code in this repository is dedicated to the public domain.
