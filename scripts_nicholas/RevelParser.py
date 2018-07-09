"""
Script that converts the notation given by the REVEL website for a genetic variant to genomic
coordinate notation (for hg38). The script needs two command line arguments to run, which specify
the csv file to read from's path and the txt file to read to's path.
call the script as:
python REVELChromosomeTest.py <file to read from> <file to write to>

"""
#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------
# Opens the csv file with given name from the REVEL website for read/write.
with open(sys.argv[1], newline='') as csvfile:
	revelTest = open(sys.argv[2], 'w+') # Opens file to write to for writing
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|') # Creates a reader
	for row in reader: # Iterates through each row in the csv file
		# The following lines in this code block formats the variant into genomic coordinate notation
		newList = row[0].split(",")
		newString = ""
		newString += "chr"
		newString += new_list[0]
		newString += ":g."
		newString += new_list[1]
		newString += ":"
		newString += new_list[3]
		newString += ">"
		newString += new_list[2]
		newString += "\n"
		revelTest.write(newString)
	revelTest.close()
