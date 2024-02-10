import random

zerogames = 0
total_games = 10000000
total_score = 0

for i in range(total_games):
	score = 0
	for num in range(2, 13):
		#print(num)
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == num:
			score += num
		if score == 0:
			zerogames +=1
			

			total_score += score
			
			
print(zerogames / total_games)
print(total_score / total_games)