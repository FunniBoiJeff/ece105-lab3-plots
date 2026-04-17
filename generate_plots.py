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
import os
import argparse

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


def plot_histogram(sensor_a, sensor_b, ax, bins=30, density=False):
    """Plot overlaid histograms for two sensors on the provided Axes.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Readings from sensor A.
    sensor_b : array_like, shape (n,)
        Readings from sensor B.
    ax : matplotlib.axes.Axes
        Axes to draw the histograms on. Modified in place.
    bins : int or sequence, optional
        Number of histogram bins or bin edges to use (default: 30).
    density : bool, optional
        If True, plot probability density instead of counts (default: False).

    Returns
    -------
    None
        The function updates the provided Axes and returns None.

    Notes
    -----
    This mirrors the notebook: histograms are overlaid with alpha=0.5,
    mean values are indicated by dashed vertical lines, and a legend,
    axis labels and title are added.
    """
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    ax.hist(sensor_a, bins=bins, alpha=0.5, label='Sensor A', density=density, color='C0')
    ax.hist(sensor_b, bins=bins, alpha=0.5, label='Sensor B', density=density, color='C1')

    # Mean lines
    ax.axvline(np.mean(sensor_a), color='C0', linestyle='dashed', linewidth=1, label='Mean A')
    ax.axvline(np.mean(sensor_b), color='C1', linestyle='dashed', linewidth=1, label='Mean B')

    ax.set_xlabel('Temperature')
    ax.set_ylabel('Density' if density else 'Frequency')
    ax.set_title('Histogram of Sensor Temperatures')
    ax.legend()
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.3)

    return None


def main(seed=None, outdir='plots', dpi=150):
    """Generate data, compose a 1x3 figure, and save as a single PNG.

    Parameters
    ----------
    seed : int or None
        Seed passed to :func:`generate_data` for reproducible output. If None,
        non-deterministic random draws are used.
    outdir : str
        Directory where the output PNG will be written. Created if it does not exist.
    dpi : int
        Resolution (dots per inch) used when saving the PNG file.

    Returns
    -------
    None
        Writes a single file ``sensor_analysis.png`` into ``outdir`` containing
        three subplots: scatter, histogram, and boxplot (left-to-right).
    """
    sensor_a, sensor_b, timestamps = generate_data(seed)

    os.makedirs(outdir, exist_ok=True)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    ax0, ax1, ax2 = axes.ravel()

    # Left: scatter
    plot_scatter(sensor_a, sensor_b, timestamps, ax0)

    # Middle: histogram
    plot_histogram(sensor_a, sensor_b, ax1)

    # Right: boxplot
    ax2.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'], patch_artist=True)
    ax2.set_ylabel('Temperature')
    ax2.set_title('Sensor temperature summary (boxplot)')
    ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.3)

    fig.tight_layout()

    out_path = os.path.join(outdir, 'sensor_analysis.png')
    fig.savefig(out_path, dpi=dpi, bbox_inches='tight')
    plt.close(fig)

    print(f"Saved: {out_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate sensor plots and save as PNGs')
    parser.add_argument('--seed', type=int, default=None, help='RNG seed for data generation')
    parser.add_argument('--outdir', type=str, default='plots', help='Output directory for PNG files')
    parser.add_argument('--dpi', type=int, default=150, help='DPI for saved PNG files')
    args = parser.parse_args()
    main(seed=args.seed, outdir=args.outdir, dpi=args.dpi)


# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.
