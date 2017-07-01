'''
Created on Jun 24, 2017

@author: raul
'''

import numpy as np
import math
import cv2


def subPixel(px1,px2):
    azul = math.sqrt(math.pow((px1[0]-px2[0]),2))
    verde = math.sqrt(math.pow((px1[1]-px2[1]),2))
    vermelho = math.sqrt(math.pow((px1[2]-px2[2]),2))
    return [azul,verde,vermelho]

def subImagens(img1,img2):
    imagemResultante = np.zeros((img1.shape[0],img1.shape[1],3), np.uint8)
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            pResultado = subPixel(img1[i,j], img2[i,j])
            imagemResultante[i,j] = pResultado
    return imagemResultante

def transform(p,media,min,max):
    return float(255*(p-min)/max-min)
            
# Load an color image in grayscale
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
#cv2.imshow('image.png',img1)
#cv2.imshow('image2.jpg',img2)
print(img1.shape,img1.dtype)
print(img2.shape,img2.dtype)
#imagemResultante = subImagens(img1, img2)
imagemResultante  = img1 - img2

imgA,imgVerde,imgVermelho = cv2.split(imagemResultante)

mediaA,mediaVerde,mediaVermelho = imgA.mean(),imgVerde.mean(),imgVermelho.mean()
maxA,maxVerde,maxVermelho = imgA.max(),imgVerde.max(),imgVermelho.max()
minA,minVerde,minVermelho = imgA.min(),imgVerde.min(),imgVermelho.min()

print("Media: \nAzul:%s\nVerde:%s\nVemelho:%s\n "%(mediaA,mediaVerde,mediaVermelho))
print("Max:\nAzul:%s\nVerde:%s\nVermelho:%s\n"%(maxA,maxVerde,maxVermelho))
print("Min:\nAzul:%s\nVerde:%s\nVermelho:%s\n"%(minA,minVerde,minVermelho))


#cv2.imshow('image2.jpg',imagemResultante)
cv2.imwrite('resultado.jpg',imagemResultante)
#aplica a transformacao ao elementos da matrix
vfunc = np.vectorize(transform)
imgA = vfunc(imgA,mediaA,minA,maxA)
imgVerde = vfunc(imgVerde,mediaVerde,minVerde,maxVerde)
imgVermelho= vfunc(imgVermelho,mediaVermelho,minVermelho,maxVermelho)

resultadoTrans = cv2.merge((imgA,imgVerde,imgVermelho))
cv2.imwrite('resultadoTrans.jpg',resultadoTrans)
print("Terminou")
