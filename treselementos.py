#Archivo: treselementos.py
#fecha:08/04/2025
#proy.: estudio de algoritmos
#
# ordenar una matriz de tres elementos

# Función swap(int indice)
#cambia de orden dos elementos de una lista ya existente s
#
def swap(indice):
    a = s[indice]
    s[indice] = s[indice+1]
    s[indice+1] = a
n = []
 
# Bucle para tomar datos del teclado y guardarlos en la variable n de tipo lista
for i in range(6):
    n.append (int(input())) #append es un método de las listas

s = n # Voy a hacer dos intentos  de ordenar.Para tener
      # la lista original sin cambios, tendré que copiarla a otra lista
      # y así trabajamos con la copia
for i in range(5):    #Aquí se refleja el error p.ej. con [7, 5, 3]
    if s[i] > s[i+1]:
        a = s[i]    
        s[i] = s[i+1]
        s[i+1] = a
print(s)

s = n
for i in range(leg(n)-2):    #Aquí hacemos el repaso a la lista dos veces
    for j in range (len(n)-1):
        if s[j] > s[j+1]:
            a = s[j]       #Estas tres líneas son swap().
            s[j] = s[i+1]
            s[j+1] = a
print(s)

