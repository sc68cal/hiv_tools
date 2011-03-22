from itertools import *
from classes import *
import MySQLdb


conn = MySQLdb.connect(host='localhost',user='root',passwd='root',port=8889,db='mydb')

c = conn.cursor()

c.execute("SELECT DISTINCT position \
		FROM mutation_position ORDER BY \
		position asc")

data = {}

positions = [pos[0] for pos in c.fetchall()]

for i in Mutation.select():
	data[i.visit.name] = [ mut for mut in MutationPosition.selectBy(mutation=i.id).orderBy("+position") ]


# Practice, just find the most mutations in all the samples

longest = 0
name = ""

for key in data:
	i = len(data[key])
	if i > longest:
		longest = i
		name = key


print longest, key


# OK - find the largest XXX contiguous XXX block of mutations


'''
for i in range(2,maxlen):
	for per in product(range(1,4),repeat=i):

'''
