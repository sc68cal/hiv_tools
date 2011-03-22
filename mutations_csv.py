import csv
from operator import itemgetter, attrgetter
import sys

reader = csv.reader(open(sys.argv[1]))
data = sorted([ [row[1],row[0],row[2],row[3],row[5],row[6]] 
				for row in reader ],key=itemgetter(0) )
positions = []
d_map = {}
read_map = {}
for row in data[:-1]:
	try:
		positions.index(int(row[1]))
	except ValueError:
		positions.append(int(row[1]))
	try:
		d_map[row[0]][row[1]] = row[4:]
	except KeyError:
		d_map[row[0]] = {row[1]:row[4:]}
	
	read_map[row[0]] = row[2:4]


positions.sort()

print "Name,",
for pos in positions:
	print pos,",",
print ""

for i in sorted(d_map.keys()):
	print i,",",
	read_start = int(read_map[i][0])
	read_end = int(read_map[i][1])
	for pos in positions:
		try:

			mutation_pos =  d_map[i][str(pos)][1]


			if pos >= read_start and pos <= read_end:
				if d_map[i][str(pos)][0] ==  mutation_pos:
					print 0,",",
				else:
					if mutation_pos == "A":
						print 1,',',
					elif mutation_pos == 'C':
						print 2,',',
					elif mutation_pos == "G":
						print 3,',',
					elif mutation_pos == "T":
						print 4,',',

			else:
				print -9,",",

		except KeyError:
			if pos >= read_start and pos <= read_end:
				print 0,",",
			else:

				print -9,",",
	print ""
