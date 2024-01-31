
import math

# poisson probability


def factorial(num):
	if num == 0:
		return 1
	fac = 1
	for i in range(1, num + 1):
		fac *= i
	return fac

def poisson_prob(n, k):
	prob = (n**k * math.exp(-n)) / factorial(k)
	return prob

print(poisson_prob(5, 3))