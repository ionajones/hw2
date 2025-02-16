import pytest
import numpy as np

from phys305_hw2 import newton, y, T

def test_newton():
    def f1(x):
        return (x - 1)
    def f2(x):
        return (x - 2) * (x - 2)
    def f3(x):
        return (x - 3) * (x - 3) * (x - 3)

    x = newton(f1, 0.0)
    assert x == pytest.approx(1)

    x = newton(f2, 0.0)
    assert x == pytest.approx(2)

    x = newton(f3, 0.0)
    assert x == pytest.approx(3)

def test_y():

    theta = np.pi / 4
    v0    = 10.0
    g     = 9.8
    t     = 1.0

    y0 = y(theta, v0, g, 0.00, t)
    assert y0 == pytest.approx(2.1711, 1e-3)

    y0 = y(theta, v0, g, 0.01, t)
    assert y0 == pytest.approx(2.152, 1e-3)

    y0 = y(theta, v0, g, 0.02, t)
    assert y0 == pytest.approx(2.133, 1e-3)

def test_T():

    theta = np.pi / 4
    v0    = 10.0
    g     = 9.8
    t     = 1.0

    T0 = T(theta, v0, g, 0.00)
    assert T0 == pytest.approx(1.4431, 1e-3)

    T0 = T(theta, v0, g, 0.01)
    assert T0 == pytest.approx(1.4396, 1e-3)

    T0 = T(theta, v0, g, 0.02)
    assert T0 == pytest.approx(1.4362, 1e-3)
