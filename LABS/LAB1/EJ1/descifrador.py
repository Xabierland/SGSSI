array1=[
    'e',
    'a',
    'o',
    'l',
    's',
    'n',
    'd',
    'r',
    'u',
    'i',
    't',
    'c',
    'p',
    'm',
    'y',
    'q',
    'b',
    'h',
    'g',
    'f',
    'v',
    'j',
    'ñ',
    'z',
    'x',
    'k',
    'w'
]

def letras_por_frecuencia(texto):
    # Inicializamos un diccionario para contar las frecuencias de las letras
    frecuencia_letras = {}
    
    # Eliminamos los espacios y convertimos el texto a minúsculas para considerar las letras sin distinción de mayúsculas/minúsculas
    texto = texto.replace(" ", "").lower()
    
    # Contamos las frecuencias de las letras
    for letra in texto:
        if letra.isalpha():
            frecuencia_letras[letra] = frecuencia_letras.get(letra, 0) + 1
    
    # Ordenamos el diccionario por frecuencia de aparición
    letras_ordenadas = sorted(frecuencia_letras.items(), key=lambda x: x[1], reverse=True)
    
    # Extraemos solo las letras ordenadas en una lista
    resultado = [letra[0] for letra in letras_ordenadas]
    
    return resultado

def reemplazar_caracteres(texto, array1, array2):
    # Creamos un diccionario de mapeo para los caracteres
    mapeo = dict(zip(array1, array2))

    # Creamos una lista de caracteres reemplazados
    resultado = [mapeo.get(char, char) for char in texto]

    # Convertimos la lista de caracteres reemplazados de nuevo a una cadena
    resultado = ''.join(resultado)

    return resultado

# Abre el archivo "texto.txt" en modo lectura
with open("texto.txt", "r") as archivo:
    # Lee el contenido del archivo
    texto = archivo.read()

# Llama a la función letras_por_frecuencia con el contenido del archivo
array2 = letras_por_frecuencia(texto)

resultado = reemplazar_caracteres(texto.lower(), array1, array2)

print(array1)
print()
print(array2)
print()
print(texto.lower())
print()
print(resultado)