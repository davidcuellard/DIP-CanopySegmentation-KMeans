"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Metodos de segmentación - TEST

@author: David Felipe Cuellar Diaz
"""

import segKMeans


segmetod = "kmeans/"

folderin = "/home/tg1907/Documents/Tesis5/clases/segmentacion/images/"

tipo=["GRE","NIR","RGB"]

form=[".TIF",".JPG"]

imagein=["","IMG_170805_165709_0138_","IMG_170805_165653_0127_","IMG_170805_165642_0120_","IMG_170805_165723_0147_","IMG_170805_165730_0152_","IMG_170805_165717_0143_","IMG_170805_165538_0077_","IMG_170805_165509_0058_","IMG_170805_165441_0039_","IMG_170805_165742_0160_"]

fr=1
to=1

while True:

    folderimg= folderin + str(fr) + "/" + tipo[0] + "/"
    image=folderimg + imagein[fr] + tipo[0] + form[0]
    folder = folderimg + segmetod

    skm=segKMeans.segmentacion(image=image,folder=folder)
    
    skm.KMeans()
    
    print(fr)
    
    fr = fr+1

    if fr > to:
        break

    

