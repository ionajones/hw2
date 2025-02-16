# PHYS305 Homework Set #2

Welcome to the repository for **Homework Set #2** in PHYS305.
This homework set is worth **10 points** and is designed to test your
understanding of topics that we covered in the first five classes.
The submission cutoff time is at **Tuesday Feb 25th, 11:59pm** Arizona
time.


## Structure and Grading

This homework set consists of **five assignments**, each contributing
equally to your overall grade.
The grading breakdown is as follows:

1. **Automated Evaluation (50%)**:
   * Each assignment will be graded using `pytest`, an automated
     testing framework.
   * The correctness of your solutions accounts for 1 point per
     assignment (5 points in total).
   * You can run `pytest` in GitHub Codespaces or your local
     development environment to verify your solutions before
     submission.

2. **Documentation and Coding Practices (50%)**:
   * The remaining 1 point per assignment (5 points total) will be
     based on documentation and coding practices.
   * Clear and concise **documentation** of your code, including
     meaningful comments.
   * Adherence to good **coding practices**, such as proper variable
     naming, modular design, and code readability.

By following the interface and prototypes provided in each assignment
template, you can ensure compatibility with the autograding system and
maximize your score.


## Assignments

### **Assignment 1**: Implement the Vertical Motion $y(t)$ and Solve for Flight Time $T(\theta)$ (2 points)

* **Objective**:
  Implement the equation for the projectile's vertical position $y(t)$
  under linear drag, then use a root-finding algorithm to determine
  the non-trivial flight time $T$ (i.e., when $y(t) = 0$ after
  launch).

* **Details**:
  * Write a function `y(theta, v0, g, gamma, t)` that returns the
    vertical position at time `t`.
  * Make sure to handle the special case $\gamma = 0$ (no drag).
  * Implement a root finder.
  * Implement a function `T(theta, v0, g, gamma)` that uses the root
    finder to find the positive time root of `y(...) = 0`.
  * A good initial guess for the root is the no-drag flight time.
  * Test your function(s) for different parameters.
    Print or plot the results to ensure they make physical sense.
  * The description of this assignment and a code skeleton can be
    found in `src/phys305_hw2/a1.py`.

### **Assignment 2**: Implement the Horizontal Motion $x(t)$ and Compute Range (2 points)

* **Objective**:
  Write a function for the horizontal position $x(t)$ and combine it
  with the flight time from Assignment 1 to compute the projectile's
  range $R(\theta)$.

* **Details**:
  * Implement `x(theta, v0, g, gamma, t)` that returns the horizontal
    position at time `t`.
  * Make sure to handle the special case $\gamma = 0$ (no drag).
  * Compute the range $R(\theta)$ for a given $\theta$ by evaluating
    $$x\bigl(\theta, v0, g, \gamma, T(\theta)\bigr),$$
    where $T(\theta)$ is the flight time found in Assignment 1.
  * Verify that when $\gamma = 0$, your result approximates the
    standard no-drag range formula
    $$R(\theta) = \frac{v_0^2}{g},\sin\bigl(2,\theta\bigr).$$
  * The description of this assignment and a solution template can be
    found in phys305_hw2/a2.py.

### **Assignment 3**: Finite Difference Scheme for $R'(\theta)$ (2 points)

* **Objective**:
  Implement a finite difference approach to numerically approximate
  the derivative of the range $R(\theta)$ with respect to $\theta$.

* **Details**:
  * Given your `R(theta, v0, g, gamma)`, implement a function
    `Rp(theta, v0, g, gamma)` that approximates
    $$R'(\theta) \equiv \frac{d}{d\theta} R(\theta)$$
    using a finite difference scheme.
  * Choose a small finite difference parameter $h$ and verify that
    your approximation converges.
  * Demonstrate this derivative calculation for a few different angles
    and drag coefficients, printing or plotting the approximate
    $R'(\theta)$ values.
  * The description and relevant code can be found in
    `src/phys305_hw2/a3.py`.

### **Assignment 4**: Gradient Descent to Optimize the Launch Angle (2 points)

* **Objective**:
  Use a gradient descent algorithm and your finite-difference
  derivative from Assignment 3 to numerically find the angle $\theta$
  that maximizes $R(\theta)$.

* **Details**:
  * Create a function `gd(v0, g, gamma, theta0)` to perform gradient descent.
    * Starts with an initial guess `theta0`.
    * Computes the gradient (derivative) $R'(\theta)$ using your
      finite difference scheme from Assignment 3.
    * Updates $\theta \leftarrow \theta - \alpha \, R'(\theta)$ each
      iteration.
    * Stops when the change in $\theta$ becomes smaller than some
      tolerance `tol` or when `max_iter` is reached.
  * Experiment with different step sizes `alpha` (the "learning rate")
    to see how it affects convergence.
  * Compare the angle you find with the analytical $45^\circ$ result
    in the no-drag case, and observe how it changes for increasing
    $\gamma$.
  * A code template for this assignment can be found in
    `src/phys305_hw2/a4.py`.


## Submission Guidelines

1. Create a new repostiory based on this template by using the GitHub
   Classroom Link https://classroom.github.com/ and work on the
   assignments in GitHub Codespaces or locally.

2. Use `pytest` to test your solutions before submission.
   Ensure that all test cases pass to maximize your automated
   evaluation score.

3. **Submit your completed assignments by pushing your changes to the
   repository before the deadline.**

**Note**:
**The submission deadline is a strict cutoff.
No submission will be accepted after the deadline.**
Be sure to manage your time effectively and plan ahead to ensure your
work is submitted on time.
Frequent and incremental `git commit` and `git push` are recommended
to ensure your latest work are seen.


## Additional Notes

* **Collaboration**:
  You are encouraged to discuss ideas with your peers, but your
  submission must reflect your own work.
* **Help and Resources**:
  If you encounter any difficulties, please refer to the course
  materials, consult your instructor, or seek help during office
  hours.
* **Deadlines**:
  Be mindful of the submission deadline, as late submissions will not
  be accepted.

Good luck, and enjoy working on the assignments!
