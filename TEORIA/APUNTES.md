# Apuntes de la asignatura de SGSSI

## 1.- Introduccion

### 1.1.- ¿Qué es la seguridad informática?

```text
La seguridad informatico son todas las acciones que se toman para asegurar que los bienes y servicion son usados como se deben, solo por quienes deben y cumplen con las leyes y normas que se deben.
Todo con el objetivo de detectar riegos, garantizar el uso correcto, limitar las perdidas y cumplir con las leyes.
```

### 1.2.- ¿Quien se encarga?

#### 1.2.1.- El administrador de seguridad

```text
Identificar los bienes y servicios a proteger.
Realizar el plan y implementarlo.
```

#### 1.2.2.- La direccion

```text
La seguridad debe ser un objetivo estrategico
Invertir dinero
Organizar el departamento de seguridad
```

#### 1.2.3.- El usuario

```text
Formarse
Conocer las politicas de seguridad
Involucrarse
Conocer la legislacion.
```

### 1.3.- Analisis de riesgos

```text
Coste < Probabilidad * Valor
Solo en este caso se toman medidas.
```

### 1.4.- Principios de seguridad

#### 1.4.1.- Confidencialidad

```text
La informacion solo es leida por quien debe.
Se puede conseguir con cifrado.
```

#### 1.4.2.- Integridad

```text
La informacion no se modifica sin autorizacion.
Se puede conseguir con firmas digitales.
```

#### 1.4.3.- Disponibilidad

```text
La informacion esta disponible cuando se necesita.
Se puede conseguir con copias de seguridad.
```

#### 1.4.4.- Autenticidad

```text
La informacion es de quien dice ser.
Se puede conseguir con certificados.
```

#### 1.4.5.- No repudio

```text
No se puede negar que se ha hecho algo.
Se puede conseguir con firmas digitales.
```

## 2.- Introduccion al cifrado

### 2.1 Criptografia

```text
Cifrar la informacion
```

### 2.2 Criptoanalisis

```text
Tecnicas para descrifrar la informacion
```

### 2.3 Criptologia

```text
Criptografia + Criptoanalisis
```

### 2.4 Principios Kerkhoffs

```text
El sistema debe ser practicamente irrompible
La efectividad no debe depender de no conocer su diseño
La clave debe ser sencilla
Debe de dar como resultado algo alfanumerico
El sistema debe ser operable por una persona
El sistema debe ser facil de utilizar
```

### 2.5 Criptosistemas

```text
Simetrica o de clave privada: Una clave para encriptar y desencriptar
Asimetrica o de clave publica: Una clave para encriptar y otra para desencriptar
```

## 3.- Esteganografia

```text
Ocultar informacion de forma que sin conocer la clave no se sepa que hay informacion oculta.
```

### 3.1.- Antiguamente

```text
Ejemplos:
    Mensajes debajo del pelo
    Micro puntos en textos
    Plantillas
    Escoger caracteres en base a una regla
```

### 3.2.- Actualmente

```text
Ejemplos:
    Sustitucion de bits
        Modificar el bit menos significativo de los bytes de una imagen
    Insertar bits despues de un EOF
    Crear ficheros con informacion oculta
Recomendable usar criptografia antes de esteganografia
```

## 4.- Algoritmos resumen

### 4.1 - Funciones hash

```text
Tamaño constante independiente del tamaño del mensaje
Representa el contenido original
Si el contenido cambia el resumen cambia
Si el contenido es igual el resumen es igual
No se puede recuperar el contenido original
```

### 4.2 - Funciones

```text
Certificar la integridad
Almacenar contraseñas
Identificadr datos o archivos
Prueba de trabajo (Criptomonedas)
Firmas digitales
```

## 5.- Cifrado simetrico

### 5.1.- Clave privada

```text
Cifrado de flujo: Cifra un bit a la vez
Cifrado en bloque: dividir el mensaje en bloques.
Objetivos:
    Convertir el mensaje en ininteligible
    Recuperar la informacion cifrada
    Implementacion sencilla
Tecnicas:
    Transposicion: Cambiar el orden de los caracteres
    Sustitucion: Cambiar los caracteres por otros
```

## 6.- Cifrado asimetrico

### 6.1.- Clave Publica

```text
Dos claves por usuario
    Clave publica
    Clave privada
Relacionadas matematicamente
Lo que cifra una lo descifra la otra
Solo el destinatario puede leer el mensaje
Solo hay que almacenar una clave
Cualquiera puede usar la clave publica para enviar mensajes
No son necesarios canales seguros
La clave privada no se puede compartir
Es practicamente imposible deducir la clave privada a partir de la publica
Debe ser facil obtener la clave publica
Solo se debe cifrar con la publica ya que si cifras con la privada todo el mundo podra descifrarlo
Si alguien intercepta he intercambia las claves publicas puede leer los mensajes
    Usar canales seguros
    Usar un AC para validar las claves publicas
```

### 6.2.- Cifrado hibrido

```text
Mas rapidos que los de clave publica
Se crea una clave secreta que se usa para encriptar el mensaje y posteriormente se encripta la clave secreta con la clave publica y se envian ambas al destinatario
```

## 7.- Firma digital

### 7.1.- Introduccion

```text
Solo quien tiene la clave privada puede firmar un documento
No se puede falsificar
Cualquiera puede verificar una firma digital
No se pueden reutilizar las firmas
No se pueden modificar
No se pueden negar haber firmado
No se puede alterar un documento despues de firmarlo
Ademas de firmarlo se puede encriptar un mensaje.
    Criptografia asimetrica
    Criptografia hibrida
```

### 7.2.- Confianza de firmas

```text
Se usa PGP, GPG y similares
Un usuario certifica que la clave publica de otro usuario es de confianza
La confianza se propaga segun la confianza que demos a los usuarios
```

### 7.3.- Niveles de confianza

```text
Desconocido
    No conocemos al usuario
Ninguno
    No confiamos en el usuario
Marginal
    Nos fiamos del usuario por otros usuarios
Absoluto
    Nos fiamos del usuario
```

## 8.- Certificados

### 8.1.- Public Key Infraestructure

```text
Infraestructura de clave publica
Web of trust: Cada usuario certifica a otros usuarios
Certificados: Una entidad certifica a los usuarios
```

### 8.2.- Autoridad de Certificación

```text
Certifica que el usuario y la entidad son quienes dicen ser
Almacena las claves publicas de los usuarios
```

### 8.3.- Certificados

```text
La AC emite un certificado digital
En el certificado digital el AC firma la clave publica del solicitante con su clave privada.
```

### 8.4.- Agencia de Registro

```text
Independiente de AC
Verifica la identidad del solicitante
    Agencias tributarias, seguridad social, notarios, bancos, etc
```

### 8.5.- Certificados digitales X.509

```text
Es un estandar de certificados
Contiene una identidad y una clave publica
Es firmada por un CA lo que permite
    Firmar con la clave privada
    Establecer comunicaciones seguras
El CA debe mantener una base de datos con nombres distingidos y de CA confiables
Cadenas de confianza
Certificate Revocation List
```

### 8.6.- Certificate Revocation List

```text
Una lista publica con certificados revocados
    Razones:
        unspecified, 
        keyCompromise,
        cACompromise, 
        affiliationChanged, 
        superseded, 
        cessationOfOperation,
        certificateHold, 
        removeFromCRL, 
        privilegeWithdrawn, 
        aACompromise
```

### 8.6.- OCSP

```text
Permite validar el estado de un certificado
Es mas rapido que CRL
Se actualiza en tiempo real
Neceista una conexion a internet
Cada AC tiene su propio OCSP
Este servicio remite una peticion estandarizada
Es posible retener una respuesta hasta que esta expire y aun asi se puede usar
    Solucion: nonce
```

## 9.- Comunicaciones seguras

### 9.1.- Protocolos seguros

```text
Basados en TLS/SSL - X.509
    HTTPS
    S/MIME
    SMTPS
    POP3S
    IMAPS
    EAP-TLS
    LDAPS
    VPN
```

### 9.2.- TLS

```text
Transport Layer Security
El cliente le pide al servidor usar TLS
HTTP redirige del puerto 80 al 443
El cliente indica los crifrados que soporta
El servidor elige el cifrado
El servidor envia su certificado
El cliente comprueba el certificado
El cliente genera una clave simetrica
El cliente envia la clave simetrica cifrada con la clave publica del servidor
El servidor descifra la clave simetrica
El cliente y el servidor se comunican con la clave simetrica
```

### 9.3.- SSH

```text
Secure Shell
Se usa para conectarse a servidores remotos
Solo hace falta poner la clave publica en el servidor
Usando esa clave se manda la informacion cifrada
Usos:
    Acceso remoto
    Transferencia de ficheros
    Copiar archivos
    Tuneles
    Port fowarding
    Conexiones X11
```

## 10.- Bitcoin

### 10.1.- Introduccion

```text
Criptomoneda que usa cifrado asimetricos y algoritmos resumen
Usado tanto como libro de contabilidad como de moneda
```

### 10.2.- ¿Que es Bitcoin?

```text
Una red de pagos descentralizada.
Usa el protocolo Bitcoin
La moneda es bitcoin
```

### 10.3.- ¿La red Bitcoin?

```text
Libro de cuentas donde se escriben todos los pagos he impide su modificacion
Una copia del libro en cada nodo con las transacciones
Para escribir en el libro hace falta pasar una prueba de trabajo llamada mineria la cual por fuerza bruta resuelve un problema criptografico y recibe el bitcoin como pago por el trabajo y comision por las transacciones con maximo de 21 millones de bitcoins
Esta prueba se basa en hayar un hash el cual tiene que ser menor a un numero antes puesto que verifique todo el contenido del bloque. Esto se consigue alteranto un dato que va en todo los bloques de transacciones llanado nonce lo que hace que el hash cambie.
```

### 10.5.- Soluciones que aporta

```text
Todo el mundo tiene acceso a una cuenta
    Descentralizado
Desaparece la falta de privacidad
Da igual el pais
    Sin fronteras
Elimina la inflacion
    Suministro limitado
```

### 10.6.- Usos acutales

```text
Ahorro
Tranferencias internacionales
    Evitar pagos pequeños
    Pagos rapidos
Compras
Especulacion financiera
    Posibles perdidas
Certificados de propiedad
Certificados de existencia
```
