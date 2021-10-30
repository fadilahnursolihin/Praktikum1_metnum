import numpy as np
import matplotlib.pyplot as plt
from math import e #Untuk memanggil bilangan eksponen natural (e)

# Mendefinisikan fungsi
def f(x):
    return e**x-5*x**2

# Sesi Input Nilai Awal yang dikonversi ke pecahan
x0 = float(input('x0:  '))
x1 = float(input('x1:  '))
eps = float(input('epsilon : '))

#Metode Regulafalsi
def regulafalse(x0,x1,eps):
    step = 1
    print('\n\n*** --METODE REGULAFALSI-- ***')
    condition = True
    while condition:
        x2 = x1-(f(x1)*(x1-x0)/(f(x1)-f(x0)))
        print('Interation-%d, x2 = %0.6f and f(x2) =%0.6f' % (step, x2, f(x2)))
        if f(x0) * f(x2) <0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > eps

     print('\n Akar Persamaan Tersebut : %0.8f' % x2)

# Menggambar fungsi
rr= np.linspance(0, 2, 100) #masukan nilai tebak awal
plt.plot(rr, f(rr))
plt.show()
plt.savefig("fungsi.png") #untuk menyimpan gambar fungsi

# Pengecekan nilai awal
if f(x0) * f(x1) > 0.0:
    print('Nilai yang diprediksi tidak mengurung akar')
    print('Silahkan mencoba ulang prediksi nilai baru')
else:
    regulafalse(x0,x1,eps)