import pytest
import numpy as np

from phys305_hw2 import gd_hist, Theta

def test_gd():

    f1 = lambda x: -(x - 1)**2
    f2 = lambda x: -(x - 2)**2
    f3 = lambda x: -(x - 3)**2

    x1 = gd_hist(f1, 0, 0.01)[-1]
    assert x1 == pytest.approx(1.0, 0.1)

    x2 = gd_hist(f2, 0, 0.01)[-1]
    assert x2 == pytest.approx(2.0, 0.1)

    x3 = gd_hist(f3, 0, 0.01)[-1]
    assert x3 == pytest.approx(3.0, 0.1)

def test_Theta():

    v0 = 10.0
    g  =  9.8

    theta0 = Theta(v0, g, 0.00)
    assert theta0 == pytest.approx(np.pi/4, 1e-3)

    theta0 = Theta(v0, g, 0.01)
    assert theta0 == pytest.approx(0.7836, 1e-3)

    theta0 = Theta(v0, g, 0.02)
    assert theta0 == pytest.approx(0.7818, 1e-3)
