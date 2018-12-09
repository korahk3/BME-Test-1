

import urllib.request

print('Now check the folder!')

#Bellow is the data used for models created by BME- clinic team.
url ='https://wiki.cancerimagingarchive.net/download/attachments/16056856/TCIA_NSCLC-Radiomics-Genomics_06-22-2015.tcia?version=1&modificationDate=1534787429713&api=v2'
urllib.request.urlretrieve(url , 'C:/Users/Public/RANDOM BY KIRAN/TEST.tcia ')


#Please download this to view and download the links 
#this link for windows computers only #just put '#' in front of "applicationlink.... and urllib.request.urlretrieve(Applicationlin...)" 

Applicationlink='https://wiki.cancerimagingarchive.net/download/attachments/41518329/NBIA%20Data%20Retriever-3.2.msi?version=2&modificationDate=1541687756961&api=v2'
urllib.request.urlretrieve(Applicationlink,'C:/Users/Public/RANDOM BY KIRAN/Application.msi')
# make sure the download path is correct.


#current libraries used in our project / Clinic 
#pip install urllib.request or urllib

