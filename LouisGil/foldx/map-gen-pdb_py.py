#!/usr/bin/python3

import requests
import json
import pandas as pd

def get_structures (chrom, pos):
    main_url = 'http://mupit.icm.jhu.edu/MuPIT_Interactive'
    query_url = main_url+'/rest/showstructure/query'
    chrompos = '%s:%s' %(chrom,pos)
    params = {
             'search_textarea':chrompos.replace(':',' '),
             'search_gene':'',
             'search_structure':'',
             'search_protein':'',
             'search_upload_file':'',
             }
    r = requests.post(query_url, data=params)
    return r.json()
  
def finder(dictionary,chr,location,aaf,aal):
    chr_loc=str(chr)+":"+str(location)
    temp=[]

    #Empty cases when there is no structure given the possition and chr
    if dict_json["gms"]=={}:
        # print("No 3D structure found (Nothing under gms key)")
        return
    if dict_json["gms"][chr_loc]=={}:
        print("No 3D structure found (Nothing under chr:pos key)")
        return
    if dict_json["gms"][chr_loc]['structures']=={}:
        print("No 3D structure found (Nothing under structures key)")
        return

    #BRCA Exchange hand picked proteinstructure ids
    if "4igk" in dict_json["gms"][chr_loc]['structures']:
        temp.append("4igk")
    if "1t15" in dict_json["gms"][chr_loc]['structures']:
        temp.append("1t15")
    if "1jm7" in dict_json["gms"][chr_loc]['structures']:
        temp.append("1jm7")
    if "fENSP00000380152_7" in dict_json["gms"][chr_loc]['structures']:
        temp.append("fENSP00000380152_7")

    #Case for when you dont find a a structureID  tha BRCA EXANGE uses
    if len(temp)==0:
        # print("Your input is not one of the struc ID BRCA EXANGE uses")
        return

    for i in temp:
        #parsing trhough dictionary for the chain and position
        pos_and_chain=dict_json["structures"][i]["gmtoseqres"][chr_loc]
        pos_and_chain_list=pos_and_chain.split(";")

        #format the chain and position to be printed preatier
        for x in range(len(pos_and_chain_list)):
            pos=pos_and_chain_list[x].split(":")[0]
            
            chain=pos_and_chain_list[x].split(":")[1]

            # print (i+"  "+aaf+chain+str(pos)+aal)

            print("foldx --command=PositionScan --pdb="+i+".pdb --pdb-dir=/home/louisgil --positions="+aaf+chain+str(pos)+aal)
  


def foldx_input(c,p,structure):

    print(c+p+"  "+structure)

if __name__=='__main__':
    # df = pd.read_excel("ClinVarBrca.vcf.CRAVAT_analysis.dev.loaceved_20180719_124030.xls",skiprows=10,header=1)
    df = pd.read_csv("clinvar_dataset_single_sub_vep.vcf",sep='\t',skiprows=3,header=1)
    df['#CHROM'].rename('ch') 
    df['Chromosome']= 'chr' + df['#CHROM'].astype(str)
    df['POS']
    AA=df['INFO'].str.split('|').str[11].str.split(":").str[1].str.split(".").str[1]
    df['AAf']=AA.str[0]
    df['AAl']=AA.str[-3]

    # mapping = get_structures('chr17',43070969)
    for P, C,aaf,aal in zip(df.POS, df.Chromosome,df.AAf,df.AAl):
        # print(C,P);
        mapping = get_structures(C,P)
        # # mapping = get_structures('chr13',32319191)
        temp=(json.dumps(mapping, indent=2,sort_keys=True))
        dict_json = json.loads(temp)
        # # print(dict_json.keys())
        finder(dict_json,C,P,aaf,aal)
        # print(dict_json["gms"]["chr17:43070969"]['structures'])
        # print(dict_json['structures'])

