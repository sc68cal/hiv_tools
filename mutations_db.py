import csv
from operator import itemgetter, attrgetter
from classes import *
import re
reader = csv.reader(open("/Users/scollins/Programming/Python/CoreITPro/BTech/seqdata/data/Sheet3-Table 1.csv"))
data = sorted([ [row[1],row[0],row[2],row[3],row[5],row[6]] for row in reader ],key=itemgetter(0))
d_map = {}
read_map = {}
for row in data[:-1]:
	try:
		d_map[row[0]][row[1]] = row[4:]
	except KeyError:
		d_map[row[0]] = {row[1]:row[4:]}
	
	read_map[row[0]] = row[2:4]

for i in sorted(d_map.keys()):
	read_start = int(read_map[i][0])
	read_end = int(read_map[i][1])

	tmp_name = re.search('^A\d{1,4}',i).group(0)
	
	v_name = re.search('R\d{2}',i)

	if v_name != None:
		tmp_name += "-" + v_name.group(0)


	try:
		tmp_visit = Visit.select(Visit.q.name==tmp_name).getOne()
	except SQLObjectNotFound:
		print "Visit not found for ", tmp_name
		continue
	
	tmp_mutation = Mutation(visit=tmp_visit,readStart=int(read_map[i][0]),readEnd=int(read_map[i][1]))
	for key in d_map[i]:
		tmp_mutation_pos = MutationPosition(mutation=tmp_mutation,position=int(key),refNt=d_map[i][key][0],mutNt=d_map[i][key][1])


'''
	try:

		tmp_visit = Visit.select(Visit.q.name=="
'''
'''
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
'''
