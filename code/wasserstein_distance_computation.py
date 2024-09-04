# wasserstein_distance_computation.py

import numpy as np
import matplotlib.pyplot as plt
import gudhi as gd
from gudhi.wasserstein import wasserstein_distance

def compute_persistence_diagram(points, max_edge_length=2, max_dimension=2):
    """
    Compute the persistence diagram for a given point cloud.
    
    Args:
        points (ndarray): Point cloud data.
        max_edge_length (float): Maximum edge length for Rips complex.
        max_dimension (int): Maximum dimension for Rips complex.
        
    Returns:
        persistence_intervals (ndarray): Array of persistence intervals in dimension 1.
    """
    rips_complex = gd.RipsComplex(points=points, max_edge_length=max_edge_length)
    simplex_tree = rips_complex.create_simplex_tree(max_dimension=max_dimension)
    simplex_tree.persistence()
    return simplex_tree.persistence_intervals_in_dimension(1)  # 1-dimensional features (loops)

def compute_wasserstein_distance_between_diagrams(persistence_diagram_1, persistence_diagram_2, order=2, internal_p=1):
    """
    Compute the Wasserstein distance between two persistence diagrams.
    
    Args:
        persistence_diagram_1 (ndarray): First persistence diagram.
        persistence_diagram_2 (ndarray): Second persistence diagram.
        order (int): Order of the Wasserstein distance.
        internal_p (int): Internal p for the distance.
        
    Returns:
        distance (float): The Wasserstein distance.
    """
    return wasserstein_distance(persistence_diagram_1, persistence_diagram_2, order=order, internal_p=internal_p)

def plot_persistence_diagrams(persistence_diagram_1, persistence_diagram_2, label_1='PD of "8"', label_2='PD of "9"', folder_path='figs', filename='pd_8_and_9'):
    """
    Plot two persistence diagrams on the same plot and save.
    
    Args:
        persistence_diagram_1 (ndarray): First persistence diagram.
        persistence_diagram_2 (ndarray): Second persistence diagram.
        label_1 (str): Label for the first diagram.
        label_2 (str): Label for the second diagram.
        folder_path (str): Path to save the figure.
        filename (str): Base filename for the saved figure.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(persistence_diagram_1[:, 0], persistence_diagram_1[:, 1], c='red', label=label_1, s=80)
    plt.scatter(persistence_diagram_2[:, 0], persistence_diagram_2[:, 1], c='blue', label=label_2, s=80)
    max_val = max(np.max(persistence_diagram_1[:, 1]), np.max(persistence_diagram_2[:, 1]))
    plt.plot([0, max_val], [0, max_val], 'k--')  # Diagonal line y = x
    plt.xlabel("Birth")
    plt.ylabel("Death")
    plt.legend(loc='lower right') 
    plt.savefig(f'{folder_path}/{filename}.svg')
    plt.close()  # Close the plot to avoid display
