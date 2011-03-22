#!/usr/bin/env python
import re
import sys

fp = open(sys.argv[1])

barcodes = (
		"ACACGACGACT",
		"ACACGTAGTAT",
		"ACACTACTCGT",
		"ACGACACGTAT",
		"ACGAGTAGACT",
		"ACGCGTCTAGT",
		"ACGTACACACT",
		"ACGTACTGTGT",
		"ACGTAGATCGT",
		"ACTACGTCTCT",
		"ACTATACGAGT",
		"ACTCGCGTCGT",
)

data = ""

# First, take the whole file and concatenate it into a single string
for line in fp:
	data += line

# Split the lines up based on the token that indicates a new record
data = data.split('>')[1:]

for i in range(0,len(data)):
	newline = data[i].find('\n')
	seq = data[i][newline:].replace('\n','')
	data[i] = [data[i][:newline],seq]

files = {}
stats = {}
for bar in barcodes:
	files[bar] = open(bar+'.db',"w")
	stats[bar] = 0

for dp in data:
	for barcode in barcodes:
		needle = re.compile("^"+barcode)
		if needle.match(dp[1]):
			files[barcode].write(">"+dp[0]+"\n"+dp[1]+"\n")
			stats[barcode] += 1
for barcode in barcodes:
	print barcode, "matches", stats[barcode], 'items'

