################################################################################################
# Script that extracts the HGVS necleotide representation of each variant and the pathogenicity
# (which is converted to a binary value) from the file 'variants.to.include.in.test.set.txt' or
# similarly formatted files.
# Call the script as:
# python ExtractTestData.py <input data file> <output file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------

df = pd.read_csv(sys.argv[1], sep='\t', header=0)
write_file = open(sys.argv[2], 'w+')

extract_pathogenicity = mf.get_yes_no("Extract the pathogenicity (y/n)? ")
answer_yes = (extract_pathogenicity == 'y') | (extract_pathogenicity == 'Y')

write_file.write('#Variant')
if ( answer_yes ):
	write_file.write(',Pathogenicity')
write_file.write('\n')


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

# BRCA2 :: NM_000059.3
# BRCA1 :: NM_007294.3