"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed=None):
    """Generate synthetic sensor temperature data.

    Parameters
    ----------
    seed : int or None
        Seed for the random number generator. If None, a non-deterministic
        generator is used.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape (200,) containing samples from N(loc=25.0, scale=3.0).
    sensor_b : numpy.ndarray
        Array of shape (200,) containing samples from N(loc=27.0, scale=4.5).
    timestamps : numpy.ndarray
        Array of shape (200,) of timestamps sampled uniformly on [0, 10).

    Notes
    -----
    The returned arrays match the parameters used in the original notebook
    (n=200, sensor means and scales as specified). The function uses
    numpy.random.default_rng for reproducible draws when a seed is provided.
    """
    rng = np.random.default_rng(seed)
    n = 200
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n)
    timestamps = rng.uniform(0, 10, size=n)
    return sensor_a, sensor_b, timestamps



def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a scatter plot of two sensors against timestamps on an Axes.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Readings from sensor A.
    sensor_b : array_like, shape (n,)
        Readings from sensor B.
    timestamps : array_like, shape (n,)
        Time values corresponding to each reading (same length as sensor arrays).
    ax : matplotlib.axes.Axes
        The Axes object to draw onto. This function modifies ``ax`` in place.

    Returns
    -------
    None
        The function updates the provided Axes and returns None.

    Notes
    -----
    The plotting style matches the notebook: semi-transparent colored points
    (C0 for Sensor A, C1 for Sensor B), marker size 40, alpha=0.7, a legend,
    axis labels, a title, and a subtle grid.
    """
    # Ensure inputs are numpy arrays for consistent indexing/behavior
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)
    timestamps = np.asarray(timestamps)

    ax.scatter(timestamps, sensor_a, s=40, c='C0', alpha=0.7, label='Sensor A')
    ax.scatter(timestamps, sensor_b, s=40, c='C1', alpha=0.7, label='Sensor B')

    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature')
    ax.set_title('Sensor readings vs Time (scatter)')
    ax.legend()
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.4)

    return None


