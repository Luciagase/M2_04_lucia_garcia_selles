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

print(len(fruta))
print(len(abecedario))

print('sandia' in fruta)
print('y' in abecedario)

fruta.insert(2,'kiwi')
print(fruta)
#Otra vez, las tuplas no se pueden modificar.

del fruta[4]
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

