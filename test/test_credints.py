import credints.equal_tail_intervals as ci
from numpy.testing import assert_almost_equal


def test_normal_eti():
    try:
        ci.normal(0.9, [2, 4])
    except:
        pass
    else:
        assert False, "calling equal_tail_intervals.normal() outside of an assignment should fail"
    credence = 0.9
    low, high = 2, 4
    x = ci.normal(credence, [low, high])
    from sympy.stats import P
    effective_credence = P((x>low) & (x<high)).evalf()
    assert_almost_equal(credence, effective_credence)


if __name__ == "__main__":
    import pytest
    pytest.main()

