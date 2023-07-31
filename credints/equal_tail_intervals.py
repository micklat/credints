from nbag import construct
from sympy.stats import Normal, LogNormal, quantile, rv
from typing import Optional
import numpy as np


def normal_params_from_eti(credence: float, low: float, high: float) -> tuple[float, float]:
    mean = (low+high)/2
    assert low < high
    assert 0 < credence < 1, 'credence must be strictly between 0 and 1'
    
    z = quantile(Normal("stdnorm",0,1))(0.5 + credence/2)
    stdev = (high - low) / (2 * z)
    return mean, stdev

def normal(credence: float, bounds: list[float], name:Optional[str]=None) -> rv.RandomSymbol:
    """
    Returns a normal RandomSymbol that falls within <bounds> at probability <credence>, and has
    equal probability of being higher than bounds[1] as it does of being lower than bounds[0].
    """
    low, high = bounds
    mean, stdev = normal_params_from_eti(credence, low, high)
    return construct(Normal, name, mean, stdev)


def log_normal(credence: float, bounds: list[float], name:Optional[str]=None) -> rv.RandomSymbol:
    """
    Returns a normal RandomSymbol that falls within <bounds> at probability <credence>, and has
    equal probability of being higher than bounds[1] as it does of being lower than bounds[0].
    """
    low, high = bounds
    mean, stdev = normal_params_from_eti(credence, np.log(low), np.log(high)) 
    return construct(LogNormal, name, mean, stdev)


__all__ = ["normal"]

