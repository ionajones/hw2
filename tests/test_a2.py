import pytest
import numpy as np

from phys305_hw2 import x, R

def test_x():

    theta = np.pi / 4
    v0    = 10.0
    g     = 9.8
    t     = 1.0

    x0 = x(theta, v0, g, 0.00, t)
    assert x0 == pytest.approx(7.0711, 1e-3)

    x0 = x(theta, v0, g, 0.01, t)
    assert x0 == pytest.approx(7.0358, 1e-3)

    x0 = x(theta, v0, g, 0.02, t)
    assert x0 == pytest.approx(7.0008, 1e-3)

def test_R():

    theta = np.pi / 4
    v0    = 10.0
    g     = 9.8

    R0 = R(theta, v0, g, 0.00)
    assert R0 == pytest.approx(10.2041, 1e-3)

    R0 = R(theta, v0, g, 0.01)
    assert R0 == pytest.approx(10.1077, 1e-3)

    R0 = R(theta, v0, g, 0.02)
    assert R0 == pytest.approx(10.0116, 1e-3)
