

import urllib.request

print('Beginning file download with urllib2...')

url ='https://wiki.cancerimagingarchive.net/download/attachments/16056856/TCIA_NSCLC-Radiomics-Genomics_06-22-2015.tcia?version=1&modificationDate=1534787429713&api=v2'


urllib.request.urlretrieve(url , 'C:/Users/Public/TEST.tcia ') 

#pip install the bellow;
#pip install numpy 
#etc #add more when we get into 