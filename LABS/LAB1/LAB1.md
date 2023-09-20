# Laboratorio 1 - Cifrado I

## 1. Criptoanálisis mediante análisis de frecuencias

### Crea un programa que descifre el siguiente mensaje mediante análisis de frecuencias



## 2. Esteganografía y algoritmos resumen

### Hay un mensaje importante de Buenaventura Durruti para vosotros en una de las imagenes del directorio imagenes.zip disponible en eGela. El mensaje ha sido introducido mediante el programa Stegosuite de Ubuntu, sin contraseña. La imagen que contiene el mensaje se corresponde con el Hash (MD5) e5ed313192776744b9b93b1320b5e268. ¿Qué archivo es? ¿Qué dice la frase?

El hash MD5 e5ed313192776744b9b93b1320b5e268 se encontró en el archivo: ./imagen/imagen22.jpg con la frase "Al Fascismo no se le discute, se le destruye." Buenaventura Durruti

### Si quieres escribir un mensaje secreto en una imagen, y garantizar al destinatario que nadie lo ha modificado, ¿Qué pasos seguirías?

Si lo unico que intentamos evitar es que no haya sido modificado la mejor forma es usando el md5 que no es mas que un string de 128bits que se forma tras realizar ciertas operaciones con el conteniendo de un fichero bien sea una imagen como es el caso o un pdf, txt.

### ¿Sería posible incorporar en el contenido de un fichero su propio resumen criptográfico? Esto es, ¿Podría ponerse en el texto de este enunciado el resumen criptográfico que le corresponda al propio enunciado para que pudiérais comprobar su autenticidad?

No ya que al modifiar el fichero para añadir su resumen criptografico o md5 estariamos modificando el contenido del fichero lo que alteraria su md5 haciendo que estos no coincidan.
