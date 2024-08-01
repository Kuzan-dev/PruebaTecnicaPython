## Ejercicio 1
''''
  Se tiene una matriz nxn de enteros, crear una función que retorne un arreglo cuyo primer elemento es la cantidad 
  de n ́umeros que aparecen solo una vez y cuyo segundo elemento la cantidad de terminos repetidos.
'''

def Form1(matriz):
    result = [0, 0]
    temp = []
    #Hallamos los elementos unicos y repetidos de la matriz
    for row in matriz:
        temp.extend(row)
    unique = set(temp)
    repet = []

    for val in unique.copy():
      cont = 0
      for j in temp:
         if val == j:
            cont += 1
            if cont > 1:
              repet.append(val)
              unique.remove(val)
              break #Salimos del bucle interno

    result[0] = len(unique)
    result[1] = len(repet)         
    return result

def Form2(matriz):
  temp = [x for row in matriz for x in row]

  count = {}

  for y in temp:
    if y in count:
      count[y] += 1
    else:
      count[y] = 1
  
  unique_count = sum(1 for val in count.values() if val == 1)
  repet_count = sum(1 for val in count.values() if val > 1)

  return [unique_count, repet_count]

# Matriz de prueba 1
Matriz1 = [[2,2],
          [2,2]]

print(Form1(Matriz1)) #Metodo 1
print(Form2(Matriz1)) #Metodo 2


# Matriz de prueba 2
Matriz2 = [[2,1,3],
          [4,5,2],
          [6,6,6]]

print(Form1(Matriz2)) #Metodo 1
print(Form2(Matriz2)) #Metodo 2
