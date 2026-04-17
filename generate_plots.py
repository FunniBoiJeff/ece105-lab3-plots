"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np

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



