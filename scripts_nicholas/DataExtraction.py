"""
Script that extracts data given in a csv file. Writes to file called reference.txt that on
each line has a variant with genomic coordinate and variation (relative to hg38) along with
the pathogenicity.
Call the script as:
python Data DataExtraction.py <file to read from> <file to write to>

"""
#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
import sys # For command-line arguments
#------------------------------------------------------------------------------------------------
# Extracts from a file named out.csv on the desktop.
with open(sys.argv[1], newline='') as csvfile: 
  referenceFile = open(sys.argv[2], 'w+') # Opens reference.txt for writing
  reader = csv.reader(csvfile, delimiter=' ', quotechar='|') # Creates csv reader
  variantList = []
  for variant in reader: # Iterates through each row in the reader
    variantProperies = variant[0].split(",") # Elements of the row become elements of a list
    newString = ""
    newString += variantProperies[1] + '\t'
    for item in variantProperies: # Iterates through the line looking for key words
      newerList = item.split(",") # Each comma dilineated string becomes an element of a newer list
      strippedList = [element.strip('\"') for element in newerList]
      print(strippedList)
      if ( "Benign" in strippedList ): # Checks if the variant is benign
        newString += "Benign "
      if ( "Likely_benign" in strippedList ): # Checks if the variant is "likely benign"
        newString += "Likely_benign "
      if ( "Uncertain_significance" in strippedList ): # Checks if the variant is "uncertain"
        newString += "Uncertain_significance "
      if ( "Pathogenic" in strippedList ): # Checks if the variant is pathogenic
        newString += "Pathogenic "
      if ( "Likely_pathogenic" in strippedList ): # Checks if the variant is "likely pathogenic"
        newString += "Likely_pathogenic "
    variantList.append(newString)
  variantList.sort()
  for variant in variantList:
    referenceFile.write(variant)
    referenceFile.write('\n')
  referenceFile.close()