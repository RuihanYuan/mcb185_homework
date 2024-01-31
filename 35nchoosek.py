# function for n choose k calculation
def factorial_cal(n, k):
	assert(n >= k)

	# initialize factorial variables
	fac1 = 1
	fac2 = 1
	fac_n_k = 1

	for i in range(1, n + 1):
		# for n!
		fac1 *= i
		# for k !
		if i <= k:
			fac2 *= i
		# (n - k)!
		if i <= n - k:
			fac_n_k *= i
	ans = fac1 / (fac2 * fac_n_k)
	return ans
				
print(factorial_cal(6, 4))
print(factorial_cal(10, 4))
print(factorial_cal(6, 2))