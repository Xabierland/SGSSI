# Laboratorio 1 - Cifrado II

## 1. Asegurando las comunicaciones mediante GPG

### ¿Qué quiere decir [ultimate]?

El ultimate no es mas que el nivel de confianza que tiene la clave en el sistema. Al haber creado nosotros mismo la clase se le da nivel de confianza [ultimate] pero podria ser tambien : [unknown], [undefined] [never] [marginal] [full]

### Cifrad este archivo PDF y enviároslo entre vosotros de forma que consigáis los principios de seguridad Confidencialidad, Integridad, Autenticidad y No Repudio. Razonad qué habéis tenido que hacer para conseguir cada uno de ellos

1. Confidencialidad:
La confidencialidad implica que solo las partes autorizadas puedan acceder al contenido del archivo. Para lograr la confidencialidad:
Ambas partes deben tener sus propias claves GPG (pares de claves pública y privada) generadas.
El remitente cifra el archivo PDF utilizando la clave pública del destinatario con el comando gpg --encrypt --recipient destinatario@email.com archivo.pdf.
Luego, el remitente envía el archivo cifrado al destinatario de manera segura (por ejemplo, a través de un canal de comunicación cifrado o una conexión segura).

2. Integridad:
La integridad garantiza que el archivo no ha sido alterado durante la transmisión. Para lograr la integridad:
Antes de enviar el archivo cifrado, el remitente debe calcular un resumen de hash (hash digest) del archivo original, utilizando una función de hash como MD5: md5sum archivo.pdf.
El remitente envía tanto el archivo cifrado como el valor del hash a través de un canal seguro.
El destinatario puede calcular un nuevo resumen de hash del archivo cifrado recibido y compararlo con el valor del hash original enviado por el remitente. Si coinciden, la integridad se mantiene.

3. Autenticidad:
La autenticidad asegura que el archivo proviene de la fuente pretendida y no ha sido falsificado. Para lograr la autenticidad:
El remitente firma digitalmente el archivo PDF original utilizando su clave privada con el comando gpg --detach-sign archivo.pdf.
El remitente envía tanto el archivo cifrado como el archivo de firma digital (archivo.pdf y archivo.pdf.asc) al destinatario a través de un canal seguro.
El destinatario verifica la firma digital del remitente utilizando la clave pública del remitente con el comando gpg --verify archivo.pdf.asc. Si la verificación es exitosa, se asegura la autenticidad.

4. No Repudio:
El principio de no repudio garantiza que el remitente no pueda negar el envío del archivo. Para lograr el no repudio:
La firma digital del remitente, verificada por el destinatario, proporciona evidencia de que el remitente envió el archivo.
Esto significa que el remitente no puede negar haber enviado el archivo, ya que la firma digital se basa en su clave privada.

## 2. Confianza sobre las claves

### En cada grupo se designará a uno de los estudiantes como “de confianza”. Ese estudiante enviará su clave pública al profesor. El grupo tendrá que conseguir que al enviar las claves de los otros estudiantes al profesor aparezcan como de confianza en el anillo de claves del profesor ([full]). Razonad qué habéis tenido que hacer para conseguirlo

## 3. Firmas GPG

### ¿Para qué sirve ese segundo fichero? ¿Cómo se usa?

Es el archivo que se usa para verificar que tanto el archivo como su destinatario es el que dice ser y que no se ha modificado ni subido por otra persona que no sea el remitente.

### Usa tus claves GPG para firmar un commit del repositorio GitHub en el que estás desarrollando tu sistema web para las entregas, de modo que aparezca como “Verified” en GitHub


## 4. Otras funcionalidades GPG

### ¿Cómo se exporta una clave GPG para poder usarla en otro equipo?

```bash
gpg --export -a "Xabier Gabiña" > clave_publica.asc
```

### ¿Cómo revocarías tu clave?

```bash
# Revocar la clave
gpg --gen-revoke "Xabier Gabiña"

# Para hacer efectiva la revocacion importamos la revocacion
gpg --import archivo_de_revocacion.asc

# Actualizar los servidores
gpg --send-keys nombre_de_la_clave
```

### ¿Como cifrarías este documento de manera simétrica, y qué pasos seguirias para que el receptor lo descifre?

```bash
gpg --symmetric Cifrado-II.pdf
```
