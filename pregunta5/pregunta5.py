from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
#Leemos 
data = pd.read_csv('/home/roy/examen2/dataset.csv', header=None)
data.columns = ['clase', 'edad','menopausia','tam_tumor','inv_nodos','nodos_caps','grado_maligno','pecho','lado', 'irradiacion']
#preprosesamiento
data.dropna()
data.clase.replace(('no-recurrence-events','recurrence-events'),(0, 1), inplace=True)
data.edad.replace(('10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99'),(1,2,3,4,5,6,7,8,9), inplace=True)
data.menopausia.replace(('premeno','ge40','lt40'),(0,1,2), inplace=True)
data.tam_tumor.replace(('0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59'),(1,2,3,4,5,6,7,8,9,10,11,12), inplace=True)
data.inv_nodos.replace(('0-2','3-5','6-8','9-11','12-14','15-17','18-20','21-23','24-26','27-29','30-32','33-35','36-39'),(1,2,3,4,5,6,7,8,9,10,11,12,13), inplace=True)
data.nodos_caps.replace(('yes','no'), (1,0), inplace=True)
data.pecho.replace(('left','right'), (0,1), inplace=True)
data.lado.replace(('left_up','left_low','central','right_low','right_up'),(1,3,5,7,9), inplace=True)
data.irradiacion.replace(('yes','no'),(1,0) , inplace=True)
filtro=data['nodos_caps']!='?'
data=data[filtro]
data=data[data['lado']!='?']

#Asignamos datos valores
X = np.array(data.values[0:180, 1:10], dtype='float')

#Asignamos Clase
y = np.array(data.values[0:180,0], dtype='float')

#Clasificador
clasificador = MLPClassifier(solver='lbfgs')

#Entrenamos
clasificador.fit(X,y)
pred = clasificador.predict([[9,2,6,10,1,2,0,3,0],[6,0,1,7,0,1,0,1,1]])
print("PREDICCION: ", pred)
"""USANDO NEIGHBORS de SKLEARN"""
from sklearn import neighbors as ne
nclasific = ne.KNeighborsClassifier(n_neighbors=6)
nclasific.fit(X,y)
s = nclasific.predict([[9,2,6,10,1,2,0,3,0],[6,0,1,7,0,1,0,1,1]])


"""MATRIZ DE CONFUSION"""
from sklearn.metrics import confusion_matrix
matriz = confusion_matrix([1,0], pred)
print("MATRIZ DE CONFUSION")
print(matriz)










