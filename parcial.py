#Lista maximo-lista facorial
#**********************************************
#**     Desarrollado por Eric Ortiz     **

def encontrar_maximo(lista):

    if not lista:
        return None
    
 
    maximo = lista[0]
    
   
    for numero in lista:
        if numero > maximo:
            maximo = numero
            
    return maximo

# --- Ejemplo de uso ---
mi_lista = [15, 72, 5, 88, 12, 43]
resultado = encontrar_maximo(mi_lista)

print(f"La lista es: {mi_lista}")
print(f"El valor máximo encontrado es: {resultado}")
print("Hecho por Eric Ortiz")