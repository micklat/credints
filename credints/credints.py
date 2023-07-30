from nbag import construct
from sympy.stats import Normal

def normal_eti(credence: float, bounds: list[float], name=None):
    low, high = bounds
    mean = (low+high)/2
    std = 3 # TODO (Edo has this, as does squigglepy)
    return construct(Normal, name, mean, std)

def test():
    x = normal_eti(0.8, [1.1, 1.4])
    z = normal_eti(0.9, [2,4])
    y = x*z
    try:
        normal_eti(0.9, [2, 4])
    except:
        pass
    else:
        assert False, "calling normal() outside of an assignment should fail"
    assert str(y)=="x*z"


if __name__ == '__main__':
    test()

