# estimating pi using Nilakantha series
def pi_calc(n):
	pi = 3
	# sign = sign*-1 to alternative
	sign = 1
	for i in range(2, n, 2):
		pi += sign * (4 / (i * (i + 1) * (i + 2)))
		sign *= -1
	return pi

print(pi_calc(10))
print(pi_calc(5))