

import urllib.request#import used to call and download the file from online 

print('Now check the folder!') #simple print line 


#Bellow is the data used for models created by BME-Clinic team.
#Bellow data 'Data1' and 'MetaData1' was used by Daniel Cahall for Random Forest model 

 
Data1 ='https://wiki.cancerimagingarchive.net/download/attachments/16056856/TCIA_NSCLC-Radiomics-Genomics_06-22-2015.tcia?version=1&modificationDate=1534787429713&api=v2'
urllib.request.urlretrieve(Data1 , 'C:/Users/Public/RANDOM BY KIRAN/Data1.tcia ')# make sure the download path is correct. and file format is correct
MetaData1 ='https://wiki.cancerimagingarchive.net/download/attachments/16056856/Lung3.metadata.xls?version=1&modificationDate=1404237338168&api=v2'
urllib.request.urlretrieve(MetaData1, 'C:/Users/Public/RANDOM BY KIRAN/MetaData1.csv')# make sure the download path is correct.


#Please download this to view and download the links 
#this link for windows computers only, if you already have the program just put '#' in front of the next two lines.

Applicationlink='https://wiki.cancerimagingarchive.net/download/attachments/41518329/NBIA%20Data%20Retriever-3.2.msi?version=2&modificationDate=1541687756961&api=v2'
urllib.request.urlretrieve(Applicationlink,'C:/Users/Public/RANDOM BY KIRAN/Application.msi') # make sure the download path is correct and file format is correct 


#current libraries used in our project / Clinic 
#pip install urllib.request or urllib
#More libraries used will be added to this file.


