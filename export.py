from classes import *
from re import escape
import datetime

fields = [ drug.name for drug in Drug.select() ] 

race = {"BLACK/AA":1,"MULTIPLE":2,"WHITE":3,"HISPANIC":4,
"AFRICAN":5,"UNKNOWN":6,"ND":7,"AA/NAT AM":8}

print "Patient ID,", "Visit ID,", "Race,", "Gender,", "Age,", "DSG,", "CD4,", "Viral,",
for field in fields:
	print field,",",
print ""


for patient in Patient.select():
	for visit in patient.visits:
		print patient.name,",",

		if visit.name.find("R") != -1:
			print visit.name[visit.name.find("R"):],
		else:
			print "R00",
		
		print ",",
		
		if not len(patient.race):
			print "NA,",
		else:
			print race[patient.race.upper()],",",
			
		if not len(patient.gender):
			print "NA",",",
		else:
			if patient.gender.upper() == "M":
				print 1,",",
			else:
				print 0,",",
		if not patient.yearOfBirth:
			print "NA",",",
		else:
			print datetime.datetime.today().year - patient.yearOfBirth,",",

		if not visit.dsg:
			print "NA,",
		else:
			print visit.dsg,",",
		
		if not visit.cd4: 
			print "NA,",
		else:
			print visit.cd4.replace(",",""),",", 
		if not visit.viral:
			print "NA,",
		else:
			print visit.viral.replace(",",""),",",

		drugs_used = [ drug.name for drug in visit.drugs ]

		for field in fields:
			try:
				if drugs_used.index(field) >= 0:
					print 1,",",
			except ValueError: 
				print 0,",",

		print ""
