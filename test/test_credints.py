from credints import normal_eti
from numpy.testing import assert_almost_equal


def test_normal_eti():
    try:
        normal_eti(0.9, [2, 4])
    except:
        pass
    else:
        assert False, "calling normal_eti() outside of an assignment should fail"
    credence = 0.9
    low, high = 2,4
    x = normal_eti(credence, [low, high])
    from sympy.stats import P
    effective_credence = P((x>low) & (x<high)).evalf()
    assert_almost_equal(credence, effective_credence)


if __name__ == "__main__":
    import pytest
    pytest.main()

