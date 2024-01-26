# Import library
import sys


# Function for calculating accuracy and F1 score
def accuracy_calc(tp,tn,fp,fn):
	total = tp + tn + fp + fn
	
	if total != 0:
		accuracy = (tp + tn) / total
	else:
		sys.exit("denominator can't be 0")
		
	if (tp+fp) !=0:
		precision = tp / (tp + fp)
	else:
		sys.exit("denominator can't be 0")
		
	if (tp+fn) != 0:
		recall = tp / (tp + fn)
	else:
		sys.exit("denominator can't be 0")
		
	if (precision + recall) != 0:
		F1 = (2 * precision * recall) / (precision + recall)
	else:
		sys.exit("denominator can't be 0")
		
	return accuracy,F1
	

# Test
print("accuracy, F1 score:",accuracy_calc(20,40,50,30))
print("accuracy, F1 score:",accuracy_calc(50,25,60,25))
print("accuracy, F1 score:",accuracy_calc(15,30,20,60))
print("accuracy, F1 score:",accuracy_calc(15,30,0,0))