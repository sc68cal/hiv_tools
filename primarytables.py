a = Drug(name='Heroin')
a = Drug(name="Methamphetamines")
a = Drug(name="Ritalin")
a = Drug(name="Barbituates")
a = Drug(name="PCP")
a = Drug(name="Alcohol")
a = Drug(name="Tobacco")
a = Drug(name="Other")
a = Drug(name="Narcotics")
a = Drug(name="Benzodiazepines")
a = Drug(name="Ecstacy")
a = Drug(name="Marajuana")
a = Drug(name="Cocaine")


illnesses = ['Hep C','Hep B','Depression','Bipolar','Schizophrenia','ADHD','Anxiety','Dementia','Epilepsy/Seizures','Diagnosed HIVD','Head Trauma or Spinal Injury','MS','Paranoia','PTSD','Stroke','Peripheral Neuropathy','Other neuro problems']
exposures = ['IVDU exposure','MSM Exposure','Hetero Exposure','Transfusion Exposure','NCI(hetero)','NCI(MSM)','Other Exposure']

for exp in exposures:
	a = Exposure(name=exp)

for ill in illnesses:
	a = Illness(name=ill)



