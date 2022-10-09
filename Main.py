#1) Trabajemos con listas y tuplas
fruta = ['pera','mango','manzana','chirimoya']
abecedario = ('a','b','c','d')

print(fruta)
print(abecedario)

print(fruta[1])
print(abecedario[-2])

fruta[0] = 'sandia'
print(fruta)
#No se puede modificar un elemento de una tupla porque las tuplas son basicamente listas inmutables. Conclusión, si intento modificarlo me va ha dar error y como quiero que el código me siga compilando y no se me atasque pues he tenido que borrar esa parte.
#TypeError: 'tuple' object does not support item assignment

print(len(fruta))
print(len(abecedario))

print('sandia' in fruta)
print('y' in abecedario)

fruta.insert(2,'kiwi')
print(fruta)
#Otra vez, las tuplas no se pueden modificar.

fruta.clear()
print(fruta)
#Las tuplas no son modificables.



#2) Trabajemos con sets y diccionarios
flores={'Margarita','Azucena','Azalea','Dalia'}
persona={
  'nombre':'Pepe',
  'edad':26,
  'trabajo':'ninguno',
  'ciudad':'Gotham',
  'mascotas':['Lolo','Lola']
}

print(flores)
print(persona)

#No se puede pedir un elemento ordenado de un set porque los sets no tienen orden. Da error.
print(persona['nombre'])

#No se puede modificar los elementos de un set así que da error.
persona['edad'] = 30
print(persona)

print(len(flores))
print(len(persona))

print('Dalia' in flores)
print('Juan' in persona)

flores.add('Rosa')
print(flores)
persona['genero'] = 'Masculino'
print(persona)
flores.clear()
print(flores)
persona.clear()
print(persona)



#3)Realizar un programa que pida al usuario 3 números que pueden ser flotantes (no es necesario realizar bucles aún, podemos repetir el código), estos números se deberán introducir en una lista. Cuando se haya finalizado la introducción de los datos, se mostrará el sumatorio de toda la lista. Guardar el sumatorio en una variable que se llame "sumatorio"
numeros=(input('Escribe tres numeros:'))
lista=list(numeros)
for i in range(len(lista)):
    lista[i] = float(lista[i])
sumatorio=sum(lista)
print(sumatorio)


#4)Sobre el ejercicio anterior, queremos mostrar la media aritmética de los elementos de esa lista. Indicar la instrucción necesaria para obtenerla.
#Para poder calcular la media con cualquier número de elementos sin restrigir solo a 3 elementos se utiliza len() que hace referencia al número de elementos de una lista.
media=sum(lista)/len(lista)
print(media)