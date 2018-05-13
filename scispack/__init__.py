# This is hard coded version string.
# Real packages use more sophisticated methods to make sure that this
# string is synchronised with `setup.py`, but for our purposes this is OK
__version__ = '0.0.1'

# __init__ is often used as entry point for what is called "the API"
# (application programming interface). This way, users of the lib don't
# have to know about the internal structure of a package, they just want
# to know what functionality it provides
from scispack.utils import area_of_circle
from scispack.utils import give_me_the_answer
