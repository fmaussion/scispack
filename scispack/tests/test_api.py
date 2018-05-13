# Just tests that the functions are callable and the version is there
from distutils.version import LooseVersion
import scispack


def test_version():
    assert LooseVersion(scispack.__version__) >= LooseVersion('0.0.0')


def test_functions():
    # This is not a very common test but for the sake of it lets do it

    funcs = dir(scispack)

    assert 'area_of_circle' in funcs
    assert 'give_me_the_answer' in funcs
