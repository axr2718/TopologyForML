# plotting_persistence_barcode.py

import matplotlib.pyplot as plt
import numpy as np
import gudhi as gd

def plot_persistence_barcode(persistence, epsilon, max_dist, folder_path='figs', label_suffix=''):
    """Plot and save the persistence barcode."""
    plt.figure()
    gd.plot_persistence_barcode(persistence)
    ax = plt.gca()
    max_x = max(epsilon, max_dist / 2)
    ax.set_xlim(0, max_x)
    x_ticks = np.arange(0, max_x + 0.4, 0.4)
    ax.set_xticks(x_ticks)
    handles = [
        plt.Line2D([0], [0], color='red', lw=2, label='0-dimension'),
        plt.Line2D([0], [0], color='dodgerblue', lw=2, label='1-dimension')
    ]
    plt.legend(handles=handles, loc='center right', frameon=False)
    file_name = f'{folder_path}/PersistenceBarcode{label_suffix}_epsilon_{np.round(epsilon, 1)}'
    plt.savefig(f'{file_name}.png', bbox_inches='tight')  # Save as PNG
    plt.savefig(f'{file_name}.svg', bbox_inches='tight')  # Save as SVG
    plt.close()  # Close the plot to avoid display
