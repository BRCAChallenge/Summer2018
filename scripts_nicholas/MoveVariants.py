################################################################################################
# Call the script as:
# python MoveVariants.py <csv to remove rows> <csv to add rows> <output csv 1> <output csv 2>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd # For dataframes
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
import random # For pseudo-random numbers
import time # To set the seed
#------------------------------------------------------------------------------------------------

## Move a specified number of pathogenic or benign variants from a csv file to another file.
#      this doesn't modify the original files, rather creates new ones with new data.
#  @param take_from          : The csv-like file to remove variants from.
#  @param add_to             : The csv-like file to add variants to.
#  @param modified_take_from : The modified version of take_from
#  @param modified_add_to    : The modified version of add_to
def MoveVariants(take_from, add_to, modified_take_from, modified_add_to)
	# Create dataframes from take_from and add_to. I will refer to the dataframes by their
	# respective filenames.
	sep1 = mf.determine_separator(take_from)
	sep2 = mf.determine_separator(add_to)
	df1 = pd.read_csv(take_from, sep=sep1, header=0)
	df2 = pd.read_csv(add_to, sep=sep2, header=0)

	# Gets the name of the column of the variants' pathogenicity in take_from.
	mf.print_columns_with_index(df1)
	df1_column_number = mf.get_int_answer('What column contains the pathogenicity in the first file? ')
	df1_column_name = list(df1.columns)[df1_column_number - 1]
	df1_variant_column = list(df1.columns)[0]

	# Gets the name of the column of the variants' pathogenicity add_to.
	mf.print_columns_with_index(df2)
	df2_column_number = mf.get_int_answer('What column contains the pathogenicity in the second file? ')
	df2_column_name = list(df2.columns)[df2_column_number - 1]
	df2_variant_column = list(df2.columns)[0]

	# Gets the number of variants to transfer and of what pathogenicity.
	answer = input('Move pathogenic or benign variants (p/b)? ')
	number_to_move = mf.get_int_answer('Move how many variants? ')

	# Splits take_from into two parts, one containing only pathogenic variants and the other only benign.
	df1_pathogenic = df1[ (df1[df1_column_name] == 'Pathogenic') | (df1[df1_column_name] == 'Likely_pathogenic') ]
	df1_benign = df1[ (df1[df1_column_name] == 'Benign') | (df1[df1_column_name] == 'Likely_benign') ]

	
	if ( answer == 'p'): # If the user wants to move pathogenic variants.
		# Randomly selects number_to_move pathogenic variants from take_from's pathogenic half.
		number_of_variants = df1_pathogenic.shape[0]
		indices = random.sample(range(number_of_variants), number_to_move)
		everything_else = [i for i in range(number_of_variants) if i not in indices]

		# Creates a dataframe of the pathogenic variants to move. Renames the columns to match add_to's.
		df1_to_move = df1_pathogenic.iloc[indices][[df1_variant_column, df1_column_name]]
		df1_to_move = df1_to_move.rename(index=str, columns={df1_variant_column: df2_variant_column, df1_column_name: df2_column_name})
	
		# Generates the two modified dataframes, and generates the two new csv files.
		df_out_2 = df2[[df2_variant_column, df2_column_name]].append(df1_to_move, ignore_index=True)
		df_out_1 = df1_benign.append(df1_pathogenic.iloc[everything_else])
		df_out_1.to_csv(modified_take_from, index=False)
		df_out_2.to_csv(modified_add_to, index=False)
	else: # If the user wants to move benign variants.
		# Randomly selects number_to_move benign variants from take_from's pathogenic half.
		number_of_variants = df1_benign.shape[0]
		indices = random.sample(range(number_of_variants), number_to_move)
		everything_else = [i for i in range(number_of_variants) if i not in indices]

		# Creates a dataframe of the benign variants to move. Renames the columns to match add_to's.
		df1_to_move = df1_benign.iloc[indices][[df1_variant_column, df1_column_name]]
		df1_to_move = df1_to_move.rename(index=str, columns={df1_variant_column: df2_variant_column, df1_column_name: df2_column_name})
	
		# Generates the two modified dataframes, and generates the two new csv files.
		df_out_2 = df2[[df2_variant_column, df2_column_name]].append(df1_to_move, ignore_index=True)
		df_out_1 = df1_pathogenic.append(df1_benign.iloc[everything_else])
		df_out_1.to_csv(modified_take_from, index=False)
		df_out_2.to_csv(modified_add_to, index=False)

################################ Main ################################

random.seed(time.time())

# arg1 : csv-like file (file1) to take several variants from. Doesn't modify the file.
# arg2 : csv-like file (file2) to add several variants to. Doesn't modify the file.
# arg3 : csv-like file that contains the modified version of file1.
# arg4 : csv-like file that contains the modified version of file2.
MoveVariants(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
