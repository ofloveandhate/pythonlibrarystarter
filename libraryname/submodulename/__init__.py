""" Submodulename

This code provides a submodule for Libraryname.  

It generates data.

Contains the following functions:

	* generate_data

"""

import numpy


def generate_data():
	"""
	generates some data
	"""
	return numpy.random.exponential(scale=0.1,size=[3, 5])
