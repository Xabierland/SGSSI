# Laboratorio 1 - Cifrado II

## 1. Asegurando las comunicaciones mediante GPG

### ¿Qué quiere decir [ultimate]?

El ultimate no es mas que el nivel de confianza que tiene la clave en el sistema. Al haber creado nosotros mismo la clase se le da nivel de confianza [ultimate] pero podria ser tambien : [unknown], [undefined] [never] [marginal] [full]

### Cifrad este archivo PDF y enviároslo entre vosotros de forma que consigáis los principios de seguridad Confidencialidad, Integridad, Autenticidad y No Repudio. Razonad qué habéis tenido que hacer para conseguir cada uno de ellos

```bash
# Encripta el mensaje
gpg --encrypt Cifrado-II.pdf #Si necesario redigir con > archivo

# Deencriptar
gpg --decrypt Cifrado-II.pdf.gpg > archivo.pdf

```

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

```bash
# Crear clave
gpg --generate-key

gpg --list-keys
    gpg: checking the trustdb
    gpg: marginals needed: 3  completes needed: 1  trust model: pgp
    gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
    gpg: next trustdb check due at 2025-09-26
    /home/xabier/.gnupg/pubring.kbx
    -------------------------------
    pub   rsa3072 2023-09-27 [SC] [expires: 2025-09-26]
        05F7D3156F6C75549C45EA61567737DF04245674
    uid           [ultimate] Xabier Gabiña <xabierland@gmail.com>
    sub   rsa3072 2023-09-27 [E] [expires: 2025-09-26]

gpg --armor --export 05F7D3156F6C75549C45EA61567737DF04245674
```

```text
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
SVNW4UFfZ82oTanmLzbMuJOtACM/HGx8Hsnyjb4=
=hQLR
-----END PGP PUBLIC KEY BLOCK-----
```

```bash
gpg --edit-key 92B7ED6082748793F939DA95D8D4311231CFC203
    trust
    4
    quit

gpg --list-key
```

## 3. Firmas GPG

### ¿Para qué sirve ese segundo fichero? ¿Cómo se usa?

Es el archivo que se usa para verificar que tanto el archivo como su destinatario es el que dice ser y que no se ha modificado ni subido por otra persona que no sea el remitente.

### Usa tus claves GPG para firmar un commit del repositorio GitHub en el que estás desarrollando tu sistema web para las entregas, de modo que aparezca como “Verified” en GitHub

```bash
# Importamos la clave publica a github
git commit -a -S -m "Mensaje Verificado"
```

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
