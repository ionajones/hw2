#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 1: Implement the Vertical Motion $y(t)$ and Solve for
# Flight Time $T(\theta)$ (2 points)
#
# Objective: Implement the equation for the projectile's vertical
# position $y(t)$ under linear drag, then use a root-finding algorithm
# to determine the non-trivial flight time $T$ (i.e., when $y(t) = 0$
# after launch).

# Details:
# * Write a function `y(theta, v0, g, gamma, t)` that returns the
#   vertical position at time `t`.
# * Make sure to handle the special case $\gamma = 0$ (no drag).
# * Implement a root finder.
# * Implement a function `T(theta, v0, g, gamma)` that uses the root
#   finder to find the positive time root of `y(...) = 0`.
# * A good initial guess for the root is the no-drag flight time.
# * Test your function(s) for different parameters.
#   Print or plot the results to ensure they make physical sense.
# * The description of this assignment and a code skeleton can be
#   found in `src/phys305_hw2/a1.py`.

import jax
jax.config.update("jax_enable_x64", True)

from jax import numpy as np
from jax import grad

def root(f, x0, tol=1e-12, imax=1000):
    # TODO: document and implement a root finder here;
    # you may use JAX's `grad()` function for autodiff.
    """
    Finds the root of a function f(x) using Newton's method.
    
    Parameters:
    f : function
        The function whose root is to be found.
    x0 : float
        Initial guess for the root.
    tol : float, optional
        Tolerance for convergence (default is 1e-12).
    imax : int, optional
        Maximum number of iterations (default is 1000).

    Returns:
    float
        The root of the function f(x).
    """
    df = grad(f)  # Compute derivative using JAX autodiff
    x = x0
    for i in range(imax):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x
        if dfx == 0:
            raise ValueError("Derivative is zero. Newton's method fails.")
        x -= fx / dfx
    raise ValueError("Maximum iterations reached without convergence.")

def y(theta, v0, g, gamma, t):
    # TODO: document and implement the vertical position function here
        """
    Computes the vertical position y(t) of a projectile under linear drag.
    
    Parameters:
    theta : float
        Launch angle in radians.
    v0 : float
        Initial velocity magnitude.
    g : float
        Acceleration due to gravity.
    gamma : float
        Drag coefficient.
    t : float
        Time.

    Returns:
    float
        Vertical position y at time t.
    """
    v0y = v0 * np.sin(theta)
    if gamma == 0:
        return v0y * t - 0.5 * g * t**2  # No drag case
    else:
        return (v0y + g / gamma) * (1 - np.exp(-gamma * t)) / gamma - g * t / gamma

def T_flight(theta, v0, g, gamma):
    # TODO: document and implement the flight time function here
    """
    Computes the flight time T (when y(T) = 0 after launch).
    
    Parameters:
    theta : float
        Launch angle in radians.
    v0 : float
        Initial velocity magnitude.
    g : float
        Acceleration due to gravity.
    gamma : float
        Drag coefficient.
    
    Returns:
    float
        Flight time T.
    """
    T_no_drag = 2 * v0 * np.sin(theta) / g  # Initial guess (no-drag case)
    return root(lambda t: y(theta, v0, g, gamma, t), T_no_drag)

