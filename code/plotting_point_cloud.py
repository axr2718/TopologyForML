# plotting_point_cloud.py

import matplotlib.pyplot as plt

def plot_point_cloud_with_balls(points, epsilon, folder_path='figs', label_suffix=''):
    """Plot the point cloud with balls of radius epsilon/2."""
    plt.figure(figsize=(5, 5))
    ball_radius = epsilon / 2
    for point in points:
        circle = plt.Circle(point, ball_radius, color='red', fill=True, alpha=0.5)
        plt.gca().add_patch(circle)
    plt.scatter(points[:, 0], points[:, 1], c='black', marker='o')
    plt.axis('equal')
    plt.axis('off')
    file_name = f'{folder_path}/PointCloud{label_suffix}_epsilon_{epsilon}'
    plt.savefig(f'{file_name}.png')  # Save as PNG
    plt.savefig(f'{file_name}.pdf')  # Save as PDF
    plt.close()  # Close the plot to avoid display

def plot_and_save_points(points, filename, color='red'):
    """Plot and save point cloud."""
    plt.figure(figsize=(6, 6))
    plt.scatter(points[:, 0], points[:, 1], c=color)
    plt.axis('off')  # Turn off the axis
    plt.gca().set_aspect('equal', adjustable='box')  # Keep the aspect ratio of the plot
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()  # Close the plot to avoid display
