#######################
## Louis Gil         ##
## BRCA EXANGE 	     ##
## INPUT for Cravant ##
#######################
import pandas as pd;
# import sys;


###################################################
## filter(df)
#-------------------------------------------------
# Input: dataframe
# Description:FILTERS FOR Realese date 7 or older 
# & being from enigma & the lenght of the cordinate 
# strings be 20 (meaning its a single nuc. sub).
###################################################
def filter(df):
	df=df[(df.Sources.str.contains("ENIGMA"))&(df.Data_Release_id>=7)&(df.Genomic_Coordinate_hg38.str.len()==20)]
	return df

#######################################
## add_strand(df)
#--------------------------------------
# Input: dataframe
# Description: Add strand to BRCA genes
#######################################
def add_strand(df):
	#int column to +
	temp = list('+'*len(df))
	df.insert(3, column='Strand', value=temp)
	#if BRCA1 then change strand to -
	df.loc[(df.Gene_Symbol=="BRCA1"), 'Strand']= '-'
	return df

########################################
## Cravant_input_format(df)
#--------------------------------------
# Input: dataframe
# Description: Return a dataframe with
# CAVANT accepted input.
# http://cravat.us/CRAVAT/help.jsp#input
########################################
def Cravant_input_format(df):
	#grab chromosome
	temp_char = df['Genomic_Coordinate_hg38'].str.split(':').str[0].rename('Chr.')
	#grab Position
	temp_pos=df['Genomic_Coordinate_hg38'].str.split(':').str[1].str.split('.').str[1].rename('Position')
	#grab strand
	st=df['Strand']
	#grab Reference nucleotide
	temp_ref=df['Genomic_Coordinate_hg38'].str.split(':').str[2].str.split('>').str[0].rename('Ref. base')
	#grab Altered nucleotide
	temp_alt=df['Genomic_Coordinate_hg38'].str.split(':').str[2].str.split('>').str[1].rename('Alt. base')
	#concatanate all above columns
	frames = pd.concat([temp_char,temp_pos,st,temp_ref,temp_alt], axis=1)
	return frames

########################### MAIN #############################
#input file
df = pd.read_csv("first_versions_of_variants_in_enigma_barring_first_release_ammended.csv")

#generalize input
#i=sys.argv[1]
#o=sys.argv[2]
# df=pd.read_csv(str(i))

#FILTERS FOR Realese date 7 or older & being from enigma & the lenght of the cordinate strings be 20(meaning its a single nuc. sub)
df=filter(df)

#Adds the strands to the df
df=add_strand(df)

#Creates a df formated to CRAVANT Input
df=Cravant_input_format(df)

#outputfile
df.to_csv("cravant_input.tsv", sep='\t')

#generalize output
# df.to_csv(o, sep='\t')







