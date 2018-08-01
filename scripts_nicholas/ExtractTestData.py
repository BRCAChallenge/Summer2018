################################################################################################
# Call the script as:
# python ExtractTestData.py <input data file> <output file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

## Extracts the variant identifier (HGVS, genomic coordinate, etc.) and pathogenicity from a
#      numeric value of each variant from the file 'variants.to.include.in.test.set.txt'
#  @param read_file  : The file as input to the script. The file should be tab dilimited and have
#                      no header. The first line of the file should be the title of each column.
#                      One column must contain some variant identification, and another should
#                      contain pathogenicity classification, as a number between 1 and 5.
#  @param write_file : The file to write data to. The file should be a csv file, as the output
#                      is comma-delimited.
def ExtractTestData(read_file, write_file='~/Desktop/out.csv'):

	# Creates a dataframe from read_file and opens a new file for writing.
	df = pd.read_csv(read_file, sep='\t', header=0)
	write_file = open(write_file, 'w+')

	# Asks the user if they want to add a column for pathogenicity in write_file.
	extract_pathogenicity = mf.get_yes_no("Extract the pathogenicity (y/n)? ")
	answer_yes = (extract_pathogenicity == 'y') | (extract_pathogenicity == 'Y')

	# Adds the column names.
	write_file.write('#Variant')
	if ( answer_yes ):
		write_file.write(',Pathogenicity')
	write_file.write('\n')

	# Adds all the variants that are single subsitutions and are not VUS's to write_file. Also,
	# adds the pathogenicity of the variant if the user replied yes.
	for index, row in df.iterrows():
		if ( ('>' in row.values[1]) & (not int(row.values[-1]) == 3)):
			if ( row.values[1] == 'BRCA1' ):
				write_file.write('NM_007294.3:' + str(row.values[1]))
			else:
				write_file.write('NM_000059.3:' + str(row.values[1]))
			if ( answer_yes ):
				if ( int(row.values[-1]) > 3 ):
					write_file.write(',' + 'Pathogenic')
				elif ( int(row.values[-1]) < 3 ):
					write_file.write(',' + 'Benign')
			write_file.write('\n')

	write_file.close()

################################ Main ################################

# arg1 : File with format like 'variants.to.include.in.test.set.txt' (see Synapse)
# arg2 : File to write to, a csv file. Default path: ~/Desktop/out.csv
ExtractTestData(sys.argv[1], sys.argv[2])



