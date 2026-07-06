# import libraries
import numpy as np
import matplotlib.pyplot as plt

# functiom that calculate the reflect points
def reflect_points(angle_deg, bounces=20):

    #initial angle
    start_angle = np.radians(0)
    x0 = np.cos(start_angle)
    y0 = np.sin(start_angle)

    # initial direction
    theta = np.radians(angle_deg)
    vx = np.cos(theta)
    vy = np.sin(theta)

    # initial points
    points = [(x0, y0)]
    
    # find the times t that ball reflected from circel
    for i in range(bounces):
        # equation of circle:
        # (x+t*vx)^2 + (y+t*vy)^2 = 1
        # (x^2+y^2-1) + t^2*(vx^2+vy^2) + t*2*(x*vx+y*vy) = 0
        # a*t^2 + b*t + c

        #solve the circle's equation
        a = vx**2 + vy**2
        b = 2*(x0*vx + y0*vy)
        c = x0**2 + y0**2 - 1
        delta = b**2 - 4*a*c
        if delta < 0:
            break

        # time for near point
        t = (-b-np.sqrt(delta))/(2*a)

        # add the new points to lisd
        x = x0 + vx*t
        y = y0 + vy*t
        points.append((x, y))

        # normalization the new poins
        nx = x / np.sqrt(x**2 + y**2)
        ny = y / np.sqrt(x**2 + y**2)

        # velocity and normal vector
        v = np.array([vx, vy])
        n = np.array([nx, ny])

        # reflected velocity
        v_new = v - 2*np.dot(v, n)*n
        
        # adjusting points and velocity for next step
        vx, vy = v_new[0], v_new[1]
        x0, y0 = x, y
    
    return points

# function for plot trajectory
def plot_trajectory(angle_deg, bounces=20, ax = None, color='b', label=None):

    # get points from the previous function
    points = reflect_points(angle_deg, bounces)
    x_values = [i[0] for i in points]
    y_values = [i[1] for i in points]

    # making figure
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # making circle for background
    circle = plt.Circle((0, 0), 1, fill=False, edgecolor='black', lw=1, alpha=0.7)
    ax.add_patch(circle)

    # making the lines
    for i in range(len(points)-1):
        ax.plot([x_values[i], x_values[i+1]], [y_values[i], y_values[i+1]], color=color, lw=1, alpha=0.7)

    # all points exeps start point
    ax.scatter(x_values[1:], y_values[1:], s=30, color=color, alpha=0.7)

    # start point
    ax.scatter(x_values[0], y_values[0], color='red', marker='*', s=150, alpha=1, label='Start')

    # circle's center
    ax.scatter(0, 0, color='black', s=150, marker='*', alpha=1, label='Center')

    #adjusting axes
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.5)
    if label:
        ax.set_title(label)
    
    return points

# main function

if __name__ == "__main__":
    bounces = 20
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    #20 degree
    points_20_degree = plot_trajectory(20, bounces, ax=axes[0], color='blue')
    axes[0].set_title('20 bounces, start_angle = 20 degree')

    #21 degree
    points_21_degree = plot_trajectory(21, bounces, ax=axes[1], color='green')
    axes[1].set_title('20 bounces, start_angle = 21 degree')

    axes[0].legend(loc='upper right')
    axes[1].legend(loc='upper right')

    plt.tight_layout()
    plt.show()
