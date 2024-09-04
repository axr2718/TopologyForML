# persistence_image.py

import numpy as np
import matplotlib.pyplot as plt
from persim import PersImage

def compute_persistence_image(persistence_diagram, spread, pixels=[20, 20], weighting_type="linear", kernel_type='gaussian', verbose=False):
    """
    Compute the persistence image for a given persistence diagram.
    
    Args:
        persistence_diagram (ndarray): Array of persistence intervals.
        spread (float): Spread parameter for the Gaussian kernel.
        pixels (list): Number of pixels in the image.
        weighting_type (str): Type of weighting to apply.
        kernel_type (str): Type of kernel to use.
        verbose (bool): Verbosity flag.
        
    Returns:
        persistence_image (ndarray): The persistence image.
    """
    pim = PersImage(spread=spread, pixels=pixels, weighting_type=weighting_type, kernel_type=kernel_type, verbose=verbose)
    persistence_image = pim.transform(persistence_diagram)
    return persistence_image

def plot_persistence_image(persistence_image, spread, folder_path='figs', filename_base='per_image'):
    """
    Plot and save the persistence image.
    
    Args:
        persistence_image (ndarray): The persistence image.
        spread (float): Spread parameter used, for labeling.
        folder_path (str): Path to save the figure.
        filename_base (str): Base filename for the saved figure.
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(persistence_image, cmap='jet', interpolation='nearest')  # Other options: 'copper', 'hsv'
    plt.colorbar(label='Intensity')
    plt.title(f'Spread = {spread}')
    plt.savefig(f'{folder_path}/{filename_base}_{spread}.pdf', bbox_inches='tight')
    plt.close()  # Close the plot to avoid display
