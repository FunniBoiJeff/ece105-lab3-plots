


Project: Sensor Plots (generate_plots.py)

Overview
--------
This repository contains a small script (generate_plots.py) that generates synthetic temperature sensor data and produces publication-quality visualizations. The script provides reusable functions (generate_data, plot_scatter, plot_histogram) and a main() that composes a 1x3 figure and writes a PNG summary.

Installation
------------
1. Activate the course environment:
   conda activate ece105

2. Install dependencies (choose conda or mamba):
   conda install -n ece105 numpy matplotlib -c conda-forge
   # or
   mamba install -n ece105 numpy matplotlib -c conda-forge

Usage
-----
Run the script from the repository root:

    python generate_plots.py [--seed SEED] [--outdir OUTDIR] [--dpi DPI]

Examples:

    python generate_plots.py --seed 42
    python generate_plots.py --outdir plots --dpi 200

What the script does
--------------------
- generate_data(seed): creates 200 samples each for sensor_a and sensor_b and 200 timestamps.
- plot_scatter / plot_histogram: helper functions that draw onto existing matplotlib Axes.
- main(): generates data, creates a 1x3 subplot (scatter, histogram, boxplot), and saves a single file sensor_analysis.png in the output directory.

Outputs
-------
By default the script writes:

  plots/sensor_analysis.png

(If you pass --outdir the output directory will change accordingly.)

AI tools used and disclosure
---------------------------
This README (and portions of the codebase) were assisted by an AI tool. Please fill this paragraph with any project-specific disclosure text you prefer.

License
-------
(Include your preferred license here.)

Contact
-------
For questions, contact the repository owner or course staff.
