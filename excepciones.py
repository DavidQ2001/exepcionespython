

    


#keyError: Error en clave(intenta acceder a una clave inexsistente)
#FileNoteFoundError: intenta acceder a un archivo que no existe 
lista = [1,2,3,4,5]
try:
    indice = int(input("ingrese el numero del indice"))
    elemento = lista[indice]
    print("el elemento en el inidce {} es: {}: ".format(indice, elemento))
except IndexError:
    print("Error el indice proporcionadio esta fuera del rango de la lista")
except ValueError:
    print("Error ingrese un numero valido como indice")
finally:
    print("Exitoso")
    
try:
    numero = 19
    caracter = "10"
    resultado = numero + caracter
except TypeError as e:
    print("Error",e)
    
diccionario = {
    'clave1': 'juan1',
    'clave2': 'juan2'
}
try:
    clave = input("ingrese la clave para acceder al diccionario")
    valor = diccionario[clave]
    print("el valor asociado a la clave {} es: {}".format(clave,valor))
    
except KeyError:
    print("Error la clave non existe en el diccionario")
    
    

