################################################################################################
# This script takes two csv-like files as input. The script randomly takes a certain number of
# rows that contain a variants pathogenicity in a specified column from the first csv file and
# appends them to a copy of the second file. The script outputs two new csv-like files, the first
# file with the taken columns removed and the second file with the taken columns added.
# Call the script as:
# python MoveVariants.py <csv to remove rows> <csv to add rows> <output csv 1> <output csv 2>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018/scripts_nicholas')
import MiscFunctions as mf
import random
import time
#------------------------------------------------------------------------------------------------

random.seed(int(time.time()/30))

sep1 = mf.determine_separator(sys.argv[1])
sep2 = mf.determine_separator(sys.argv[2])

df1 = pd.read_csv(sys.argv[1], sep=sep1, header=0)
df2 = pd.read_csv(sys.argv[2], sep=sep2, header=0)

mf.print_columns_with_index(df1)
df1_column_number = mf.get_int_answer('What column contains the pathogenicity in the first file? ')
df1_column_name = list(df1.columns)[df1_column_number - 1]
df1_variant_column = list(df1.columns)[0]
print(df1_column_name, df1_variant_column)

mf.print_columns_with_index(df2)
df2_column_number = mf.get_int_answer('What column contains the pathogenicity in the second file? ')
df2_column_name = list(df2.columns)[df2_column_number - 1]
df2_variant_column = list(df2.columns)[0]
print(df2_column_name, df2_variant_column)

answer = input('Move pathogenic or benign variants (p/b)? ')
number = mf.get_int_answer('Move how many variants? ')

df1_pathogenic = df1[ (df1[df1_column_name] == 'Pathogenic') | (df1[df1_column_name] == 'Likely_pathogenic') ]
df1_benign = df1[ (df1[df1_column_name] == 'Benign') | (df1[df1_column_name] == 'Likely_benign') ]

if ( answer == 'p'):
	number_of_variants = df1_pathogenic.shape[0]
	indices = random.sample(range(number_of_variants), number)
	everything_else = [i for i in range(number_of_variants) if i not in indices]

	df1_to_move = df1_pathogenic.iloc[indices][[df1_variant_column, df1_column_name]]
	df1_to_move = df1_to_move.rename(index=str, columns={df1_variant_column: df2_variant_column, df1_column_name: df2_column_name})
	
	df_out_2 = df2[[df2_variant_column, df2_column_name]].append(df1_to_move, ignore_index=True)
	df_out_1 = df1_benign.append(df1_pathogenic.iloc[everything_else])
	df_out_1.to_csv(sys.argv[3])
	df_out_2.to_csv(sys.argv[4])
else:
	number_of_variants = df1_benign.shape[0]
	indices = random.sample(range(number_of_variants), number)
	everything_else = [i for i in range(number_of_variants) if i not in indices]

	df1_to_move = df1_benign.iloc[indices][[df1_variant_column, df1_column_name]]
	df1_to_move = df1_to_move.rename(index=str, columns={df1_variant_column: df2_variant_column, df1_column_name: df2_column_name})
	
	df_out_2 = df2[[df2_variant_column, df2_column_name]].append(df1_to_move, ignore_index=True)
	df_out_1 = df1_pathogenic.append(df1_benign.iloc[everything_else])
	df_out_1.to_csv(sys.argv[3], index=False)
	df_out_2.to_csv(sys.argv[4], index=False)