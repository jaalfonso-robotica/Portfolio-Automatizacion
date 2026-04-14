import os
os.system ('cls') 

#Crea un programa que pida al usuario un número real y muestre su raíz cuadrada (si es positivo)
#o un aviso de que no se puede calcular la raíz cuadrada (si es negativo).

numero =float(input('Introduce un numero: '))

if numero <=0:
    print ('No se puede calcular')

else:
    raiz = numero ** (0.5)
    print (f'La raiz de {numero} es {raiz}')