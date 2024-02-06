#author: Lisa Yuan, Francessca Asuncion
def pi_cal(n):
	for i in range(n):
		pi = 4 * (-1)**(i) / (2 * i + 1)
	return pi
	
print(pi_cal(5))