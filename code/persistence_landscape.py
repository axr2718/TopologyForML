# persistence_landscape.py

import numpy as np
import matplotlib.pyplot as plt
from persim import PersLandscapeApprox

def compute_persistence_landscape(persistence_diagram, homology_degree=1, start=0, stop=2, num_steps=1000):
    """
    Compute the persistence landscape for a given persistence diagram.
    
    Args:
        persistence_diagram (ndarray): Array of persistence intervals.
        homology_degree (int): Homology degree to compute the landscape for.
        start (float): Start of the filtration parameter.
        stop (float): End of the filtration parameter.
        num_steps (int): Number of steps in the filtration parameter.
        
    Returns:
        landscape (PersLandscapeApprox): The persistence landscape object.
    """
    # Ensure persistence_diagram is a numpy array
    persistence_diagram = np.array(persistence_diagram)
    # Create the persistence landscape object
    landscape = PersLandscapeApprox(dgms=[persistence_diagram], hom_deg=homology_degree, start=start, stop=stop, num_steps=num_steps)
    return landscape

def plot_persistence_landscape(landscape, folder_path='figs', filename='landscape'):
    """
    Plot and save the persistence landscape.
    
    Args:
        landscape (PersLandscapeApprox): The persistence landscape object.
        folder_path (str): Path to save the figure.
        filename (str): Base filename for the saved figure.
    """
    plt.figure(figsize=(8, 6))
    epsilon_thresholds = np.linspace(landscape.start, landscape.stop, landscape.num_steps)
    
    for i in range(len(landscape.values)):
        plt.plot(epsilon_thresholds, landscape.values[i], label=f'$\lambda^{{{i + 1}}}$', linewidth=4)
    
    plt.xlabel('Threshold $\epsilon$')
    plt.ylabel('Persistence Landscape')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    # Add a legend to distinguish between layers
    plt.legend()
    
    # Remove the grid
    plt.grid(False)
    plt.savefig(f'{folder_path}/{filename}.svg', bbox_inches='tight')  # Save as SVG
    plt.savefig(f'{folder_path}/{filename}.pdf', bbox_inches='tight')  # Save as PDF
    plt.close()  # Close the plot to avoid display
