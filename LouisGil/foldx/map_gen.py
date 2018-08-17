#!/usr/bin/python3

import requests
import json
import pandas as pd
import os

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
  
def finder(dictionary,chr,location,AAref,AAalt,r,a):
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
            foldx_position=AAref+chain+str(pos)+AAalt
            print("foldx --command=PositionScan --pdb="+i+".pdb --pdb-dir=/home/louisgil --positions="+ foldx_position
                +" > "+chr+"."+str(location)+"."+r+'.'+a+"."+ foldx_position+"."+i+".training"+".txt")
            
            # print("foldx --command=PositionScan --pdb="+i+".pdb --pdb-dir=/home/louisgil --positions="+ foldx_position+" > "+chr+"."+str(location)+"."+ foldx_position+".txt"+"\n")
            # os.system("foldx --command=PositionScan --pdb="+i+"_Repair.pdb --pdb-dir=/home/louisgil/foldxTemp --positions="+ foldx_position+" > "+chr+"."+str(location)+"."+ foldx_position+".txt")
            # print("http://mupit.icm.jhu.edu/MuPIT_Interactive/?structure_id="+i+"&addtlinfo=brca&gm="+chr+":"+str(location)+"&altaa="+AAalt+"\n\n")



if __name__=='__main__':
    df = pd.read_csv('h.vcf',sep='\t',skiprows=3,header=1)
    #chomosome
    df['Chromosome']= 'chr' + df['#CHROM'].astype(str)
    #position
    df['POS']
    #protein HGVS
    AA=df['INFO'].str.split('|').str[11].str.split(":").str[1].str.split(".").str[1]
    #Amino acid reference
    df['AAref']=AA.str[0:3]

    #Amino acid Altered
    df['AAalt']=AA.str[-3:]

    #Count Nan's
    # df['AAalt'].isnull().sum()

    #Eliminate terminators
    df= df[df.AAalt != 'Ter']

    #Make a new dataframe 
    frames=pd.concat([df['Chromosome'],df['POS'],df['AAref'],df['AAalt'],df['REF'],df['ALT']],axis=1)

    #Eliminate Nan's
    frames=frames.dropna()

    #Transform the amino acid in to it 1 letter leyend
    #Amino Acid reference
    frames.AAref.loc[frames.AAref == 'Ala'] = 'A'
    frames.AAref.loc[frames.AAref == 'Arg'] = 'R'
    frames.AAref.loc[frames.AAref == 'Asn'] = 'N'
    frames.AAref.loc[frames.AAref == 'Asp'] = 'D'
    frames.AAref.loc[frames.AAref == 'Asx'] = 'B'
    frames.AAref.loc[frames.AAref == 'Cys'] = 'C'
    frames.AAref.loc[frames.AAref == 'Glu'] = 'E'
    frames.AAref.loc[frames.AAref == 'Gln'] = 'Q'
    frames.AAref.loc[frames.AAref == 'Glx'] = 'Z'
    frames.AAref.loc[frames.AAref == 'Gly'] = 'G'
    frames.AAref.loc[frames.AAref == 'His'] = 'H'
    frames.AAref.loc[frames.AAref == 'Ile'] = 'I'
    frames.AAref.loc[frames.AAref == 'Leu'] = 'L'
    frames.AAref.loc[frames.AAref == 'Lys'] = 'K'
    frames.AAref.loc[frames.AAref == 'Met'] = 'M'
    frames.AAref.loc[frames.AAref == 'Phe'] = 'F'
    frames.AAref.loc[frames.AAref == 'Pro'] = 'P'
    frames.AAref.loc[frames.AAref == 'Ser'] = 'S'
    frames.AAref.loc[frames.AAref == 'Thr'] = 'T'
    frames.AAref.loc[frames.AAref == 'Trp'] = 'W'
    frames.AAref.loc[frames.AAref == 'Tyr'] = 'Y'
    frames.AAref.loc[frames.AAref == 'Val'] = 'V'
    #Amino Acid altered
    frames.AAalt.loc[frames.AAalt == 'Ala'] = 'A'
    frames.AAalt.loc[frames.AAalt == 'Arg'] = 'R'
    frames.AAalt.loc[frames.AAalt == 'Asn'] = 'N'
    frames.AAalt.loc[frames.AAalt == 'Asp'] = 'D'
    frames.AAalt.loc[frames.AAalt == 'Asx'] = 'B'
    frames.AAalt.loc[frames.AAalt == 'Cys'] = 'C'
    frames.AAalt.loc[frames.AAalt == 'Glu'] = 'E'
    frames.AAalt.loc[frames.AAalt == 'Gln'] = 'Q'
    frames.AAalt.loc[frames.AAalt == 'Glx'] = 'z'
    frames.AAalt.loc[frames.AAalt == 'Gly'] = 'G'
    frames.AAalt.loc[frames.AAalt == 'His'] = 'H'
    frames.AAalt.loc[frames.AAalt == 'Ile'] = 'I'
    frames.AAalt.loc[frames.AAalt == 'Leu'] = 'L'
    frames.AAalt.loc[frames.AAalt == 'Lys'] = 'K'
    frames.AAalt.loc[frames.AAalt == 'Met'] = 'M'
    frames.AAalt.loc[frames.AAalt == 'Phe'] = 'F'
    frames.AAalt.loc[frames.AAalt == 'Pro'] = 'P'
    frames.AAalt.loc[frames.AAalt == 'Ser'] = 'S'
    frames.AAalt.loc[frames.AAalt == 'Thr'] = 'T'
    frames.AAalt.loc[frames.AAalt == 'Trp'] = 'W'
    frames.AAalt.loc[frames.AAalt == 'Tyr'] = 'Y'
    frames.AAalt.loc[frames.AAalt == 'Val'] = 'V'

    # mapping = get_structures('chr17',43070969)
    for P, C,aaf,aal,r,a in zip(frames.POS, frames.Chromosome,frames.AAref,frames.AAalt,frames.REF,frames.ALT):
        # print(C,P);
        mapping = get_structures(C,P)
        # # mapping = get_structures('chr13',32319191)
        temp=(json.dumps(mapping, indent=2,sort_keys=True))
        dict_json = json.loads(temp)
        # # print(dict_json.keys())
        finder(dict_json,C,P,aaf,aal,r,a)
        # print(dict_json["gms"]["chr17:43070969"]['structures'])
        # print(dict_json['structures'])

