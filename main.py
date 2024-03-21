from lib import *
import sys

"""dicc = {
    'nom' : "Zaira",
    'edad' : 35,
    'tel' : {
        'cel' : 5,
        'fij' : 6,
    }
}

print(dicc['tel']['cel'])"""

"""grafoTest = {
    'A':{'B':5,'C':3},
'B':{'A':5,'C':2,'D':4},
'C':{'A':3,'B':2,'D':6,'E':7},
'D':{'B':4,'C':6,'E':8},
'E':{'C':7,'D':8},
}"""

grafoTest = grafo()

grafoTest.addArista('A','B',5)
grafoTest.addArista('A','C',3)
grafoTest.addArista('B','A',5)
grafoTest.addArista('B','C',2)
grafoTest.addArista('B','D',4)
grafoTest.addArista('C','A',3)
grafoTest.addArista('C','B',2)
grafoTest.addArista('C','D',6)
grafoTest.addArista('C','E',7)
grafoTest.addArista('D','B',4)
grafoTest.addArista('D','C',6)
grafoTest.addArista('D','E',8)
grafoTest.addArista('E','C',7)
grafoTest.addArista('E','D',8)

origenG = 'A'
destinoG = 'E'
path={}
visitados = []
visitados.append(origenG)

llaves = grafoTest.Aristas[origenG].keys()
print(llaves)
for i in llaves:
    path[i]={origenG : grafoTest.Aristas[origenG][i]}
print('Primera Interacion')
print(visitados)
print(path)
verticeAct = 'B'
llaves = grafoTest.Aristas[verticeAct].keys()
print(llaves)
for i in llaves:
    if i not in visitados:
        if i not in path: path[i]={}
        path[verticeAct]
        llaves = list (path[verticeAct].keys())
        acumulado = path[verticeAct][llaves[0]]
        
        path[i].update({verticeAct : grafoTest.Aristas[verticeAct][i]+ acumulado})
        if len(path[i]) == 2:
            kiss = list (path[i].keys())
            if kiss[0]>kiss[1]:
                del (path[i][ kiss[0]])
            elif kiss[0]<kiss[1]:
                del(path[i][kiss[1]])
            pass



print(path)      
exit()
