# plotting_persistence_diagram.py

import matplotlib.pyplot as plt
import gudhi as gd

def plot_persistence_diagram(persistence, folder_path='figs', label_suffix=''):
    """Plot and save the persistence diagram."""
    plt.figure()
    gd.plot_persistence_diagram(persistence)
    handles = [
        plt.Line2D([0], [0], color='red', lw=2, label='0-dimension'),
        plt.Line2D([0], [0], color='dodgerblue', lw=2, label='1-dimension')
    ]
    plt.legend(handles=handles, loc='upper right', frameon=False)
    file_name = f'{folder_path}/PersistenceDiagram{label_suffix}'
    plt.savefig(f'{file_name}.png', bbox_inches='tight')  # Save as PNG
    plt.savefig(f'{file_name}.svg', bbox_inches='tight')  # Save as SVG
    plt.close()  # Close the plot to avoid display
