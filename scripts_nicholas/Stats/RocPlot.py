################################################################################################
# Script that creates a ROC-plot from the data outputted from ExtractPlotScores.py
# Call the script as:
# python RocPlot.py <data file>
################################################################################################

#------------------------------------------------------------------------------------------------
import sys # For command-line arguments
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
sys.path.append('/Users/nicholaslenz/Desktop/Summer2018 (Repo)/scripts_nicholas')
import MiscFunctions as mf
#------------------------------------------------------------------------------------------------
# Determines the separator type associated with the file format of the data file.
sep = mf.determine_separator(sys.argv[1])

# Creates a partition of the interval [0,1]. Creates two empty lists; one will store the true
# positive rate and the other will store the false positive rates.
thresholds = [float(i)/100 for i in range(101)]
x = []
y = []

df = pd.read_csv(sys.argv[1], sep=',')

# Determines what term will be considered positive and which will be negative.
positive_term = 'Pathogenic'
negative_term = 'Benign'
positives = df[df['pathogenicity'] == positive_term].shape[0]
negatives = df[df['pathogenicity'] == negative_term].shape[0]

# For each threshold in the partition, determines the true positive rate and the true negative
# rate for the data.
for threshold in thresholds:
	true_positives  = 0
	false_positives = 0
	for index, row in df.iterrows():
		score = float(row.values[2])
		if ( (score >= threshold) & (row.values[1] == positive_term) ):
			true_positives += 1
		elif ( (score >= threshold) & (row.values[1] == negative_term) ):
			false_positives += 1

	true_positive_rate = true_positives/positives
	false_positive_rate = false_positives/negatives

	x.append(false_positive_rate)
	y.append(true_positive_rate)

#------------------------------------------------------------------------------------------------
# Creates an empty figure, with total area of 1.
figure = plt.figure(figsize=(6, 6))
ax = figure.add_subplot(1, 1, 1)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.xaxis.set_major_locator(MultipleLocator(0.250))
ax.yaxis.set_major_locator(MultipleLocator(0.250))
ax.xaxis.set_minor_locator(MultipleLocator(0.125))
ax.yaxis.set_minor_locator(MultipleLocator(0.125))
ax.tick_params(which='major', length=10.0)
ax.tick_params(which='minor', length=5.0)
ax.set_ylabel('True Positive Rate')
ax.set_xlabel('False Positive Rate')

# Draws the grid and plots the ROC curce and the baseline curve.
ax.grid(linestyle=':', linewidth=0.5, color='black')
ax.plot(x, y, color='blue', linewidth='3.0')
ax.plot([0,1], [0,1], color='orange', linestyle='--')
plt.show()