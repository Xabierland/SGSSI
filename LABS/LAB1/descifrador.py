import collections

# Función para calcular las frecuencias de las letras en el texto
def calcular_frecuencias_personalizadas(texto):
    frecuencias = collections.Counter(texto)
    return frecuencias

# Función para descifrar el texto utilizando análisis de frecuencia y una tabla de frecuencias personalizada
def desencriptar_por_frecuencia(cifrado, tabla_frecuencias):
    # Calcular las frecuencias de las letras en el texto cifrado
    frecuencias_cifrado = calcular_frecuencias_personalizadas(cifrado)
    
    # Ordenar las letras por frecuencia descendente
    letras_ordenadas = sorted(frecuencias_cifrado.keys(), key=lambda letra: frecuencias_cifrado[letra], reverse=True)
    
    # Suponemos que la letra más común en la tabla de frecuencias personalizada es 'e', por lo que intentamos descifrar 'e' como 'e' en el texto original
    letra_mas_comun_cifrado = letras_ordenadas[0]
    letra_mas_comun_original = max(tabla_frecuencias, key=tabla_frecuencias.get)
    
    # Calcular el desplazamiento necesario para descifrar la letra más común como 'e' usando la tabla de frecuencias personalizada
    desplazamiento = ord(letra_mas_comun_original) - ord(letra_mas_comun_cifrado)
    
    # Descifrar el texto cifrado
    texto_desencriptado = ''
    for letra in cifrado:
        if letra.isalpha():
            letra_desencriptada = chr(((ord(letra) - ord('a') - desplazamiento) % 26) + ord('a'))
            texto_desencriptado += letra_desencriptada
        else:
            texto_desencriptado += letra
    
    return texto_desencriptado

# Leer el texto cifrado desde un archivo de texto llamado "texto.txt"
with open("texto.txt", "r") as archivo:
    texto_cifrado = archivo.read()

# Tabla de frecuencias personalizada
frecuencias_personalizadas = {
    'e': 16.78,
    'a': 11.96,
    'o': 8.69,
    'l': 8.37,
    's': 7.88,
    'n': 7.01,
    'd': 6.87,
    'r': 4.94,
    'u': 4.80,
    'i': 4.15,
    't': 3.31,
    'c': 2.92,
    'p': 2.776,
    'm': 2.12,
    'y': 1.54,
    'q': 1.53,
    'b': 0.92,
    'h': 0.89,
    'g': 0.73,
    'f': 0.52,
    'v': 0.39,
    'j': 0.30,
    'ñ': 0.29,
    'z': 0.15,
    'x': 0.06,
    'k': 0.00,
    'w': 0.00
}

# Aplicar el análisis de frecuencia utilizando la tabla de frecuencias personalizada
texto_desencriptado = desencriptar_por_frecuencia(texto_cifrado, frecuencias_personalizadas)
print(texto_desencriptado)
