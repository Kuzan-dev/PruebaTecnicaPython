## Ejercicio 2
'''
  Se tiene un n ́umero natural n, crear una funci ́on que retorne una lista de todos 
  los pares de n ́umeros naturales que sumen el número n. n < 10**6
'''

n= 107

def Form1(n):
    pares = []
    for i in range(n // 2 + 1):
        pares.append((i, n - i))
    return pares

def Form2(n):
    return [(i, n - i) for i in range(n // 2 + 1)]


# Prueba de la función Form1
print(Form1(n)) #Metodo 1

# Prueba de la función Form2
print(Form2(n)) #Metodo 2