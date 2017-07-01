'''
Created on Jun 24, 2017

@author: raul
'''

import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
from numba import jit

@jit
def ehRedundante(i,j,n,matriz):
    pVermelhoM = 0
    pVerdeM = 0
    pAzulM = 0
    resultados = [False,False,False]
    pijAzul = matriz[i][j][0]
    pijVerde = matriz[i][j][1]
    pijVermelho = matriz[i][j][2]
    for l in range(i,i+n):
        for c in range(j,j+n):
            subAzul = math.fabs(pijAzul - matriz[l][c][0])
            subVerde = math.fabs(pijVerde - matriz[l][c][1])
            subVermelho = math.fabs(pijVermelho - matriz[l][c][2])
            if(pAzulM<subAzul):
                pAzulM = subAzul
            if(pVerdeM<subVerde):
                pVerdeM = subVerde
            if(pVermelhoM<subVermelho):
                pVermelhoM = subVermelho

    if(pAzulM<10):
        resultados[0] = True
    if(pVerdeM<10):
        resultados[1] = True
    if(pVermelhoM<10):
        resultados[2] = True
    return resultados

@jit
def contarBlocos(img,n):
    numReduAzul = 0
    numReduVermelho = 0
    numReduVerde = 0
    for i in range(img.shape[0]-(n-1)):
        for j in range(img.shape[1]-(n-1)):
            resultados = ehRedundante(i, j, n, img)
            if(resultados[0]):
                numReduAzul+=1
            if(resultados[1]):
                numReduVerde+=1
            if(resultados[2]):
                numReduVermelho+=1
    return numReduAzul,numReduVerde,numReduVermelho
        
img1 = cv2.imread('Sky Field.jpg')  
resulAzul = []
resulVerde = []
resulVermelho = []
n = 32
arq = open("blocos.txt","a")
for i in range(2,n+1):
    rAzul,rVerde,rVermelho = contarBlocos(img1, i)
    resulAzul.append(rAzul)
    resulVerde.append(rVerde)
    resulVermelho.append(rVermelho)
    print("n=%s: %s %s %s"%(i,rAzul,rVerde,rVermelho))
    arq.write("n=%s: %s %s %s\n"%(i,rAzul,rVerde,rVermelho))
arq.close()

fig = plt.figure()

x = list(range(2,n+1))
y = resulAzul

width_n = 0.9

plt.bar(x, y, width=width_n, color="blue")
plt.show()
plt.bar(x, resulVerde, width=width_n, color="green")
plt.show()
plt.bar(x, resulVermelho, width=width_n, color="red")
plt.show()
