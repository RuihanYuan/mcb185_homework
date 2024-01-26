# Author: Lisa

# Import math for later calculation
import math
import sys

# Function for solving quadratic equation
def quad_solver(a, b, c):
	if a == 0:
		sys.exit("Coefficient 'a' can't be 0")
		
	sq_root = b**2 - 4*a*c
	if sq_root >= 0:
		ans1 = ((-b + math.sqrt(sq_root)) / (2 * a))
		ans2 = ((-b - math.sqrt(sq_root)) / (2 * a))
	else:
		sys.exit('error: The equation has complex roots')
		
	if ans1 == ans2:
		return ans1
	else:
		return ans1, ans2
	
	
# Test
ans1,ans2 = quad_solver(13, 40, 5)
print("answer:", ans1,",", ans2)

ans1,ans2 = quad_solver(23, 34, 2)
print("answer:", ans1, ",", ans2)

ans1,ans2 = quad_solver(1, 10, 4)
print("answer:", ans1, ",", ans2)

ans1,ans2 = quad_solver(0, 2, 5)
print("answer:", ans1, ",", ans2)