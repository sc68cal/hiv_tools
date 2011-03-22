from sqlobject import *

__author__="scollins"
__date__ ="$Wed Mar 31 10:22:24 EDT 2010"

conn = connectionForURI("mysql://root:root@localhost:8889/mydb")

sqlhub.processConnection = conn

class Drug(SQLObject):
	class sqlmeta:
		fromDatabase=True
	
class DrugTest(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')
	drug = ForeignKey('Drug')

class DrugUsed(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')
	drug = ForeignKey('Drug')
	
class Exposure(SQLObject):
	class sqlmeta:
		fromDatabase=True
	
class HivdTest(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')
	
class Illness(SQLObject):
	class sqlmeta:
		fromDatabase=True
	
class Patient(SQLObject):
	class sqlmeta:
		fromDatabase=True

	visits = MultipleJoin('Visit')

class PatientAdditionalIllnesses(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')
	illness = ForeignKey('Illness')
	
class PatientExposedTo(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')
	exposure = ForeignKey('Exposure')
	
class Sequence(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')


class Mutation(SQLObject):
	class sqlmeta:
		fromDatabase=True
	visit = ForeignKey('Visit')

class MutationPosition(SQLObject):
	class sqlmeta:
		fromDatabase=True
	mutation = ForeignKey('Mutation')
	
class Visit(SQLObject):
	class sqlmeta:
		fromDatabase=True
	patient = ForeignKey('Patient')

	illnesses = RelatedJoin('Illness', joinColumn='visit_id', otherColumn='illness_id',
	intermediateTable='patient_additional_illnesses', createRelatedTable=False)
	
	drugs = RelatedJoin('Drug', joinColumn="visit_id", otherColumn="drug_id",
	intermediateTable="drug_used", createRelatedTable=False)

	exposures = RelatedJoin('Exposure', joinColumn="visit_id", otherColumn="exposure_id",
	intermediateTable="patient_exposed_to", createRelatedTable=False)
	
