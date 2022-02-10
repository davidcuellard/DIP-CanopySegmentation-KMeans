"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Segmentación KMeans

@author: David Felipe Cuellar Diaz
"""

#basado en: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html

# importar paquetes
import cv2
import numpy as np

class segmentacion: 

    def __init__(self,image="image.jpg",folder="",scalefactor=1,resize=False):        
        self.image=image
        self.folder=folder
        self.scalefactor=scalefactor
        self.resize=resize
    
    def KMeans(self):
        
        # carga la imagen
        imagein = cv2.imread(self.image)

        # cambia el tamaño de la imagen si es necesario
        if self.resize == True:
            height, width = imagein.shape[:2]
            imagein = cv2.resize(imagein,(int(self.scalefactor*width), int(self.scalefactor*height)), interpolation = cv2.INTER_NEAREST)
        
        # crea una copia de la imagen                
        imagecopy=imagein.copy()
       
        # convierte la imagen a np.float32
        samples = np.float32(imagein.reshape((-1,3)))
        
        # define criteria, numero de clusters (k) y aplica kmeans
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 2
        ret,label,center=cv2.kmeans(samples,K,None,criteria,10,cv2.KMEANS_PP_CENTERS)
        
        # Convierte el fondo en uint8, se aplica a la imagen de entrada 
        center = np.uint8(center)
        result = center[label.flatten()]
        result2 = result.reshape((imagein.shape))
        
        cv2.imwrite(self.folder + "imagecopy.bmp",imagecopy) 
        cv2.imwrite(self.folder + "output.bmp",result2)

        # Convierte el resultado kmeans en escala de grises
        gray= cv2.cvtColor(result2, cv2.COLOR_BGR2GRAY)
        
        # aplica umbralización threshold para crear la máscara
        ret,mask = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)    
        
        # aplica la máscara a la imagen de entrada
        resultmask = cv2.bitwise_and(imagein, imagein, mask=mask)
        
        
        # Guarda las imágenes
        cv2.imwrite(self.folder + "mask.bmp",mask)
        cv2.imwrite(self.folder + "result.bmp",resultmask)

        # Invierte la máscara y se la aplica a la imagen de entrada
        ret,mask2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
        resultmask2 = cv2.bitwise_and(imagein, imagein, mask=mask2)
        
        # Guarda las imagenes
        cv2.imwrite(self.folder + "mask2.bmp",mask2)
        cv2.imwrite(self.folder + "result2.bmp",resultmask2)
        
        cv2.destroyAllWindows()