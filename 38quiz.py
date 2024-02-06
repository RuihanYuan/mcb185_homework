#author: Lisa Yuan, Francessca Asuncion


def pi_cal(n):
	for i in range(n):
		pi = 4 * (-1)**(i) / (2 * i + 1)
	return pi
	


def pi_calc(n):
	pi = 3
	# sign = sign*-1 to alternative
	sign = 1
	for i in range(2, n, 2):
		pi += sign * (4 / (i * (i + 1) * (i + 2)))
		sign *= -1
	return pi
	
for i in range(1,100):
	print(pi_cal(i),pi_calc(i))