import pygame
import random
import matplotlib.pyplot as plt

# ---------------- Convex Hull Functions ---------------- #
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def brute_hull(points):
    n = len(points)
    if n <= 1:
        return points

    hull = []
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            left, right = False, False
            for k in range(n):
                if k == i or k == j:
                    continue
                o = orientation(p1, p2, points[k])
                if o == 1:
                    left = True
                elif o == 2:
                    right = True
            if not (left and right):
                if p1 not in hull:
                    hull.append(p1)
                if p2 not in hull:
                    hull.append(p2)

    hull.sort(key=lambda x: (x[0], x[1]))
    return hull

def divide_and_conquer(points):
    if len(points) <= 5:
        return brute_hull(points)

    points.sort()
    mid = len(points) // 2

    left = divide_and_conquer(points[:mid])
    right = divide_and_conquer(points[mid:])

    return brute_hull(left + right)

# ---------------- Generate Points ---------------- #
random.seed(42)
INSIDE_COUNT = 20
OUTSIDE_COUNT = 10

# All base points to compute safe zone
all_points = [(random.randint(100, 500), random.randint(100, 500)) for _ in range(INSIDE_COUNT)]

# Outside points
outside_points = [(random.randint(20, 580), random.randint(20, 580)) for _ in range(OUTSIDE_COUNT)]

# Compute convex hull (safe zone polygon)
hull = divide_and_conquer(all_points)

# ---------------- Matplotlib Visualization ---------------- #
plt.figure(figsize=(6, 6))
x, y = zip(*all_points)
plt.scatter(x, y, color='yellow', label="Inside Points")

ox, oy = zip(*outside_points)
plt.scatter(ox, oy, color='blue', label="Outside Points")

hx, hy = zip(*(hull + [hull[0]]))
plt.plot(hx, hy, color='red', linewidth=2, label="Safe Zone (Convex Hull)")

plt.title("Convex Hull Safe Zone - Drone Surveillance")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()

# ---------------- Pygame Simulation ---------------- #
pygame.init()

WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Surveillance - Convex Hull Safe Zone (pygame-ce)")

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
YELLOW = (240, 220, 0)
RED = (255, 60, 60)
GREEN = (0, 200, 0)

# Drone
drone_pos = [300, 300]
drone_speed = 5
drone_radius = 8

# Point-In-Polygon (Ray Casting)
def point_in_polygon(point, poly):
    x, y = point
    inside = False
    p1x, p1y = poly[0]

    for i in range(len(poly) + 1):
        p2x, p2y = poly[i % len(poly)]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    else:
                        xinters = p1x

                    if x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    win.fill(WHITE)

    # Draw inside points
    for p in all_points:
        pygame.draw.circle(win, YELLOW, p, 5)

    # Draw outside points
    for p in outside_points:
        pygame.draw.circle(win, BLUE, p, 5)

    # Draw convex hull polygon
    if len(hull) > 1:
        pygame.draw.polygon(win, RED, hull, 2)

    # Keyboard control for drone
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        drone_pos[0] -= drone_speed
    if keys[pygame.K_RIGHT]:
        drone_pos[0] += drone_speed
    if keys[pygame.K_UP]:
        drone_pos[1] -= drone_speed
    if keys[pygame.K_DOWN]:
        drone_pos[1] += drone_speed

    # Determine safe zone status
    safe = point_in_polygon(drone_pos, hull)
    drone_color = GREEN if safe else RED

    pygame.draw.circle(win, drone_color, drone_pos, drone_radius)

    # Text status
    font = pygame.font.Font(None, 32)
    status = "INSIDE SAFE ZONE" if safe else "OUTSIDE - ALERT!"
    text = font.render(status, True, (0, 0, 0))
    win.blit(text, (20, 20))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
