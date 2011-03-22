import csv
from classes import *
from datetime import datetime
import sys

def parseDrugUse(row,patient_visit):

	druglist = {}
	csv_columns = ["Marajuana","Cocaine","Heroin","Methamphetamines",\
	"Ritalin","Barbituates","PCP","Other","Narcotics","Benzodiazepines","Ecstacy"]
	
	for drug in list(Drug.select()):
		druglist[drug.name] = drug.id

	if row[80].find("t") != -1:
		tmp_drug_use = DrugUsed(visit=patient_visit,drug=Drug.get(druglist["Tobacco"]))
		if row[81] != "current":
			tmp_drug_use.dateStopped = row[81]
	if row[80].find('a') != -1:
		tmp_drug_use = DrugUsed(visit=patient_visit,drug=Drug.get(druglist["Alcohol"]))
		if row[82] != "current":
			tmp_drug_use.dateStopped = row[82]
	i=0
	for column in row[86:96]:
		if column.upper() == "X":
			tmp_drug_use = DrugUsed(visit=patient_visit,drug=Drug.get(druglist[csv_columns[i]]))
		elif i==7 and len(column) > 2 and column != "no drug use" and column != "missing form":
			try:
				tmp_drug = Drug.select(Drug.q.name==column).getOne()
			except SQLObjectNotFound:
				tmp_drug = Drug(name=column)
			tmp_drug_use = DrugUsed(visit=patient_visit,drug=tmp_drug)
		i+=1

def parseExposures(row,patient_visit):
	csv_columns = ["IVDU exposure","MSM Exposure","Hetero Exposure",\
	"Transfusion Exposure","NCI(hetero)","NCI(MSM)","Other Exposure"]
	exp_list = {}

	for exposure in list(Exposure.select()):
		exp_list[exposure.name] = exposure.id
	
	i=0
	for column in row[52:58]:
		if column.upper() == "X":
			tmp_patient_exposed = PatientExposedTo(visit=patient_visit,\
			exposure=Exposure.get(exp_list[csv_columns[i]]))
		i+=1




def parseIllness(row,patient_visit):


	csv_columns = ["Depression","Bipolar","Schizophrenia","ADHD","Anxiety","Dementia",\
	"Epilepsy/Seizures","Diagnosed HIVD","Head Trauma or Spinal Injury", "MS", "Paranoia",\
	"PTSD","Stroke","Peripheral Neuropathy","Other neuro problems","No neuro problems listed"]
	
	ill_list = {}

	for illness in list(Illness.select()):
		ill_list[illness.name] = illness.id


	i=0
	for column in row[104:119]:
		if column.upper() == "X":
			tmp_patient_illness = PatientAdditionalIllnesses(visit=patient_visit,\
			illness=Illness.get(ill_list[csv_columns[i]]))
		elif i==14 and len(column):
			try:
				tmp_ill = Illness.select(Illness.q.name==column).getOne()
			except SQLObjectNotFound:
				tmp_ill = Illness(name=column)
			tmp_patient_illness = PatientAdditionalIllnesses(visit=patient_visit,
			illness=tmp_ill)
		i+=1


def parsePatient(row):
	fmt = "%m/%d/%y"
	v_dt = c_dt = v_sc = c_sc = None
	
	try:
		v_dt=datetime.strptime(row[44],fmt)
	except ValueError:
		pass
	try:
		c_dt=datetime.strptime(row[38],fmt)
	except ValueError:
		pass

	try:
		v_sc = int(row[43].replace(',',''))
	except:
		pass
	
	try:
		c_sc = int(row[37].replace(',',''))
	except:
		pass


	tmp_patient = Patient(\
	name=row[0],\
	gender=row[29],\
	race=row[30],\
	yearOfBirth=row[32],\
	seroPositiveSince=row[34],\
	lowestCd4=c_sc,\
	highestViral=v_sc,\
	highestViralDate=v_dt,\
	lowestCd4Date=c_dt
	)

def parseVisit(row,initial=False):
	try:
		if not initial:
			patient_name = row[0][:row[0].find("-R")].upper()
		else:
			patient_name = row[0]
	
		tmp_patient = Patient.selectBy(name=patient_name).getOne()

		try:
			tmp_dsg = int(row[36])
		except:
			tmp_dsg = None

		tmp_visit = Visit(\
		patientID=tmp_patient,\
		cd4=row[40],\
		viral=row[46],
		name=row[0],
		dsg=tmp_dsg)
		
		parseDrugUse(row,tmp_visit)
		parseExposures(row,tmp_visit)
		parseIllness(row,tmp_visit)

	except Exception as e:
		print e
		print "Unable to import row: attempt manual entry:"
		print row


if __name__ == '__main__':
	reader = csv.reader(open(sys.argv[1]),delimiter=",",quotechar='"')

	for row in reader:
		# See if it is a new patient, or a previously entered one
		# with a return visit
		if row[0][0] == "A":
			if row[0].find('-R') != -1:
				parseVisit(row)	
			else:
				# New patient - add them to the DB first
				parsePatient(row)
				# Now go back and add their initial visit
				parseVisit(row,True)

