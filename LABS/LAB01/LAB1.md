# Laboratorio 1 - Cifrado I

## 1. Criptoanálisis mediante análisis de frecuencias

### Crea un programa que descifre el siguiente mensaje mediante análisis de frecuencias

```bash
python3 contador.py 
x: 103
e: 94
k: 74
i: 70
c: 68
j: 55
t: 54
a: 47
r: 41
z: 38
h: 32
n: 32
p: 22
d: 19
q: 13
o: 13
v: 10
s: 7
g: 5
u: 3
m: 2
f: 1
l: 1

python3 modificar_texto.py X e
python3 modificar_texto.py E a
python3 modificar_texto.py T l 
python3 modificar_texto.py A d 
python3 modificar_texto.py J n
python3 modificar_texto.py K r 
python3 modificar_texto.py V y 
python3 modificar_texto.py N s 
python3 modificar_texto.py Z u
python3 modificar_texto.py H t
python3 modificar_texto.py I o
python3 modificar_texto.py Q b
python3 modificar_texto.py R c
python3 modificar_texto.py C i
python3 modificar_texto.py P m
python3 modificar_texto.py D p
python3 modificar_texto.py O f
python3 modificar_texto.py S q
python3 modificar_texto.py G j
python3 modificar_texto.py U g
python3 modificar_texto.py F s
python3 modificar_texto.py M h
```

#### Resultado

con durruti moria el dirigente que, a su manera, mejor espresaba como combatir al fascismo desde un criterio de independencia
de clase, a diferencia del colaboracionismo frentepopulista de la direccion anarquista.
durruti fue un factor de primer orden en el papel de la clase obrera en catalunya en julio de 1936. pero durruti, como ocurre con
las personalidades en la historia, no cayo del cielo. personificaba la tradicion revolucionaria de la clase obrera. su enorme
popularidad entre la clase trabajadora, reflejada en el entierro multitudinario en barcelona el 22 de noviembre de 1936,
muestra esa identificacion. su muerte fue sin duda un golpe objetivo al proceso revolucionario en marcha. sin durruti quedo mas
libre el camino para que el estalinismo, con la complicidad del gobierno del frente popular y de la direccion anarquista,
terminara en mayo de 1937 la tarea de liquidar la revolucion, desmoraliLando a la clase obrera y facilitando con ello el posterior
triunfo franquista.

## 2. Esteganografía y algoritmos resumen

### Hay un mensaje importante de Buenaventura Durruti para vosotros en una de las imagenes del directorio imagenes.zip disponible en eGela. El mensaje ha sido introducido mediante el programa Stegosuite de Ubuntu, sin contraseña. La imagen que contiene el mensaje se corresponde con el Hash (MD5) e5ed313192776744b9b93b1320b5e268. ¿Qué archivo es? ¿Qué dice la frase?

El hash MD5 e5ed313192776744b9b93b1320b5e268 se encontró en el archivo: ./imagen/imagen22.jpg con la frase "Al Fascismo no se le discute, se le destruye." Buenaventura Durruti

### Si quieres escribir un mensaje secreto en una imagen, y garantizar al destinatario que nadie lo ha modificado, ¿Qué pasos seguirías?

Si lo unico que intentamos evitar es que no haya sido modificado la mejor forma es usando el md5 que no es mas que un string de 128bits que se forma tras realizar ciertas operaciones con el conteniendo de un fichero bien sea una imagen como es el caso o un pdf, txt.

### ¿Sería posible incorporar en el contenido de un fichero su propio resumen criptográfico? Esto es, ¿Podría ponerse en el texto de este enunciado el resumen criptográfico que le corresponda al propio enunciado para que pudiérais comprobar su autenticidad?

No ya que al modifiar el fichero para añadir su resumen criptografico o md5 estariamos modificando el contenido del fichero lo que alteraria su md5 haciendo que estos no coincidan.
