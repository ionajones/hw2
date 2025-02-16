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

def newton(f, x0, tol=1e-6, imax=100):
    # TODO: document and implement a Newton-Raphson algorithm here
    pass

def y(theta, v0, g, gamma, t):
    # TODO: document and implement the vertical position function here
    pass

def T(theta, v0, g, gamma):
    # TODO: document and implement the flight time function here
    pass
