import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X)
	
	Y = np.array(y).reshape(-1,1)
	x_t = X.T
	theta = np.linalg.inv(x_t.dot(X)).dot(x_t).dot(Y)
	theta = np.round(theta,4).flatten().tolist()
	return theta