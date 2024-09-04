# persistence_curve.py

import numpy as np
import matplotlib.pyplot as plt

def generating_function_lifespan(birth, death, epsilon):
    """Generating function for 1D features that returns the lifespan (death - birth) if the interval is in range."""
    return death - birth if birth <= epsilon <= death else 0

def summary_statistic_sum(values):
    """Summary statistic that returns the sum of values."""
    return np.sum(values)

def summary_statistic_mean(values):
    """Summary statistic that returns the mean of values."""
    return np.mean(values) if values else 0

def compute_persistence_curve(persistence_intervals, epsilon_values, generating_function, summary_statistic):
    """
    Compute the persistence curve based on the given generating function and summary statistic.
    
    Args:
        persistence_intervals (ndarray): Array of persistence intervals.
        epsilon_values (list or ndarray): Array of filtration parameters.
        generating_function (function): Function to apply to each interval.
        summary_statistic (function): Function to aggregate the values.
        
    Returns:
        persistence_curve (list): List of persistence curve values.
    """
    persistence_curve = []
    
    for epsilon in epsilon_values:
        # Apply the generating function to each interval in the persistence diagram
        values = [generating_function(b, d, epsilon) for b, d in persistence_intervals]
        
        # Apply the summary statistic to aggregate the results
        persistence_value = summary_statistic(values)
        
        # Store the result
        persistence_curve.append(persistence_value)
    
    return persistence_curve

def plot_persistence_curve(epsilon_values, persistence_curve_sum, persistence_curve_mean, folder_path='figs', filename='bettifunction'):
    """Plot and save the persistence curve."""
    plt.figure(figsize=(8, 6))
    plt.step(epsilon_values, persistence_curve_sum, where='post', color='blue', linewidth=4, linestyle='--', label='Sum')
    plt.step(epsilon_values, persistence_curve_mean, where='post', color='lightblue', linewidth=4, label='Mean')
    plt.scatter(epsilon_values, persistence_curve_sum, color='blue')  # Plot the key points for sum
    plt.scatter(epsilon_values, persistence_curve_mean, color='lightblue')  # Plot the key points for mean
    plt.xlabel('Filtration Parameter $\epsilon$')
    plt.ylabel('Persistence Curve Value')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    
    # Remove the grid
    plt.grid(False)
    
    # Add a legend
    plt.legend()
    
    # Save and close the plot
    plt.savefig(f'{folder_path}/{filename}.pdf', bbox_inches='tight')
    plt.close()  # Close the plot to avoid display
