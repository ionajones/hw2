import pytest
import numpy as np

from phys305_hw2 import fd, Rp

def test_fd():

    f1 = lambda x: x
    f2 = lambda x: x * x
    f3 = lambda x: x * x * x

    assert fd(f1, 1, 1e-6) == pytest.approx(1.0, 1e-3)
    assert fd(f2, 1, 1e-6) == pytest.approx(2.0, 1e-3)
    assert fd(f3, 1, 1e-6) == pytest.approx(3.0, 1e-3)

def test_Rp():

    theta = np.pi / 4
    v0    = 10.0
    g     = 9.8

    Rp0 = Rp(theta, v0, g, 0.00)
    assert Rp0 == pytest.approx(0.0, 1e-3)

    Rp0 = Rp(theta, v0, g, 0.01)
    assert Rp0 == pytest.approx(-0.0965, 1e-3)

    Rp0 = Rp(theta, v0, g, 0.02)
    assert Rp0 == pytest.approx(-0.1899, 1e-3)
