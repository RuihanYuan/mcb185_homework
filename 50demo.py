tax = ('Homo', 'sapiens', 9606)
print(tax)

print(tax[0])
print(tax[::-1]) #from last to first

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)

nts = 'ATCG'
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for nt, name in zip(nts, names):
	print(nt, name)
	#zip(): combine two list/tuples side by side
	#could zip tuple with list
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	#enumerate(): count the index and combining with the corresponding element
	
nts1 = ['A', 'T', 'C']
nts1[2] = 'G'
nucleotides = nts1
nucleotides.append('C')
nucleotides.sort(reverse=True)
print(nts, nucleotides)

#convert str into list
alph = 'ACDEFGHIJKLMNOPQRSVM'
print(alph)
aas = list(alph)
print(aas)

#delimiter: space
text = 'good day   to you'
words = text.split()
print(words)

#delimiter: comma
line = '1.41,2.72,3.14'
print(line.split(','))

#delimiter: tab
l1 = '1	3	4	5'
print(l1.split('\t'))

#join by -
s = '-'.join(aas)
print(s)
#join w/o spaces
s = ''.join(aas)
print(s)

#index() return error if can't find and quit the program
print('index G?', alph.index('G'))
#print('index z?', alph.index('z'))

#find() return -1 if can't find
print('find G?', alph.find('G'))
print('find z?', alph.find('z'))

#pre-define thing(what to search)
thing = 'A'
												#list
if thing in alph: 
	idx = alph.index(thing)
print(idx, thing)
