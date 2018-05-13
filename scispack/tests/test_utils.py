import pytest
from numpy.testing import assert_allclose
from scispack import utils


def test_give_me_the_answer():

    # Basic functionality
    assert utils.give_me_the_answer('What makes me happy?') == 42

    # Kwarg
    assert utils.give_me_the_answer('What makes me REALLY happy?',
                                    clever=True) == 42

    # errors
    with pytest.raises(ValueError):
        utils.give_me_the_answer(42)


def test_area_of_circle():

    assert utils.area_of_circle(0) == 0
    assert_allclose(utils.area_of_circle(10), 3.14159 * 10**2, atol=0.01)
