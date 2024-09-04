# data_generation.py

import numpy as np

def create_number_8(n_lower=10, n_upper=10):
    """Generate points in the shape of the number '8' with added noise."""
    # Generate points for the upper loop
    t_upper = np.linspace(0, 2 * np.pi, n_upper)
    x_upper = 0.6 * np.sin(t_upper) + np.random.normal(0, 0.1, size=t_upper.size)
    y_upper = 0.6 * np.cos(t_upper) + 0.8 + np.random.normal(0, 0.05, size=t_upper.size)
    
    # Generate points for the lower loop
    t_lower = np.linspace(0, 2 * np.pi, n_lower)
    x_lower = np.sin(t_lower) + np.random.normal(0, 0.05, size=t_lower.size)
    y_lower = np.cos(t_lower) - 0.8 + np.random.normal(0, 0.05, size=t_lower.size)
    
    x = np.concatenate((x_upper, x_lower))
    y = np.concatenate((y_upper, y_lower))
    
    return np.column_stack((x, y))

def create_number_9(n_points=35):
    """Generate points in the shape of the number '9' with added noise."""
    # Parameters for noise
    noise_level = 0.05  # Adjust this value to increase or decrease noise intensity

    # Create the circular part
    num_points = int(n_points * 0.7)
    t = np.linspace(0, 2 * np.pi, num_points)
    x_circle = np.cos(t) + np.random.normal(0, noise_level, num_points)
    y_circle = np.sin(t) + 1.5 + np.random.normal(0, noise_level, num_points)

    # Create the tail
    tail_length = int(n_points * 0.3)
    x_tail = np.zeros(tail_length) + 0.9 + np.random.normal(0, noise_level, tail_length)
    y_tail = np.linspace(min(y_circle), -1.8, tail_length) + np.random.normal(0, noise_level, tail_length)  # Extending below the circle

    # Combine the circular part with the tail
    x = np.concatenate([x_circle, x_tail])
    y = np.concatenate([y_circle, y_tail])
    
    # Stack into a point cloud
    points = np.vstack((x, y)).T
    return points
