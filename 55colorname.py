#rgb color
#calculate the difference of the colors(dist between R,G,B channels)
#check if this is closer to red, green or blue(any color fromt the data/tsv files)
#ex: abs(r1-r_ref)+abs(g1-g_ref)+abs(b1-b_ref), and find the minimum dist, compare through the list of dif
#spilt the file by recognizing the comma(tsv)

import sys

def dtc(P,Q):
	d = 0
	d += abs(P[0] - Q[0])
	d += abs(P[1] - Q[1])
	d += abs(P[2] - Q[2])
	return d

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

colors = []
with open(colorfile) as fp:
	for line in fp:
		col = line.split('\t')
		color = col[0]
		rgb = col[2].split(',')
		r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
		dist = dtc((R, G, B), (r, g, b))
		colors.append((dist, color))
			
min_dist,closest_color = colors[0]
for dis, color in colors[1:]:
	if dis < min_dist:
		min_dist = dis
		closest_color = color
	
print(f'The closest color is {closest_color}')
print(min_dist)