import numpy as np
import math

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape == v2.shape and v1.size != 0 and v2.size != 0 and np.sum(np.abs(v1)) != 0 and np.sum(np.abs(v2)) !=  0:
		dot_product = np.dot(v1,v2)
		v1_l2 = math.sqrt(np.sum(np.square(v1)))
		v2_l2 = math.sqrt(np.sum(np.square(v2)))
		result = dot_product/(v1_l2*v2_l2)
		return result
	pass