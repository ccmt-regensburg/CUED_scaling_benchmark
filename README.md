# Scaling benchmark of CUED
## Short overview over the workflow
One starts the calculations (on SNG) via the benchmark_starter.py, which currently uses a distribution of fat, general and large nodes. 

After these have finished, the slurm_cleanup.py, envoked in the main directory, creates additional slurm.short files in the subdirectories 
in order to reduce the upload size of the files (the full slurm.out as well as time- and frequency_data.dat are ignored by .gitignore due to memory constraints).
Furthermore, a csv is created with the number of _**nodes**_ (not cores!) and the runtime in seconds.

At last, the benchmark_plot.py reads the csv, prints the overall computational time and creates a png and tikz file with the 
relative speedup against number of nodes/cores.
