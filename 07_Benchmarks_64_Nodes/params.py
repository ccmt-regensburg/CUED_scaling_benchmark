# Input parameters for SBE.py
import numpy as np


class params:
	# System parameters
	#########################################################################
	a                   = 8.308                  # Lattice spacing in atomic units (4.395 A)
	e_fermi             = 0.2                    # Fermi energy in eV
	temperature         = 0.03                    # Temperature in eV

	# Model Hamiltonian parameters
	# Brillouin zone parameters
	##########################################################################
	# Type of Brillouin zone
	# 'hexagon' for full hexagonal BZ, 'rectangle' for rectangle with adjustable size
	BZ_type = 'hexagon'

	# hexagonal BZ parameters
	Nk1                 = 1800                     # Number of kpoints in each of the paths
	Nk2                 = 180                     # Number of paths

	# Driving field parameters
	##########################################################################
	align               = 'M'
	E0                  = 3.00                   # Pulse amplitude (MV/cm)
	f                   = 25.0                   # Pulse frequency (THz)
	chirp               = -1.25                   # Pulse chirp ratio (chirp = c/w) (THz)
	sigma               = 90.0                   # Gaussian pulse width (femtoseconds)
	phase               = 0

	# Time scales (all units in femtoseconds)
	##########################################################################
	T1    = 1000                                 # Phenomenological diagonal damping time
	T2    = 10                                    # Phenomenological polarization damping time
	t0    = -1000                                 # Start time *pulse centered @ t=0, use t0 << 0
	dt    = 5e-3                                  # Time step

	# Flags for testing and features
	##########################################################################

	gauge                   = 'velocity'           # Gauge of the system
	solver                  = '2band'
	fourier_window_function = 'gaussian'
	user_out                = True
	save_latex_pdf          = False
	parallelize_over_points = True
