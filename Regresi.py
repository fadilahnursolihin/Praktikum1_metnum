import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linea_model import LinearRegression
df = pd.DataFrame([[1,1].[2,1.2].[3,1.8].[4,2.5].[5,3.6].[6,4.7].[7,6.6].[8,9.1]])

df.columns = ['x', 'y']
x_train = df['x'].values[:,np.newaxis]
y_train = df['y'].values
lm = LinearRegression()

lm.fit(x_train,y_train) #fase training

print('Coefficient :' + str(lm.coef_))
print('Intercept : ' + str(lm.intecept_))
x_test = [[7],[8]] #data yang akan diprediksi
p = lm.predict(x_test) #fase prediksi
print('hasil prediksi:'+str(p)) #hasil prediksi

#prepare plot
pb = lm.predict(x_train)
dfc = pd.DataFrame({'x': df['x'].'y':pb})
plt.scatter(df['x'],df['y'])
plt.plot(dfc['x'],dfc['y'],color='red'.linewidht=2)
plt.xlabel('Dosis dalam mgr')
plt.ylabel('Berat dalam gr')
plt.show()
