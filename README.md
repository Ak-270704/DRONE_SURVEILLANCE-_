📌 Overview

This project implements a Drone Surveillance System that identifies a safe operational zone using the Convex Hull Algorithm from Design and Analysis of Algorithms (DAA). The goal is to compute the smallest convex boundary around a random set of GPS-like points and then simulate a drone navigating inside or outside the safe zone.

The project features two major components:

Matplotlib Visualization – Shows the points and the computed Convex Hull polygon.

Pygame Simulation – A real-time drone movement interface using keyboard controls. The drone color and status change based on whether it is inside or outside the safe zone.

This project is ideal for academic submissions, DAA practical implementation, and visualization-based algorithm learning.

✨ Features

✔ Convex Hull computation using Divide & Conquer

✔ Matplotlib-based static visualization

✔ Pygame-based dynamic simulation

✔ Keyboard-controlled drone movement

Arrow keys to move UP / DOWN / LEFT / RIGHT

✔ Real-time Safe Zone Alert

🟢 Inside safe zone → “INSIDE SAFE ZONE”

🔴 Outside safe zone → “OUTSIDE – ALERT!”

✔ Random GPS-like point generation

✔ Point-in-Polygon detection

✔ Colored markers for inside & outside points

🛠 Technologies Used

Component	Technology

Programming Language	Python 3.13 / 3.14

Algorithm	Convex Hull (Divide & Conquer)

Visualization	Matplotlib

Simulation	Pygame-CE

Geometry Logic	Point-in-Polygon (Ray Casting Method)
