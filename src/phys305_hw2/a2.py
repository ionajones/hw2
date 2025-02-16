#!/usr/bin/env python3

# Please look for "TODO" in the comments, which indicate where you
# need to write your code.

# Assignment 2: Implement the Horizontal Motion $x(t)$ and Compute
# Range (2 points)
#
# Objective: Write a function for the horizontal position $x(t)$ and
# combine it with the flight time from Assignment 1 to compute the
# projectile's range $R(\theta)$.

# Details:
# * Implement `x(theta, v0, g, gamma, t)` that returns the horizontal
#   position at time `t`.
# * Make sure to handle the special case $\gamma = 0$ (no drag).
# * Compute the range $R(\theta)$ for a given $\theta$ by evaluating
#   $$x\bigl(\theta, v0, g, \gamma, T(\theta)\bigr),$$
#   where $T(\theta)$ is the flight time found in Assignment 1.
# * Verify that when $\gamma = 0$, your result approximates the
#   standard no-drag range formula
#   $$R(\theta) = \frac{v_0^2}{g},\sin\bigl(2,\theta\bigr).$$
# * The description of this assignment and a solution template can be
#   found in `src/phys305_hw2/a2.py`.

def x(theta, v0, g, gamma, t):
    # TODO: document and implement the horizontal position function here
    pass

def R(theta, v0, g, gamma):
    # TODO: document and implement the range function here
    pass
