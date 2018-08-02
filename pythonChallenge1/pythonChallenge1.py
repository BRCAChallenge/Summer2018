import pandas as pd
variants = pd.read_csv('pythonChallenge1_inputData_clinVar.csv', index_col=None)

variants.head()

iD = variants['hgvs']
aaChange = variants['proteinChange']
brca1 = 'B1'
brca2 = 'B2'
for i in range(0, len(iD)):
    seqId = iD[i]
    head = '>' + seqId[:9] + ' ' + aaChange[i] + '\n'
    if(seqId == 'NP_009225'):
        variant = head + brca1
    else:
        variant = head + brca2
    print(variant)
print('\n') 
