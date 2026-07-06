# Chaos in Circular Billiards
## More Physics with Matlab By Dan Green
## CHAPTER1 / MATHEMATICS / 1.1CHAOS

This is a simple example of a Chaos System demonstrating the motion of a ball in a circular environment.

This project simulates the reflection of a ball inside a circle. It demonstrates how a small change in the initial angle leads to totally different trajectories. a classic characteristic of chaotic systems.

The ball starts from point (1, 0) on the unit circle and moves in a straight line until it hits the boundary. Upon collision, it reflects according to the law of reflection:

v: is the velocity before collision
n:  is the unit normal vector at the collision point (pointing outward)
v':  is the velocity after collision

Simulates multiple bounces (default: 20)
Visualizes trajectories with matplotlib
Compares two different initial angles side by side
Shows reflection points on the circle boundary


The simulation shows two trajectories with initial angles of 20 and 21 degree:

20 trajectory(blue): One possible path
21 trajectory(green): A completely different path

Despite only 1 degree difference, the paths diverge significantly - demonstrating sensitive dependence on initial conditions(the Butterfly Effect).
