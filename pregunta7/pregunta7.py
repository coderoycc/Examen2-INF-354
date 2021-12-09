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


#designamos X solo tomamos cordenadas 2D
X = np.array(data.values[0:100, 1:3], dtype='float')
print(X)
#En y tomamos la clase
y = np.array(data.values[0:100,0], dtype='float')

cantidad_vecinos = 6
#importamos las librerias necesarias
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

#Instanciamos KNN
knn = NearestNeighbors(n_neighbors=cantidad_vecinos)
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)
knn.fit(X_train,y_train)

clasi = KNeighborsClassifier(6)
clasi.fit(X_train, y_train)

pred = clasi.predict(X_test)

#Matriz de confusion 
print("Matriz: ",confusion_matrix(y_test, pred))





