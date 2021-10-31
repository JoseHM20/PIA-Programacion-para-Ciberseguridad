import os
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import time

def printMeta(ruta):
    print("=======================")
    print("Metadata retrieval tool")
    print("=======================")

    print("\n")
    time.sleep(2)

    os.mkdir("METADATA") #Create a directory with the name "METADATA"
    os.chdir("METADATA") # Moves to the directory "METADATA"
    sources = []
    list = []
    for subdir, dirs, files in os.walk(ruta):
        for file in files:
            filepath = subdir + os.sep + file #Go to the subdirectory to find the img
            if filepath.endswith(".jpg") or filepath.endswith(".png"): #Searches if there is a file with .jpg or .png
             try:
                imagename = filepath 
             except OSError:
                print("No se encontró la img")
             else:
                sources.append(imagename)
                print(imagename)
                f = open(f"{file}metadata.txt","w+") #Open a file with permission to write
                image = Image.open(imagename)
                # extract EXIF data
                exifdata = image.getexif()
                for tag_id in exifdata:
                    tag = TAGS.get(tag_id, tag_id) #We get the data of the img 
                    data = exifdata.get(tag_id)
                    # decode bytes
                    if isinstance(data, bytes):
                        data = data.decode()
                    print(f"{tag:25}: {data}")    
                    x = f"{tag:25}: {data}"
                    f.write(x)
                f.close()
    with open("ElementsIMG.txt","w") as f: #Open a file to write the output 
        for i in sources:
            f.write(i+"\n") #Write the results
    os.chdir("../") #Exit the directory
