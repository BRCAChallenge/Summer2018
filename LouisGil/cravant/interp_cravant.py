#######################
## Louis Gil         ##
## BRCA EXANGE 	     ##
## Interpret  ##
#######################
import pandas as pd;
import numpy;
import matplotlib.pyplot as plt;
import seaborn as sns;
import requests
import json


def preatty_print():
	frames = pd.concat([df['ID'],df['Chromosome'],df['Position'],df['Strand'],
	                   df['Reference base(s)'],df['Alternate base(s)'],
	                   df['ClinVar'],df['VEST p-value'].rename('VEST_p_value'),df['VEST FDR']], axis=1)


	temp = list('B'*len(frames))
	frames.insert(7, column='Predicted', value=temp)
	frames.loc[(frames.VEST_p_value<=.05), 'Predicted']= 'p'
	return frames






############### Main ##########
#Input 
df = pd.read_excel("ClinVarBrca.vcf.CRAVAT_analysis.dev.loaceved_20180719_124030.xls",skiprows=10,header=1)

preatty_print(df)