## Ejercicio 2
'''
  Se tiene un n ́umero natural n, crear una funci ́on que retorne una lista de todos 
  los pares de n ́umeros naturales que sumen el número n. n < 10**6
'''

def Form1(n):
  try:
    # Verificación de que n es un número natural
    if not isinstance(n, int) or n <= 0:
      raise ValueError("n debe ser un número natural (entero positivo)")
    
    pares = []
    for i in range(n // 2 + 1):
        pares.append((i, n - i))
    return pares
  except ValueError as e:
    print(f"Error en el número n: {e}")

def Form2(n):
  try:
    # Verificación de que n es un número natural
    if not isinstance(n, int) or n <= 0:
      raise ValueError("n debe ser un número natural (entero positivo)")
    
    return [(i, n - i) for i in range(n // 2 + 1)]
  except ValueError as e:
    print(f"Error en el número n: {e}")

# Pruebas para n =107
n = 107

# Prueba de la función Form1
print(Form1(n)) #Metodo 1

# Prueba de la función Form2
print(Form2(n)) #Metodo 2