import pandas as pd
import numpy as np

from bokeh.plotting import figure, show

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def trata_dados_inteiros(coluna):
    novaLista = []
    for x in coluna:
        novaLista.append(int(x))
    return novaLista

def trata_dados_float(coluna):
    novaLista = []
    for x in coluna:
        a = str(x)
        #print(a)
        a = a[3:-2]
        a = a.replace(",","")
        onVirgula = a.find("$")
        if (onVirgula > 0):
            a = a[:onVirgula-1]
        #print(a)
        novaLista.append(float(a))
    return novaLista

def mediaLista(L):
    media = 0
    for x in L:
        media += x
    media = media/len(L)
    return media
w0 = 2
w1 = 3
w2 = 102
alfa = 0.2

def f(w0, w1,avaliacao,w2,visualizacao):
    return w0+ avaliacao*w1 + visualizacao*w2

#####Função da matrix transposta
##def f_matrizT(ws,):
    


def error(prices, rating, totalRivews, w0, w1, w2):
    sum_distancia = 0

    for i in range(len(prices)):
        pontoX = prices[i]
        pontoY = rating[i]
        pontoZ = totalReviews[i]

        distancia = f(w0,w1,pontoY,w2,pontoZ) - pontoX
        quadradoD = distancia**2
        sum_distancia += quadradoD

    return sum_distancia/len(prices)

##def dw0():
##
##def dw1():
##
##def dw2():

def escolherParcelaDosDados(lista, parcela, parte = 1):
    parcelaDaLista = []
    limiteDeDados = len(lista)*parcela//100
    if parte == 1:##dos primeiros aos ultimos
        x = 0
        while (x < limiteDeDados):
            parcelaDaLista.append(lista[x])
            x+=1
    elif parte == 2:##dos ultimos para os primeiros
        x = len(lista)
        while (x > limiteDeDados):
            parcelaDaLista.append(lista[x])
            x-=1
    return parcelaDaLista




    
dados = pd.read_csv('items.csv')
dados = dados.dropna()##remove as linhas com os NaN

rating = dados[['rating']].values
totalReviews = dados[['totalReviews']].values
prices = dados[['prices']].values

##dadosApurados = [asin,brand,title,url,image,rating,reviewUrl,totalReviews,prices]
allData = [rating,totalReviews,prices]


rating = trata_dados_inteiros(rating)
totalReviews = trata_dados_inteiros(totalReviews)
prices = trata_dados_float(prices)

##for x in range(20):
##    ##treinar os dados aqui
##    w0_temp = w0 - alfa*dw0()
##    w1_temp = w1 - alfa*dw1()
##    w2_temp = w2 - alfa*dw2()
##
##    w0 = w0_temp
##    w1 = w1_temp
##    w2 = w2_temp
##
##    p = figure(plot_width=600, plot_height=400)
##    p.scatter(rating,totalReviews,prices, radius=0.01)


#### Grafico 3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

##
x=np.array(rating)
y=np.array(totalReviews)
z=np.array(prices)
##
ax.scatter(x,y,z)

plt.show()




