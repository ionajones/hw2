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
