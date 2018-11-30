


import matplotlib.pyplot as plt #plt is declared to be used instead of matplotlib.pyplot
import pydicom #need this library to convert dicom image to arrays 
from pydicom.data import get_testdata_files #need this to call the image from the location 


filename =("C:/Users/kiran/workspace/image-000001.dcm") #need to discribe the pathway to the document 
# future going over to find the any dicom image how to make data loader 

dc = pydicom.dcmread(filename) #this is read the document information 

dc.pixel_array  #this is to convert the pixel data to array

plt.imshow(dc.pixel_array) #i believe it should be effecting 

plt.show(filename) #to show the information that is attached to the image #I think
plt.show(dc) #coverted file to arrays are display3ed with this command


