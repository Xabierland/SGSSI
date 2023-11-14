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

* Criptomoneda que usa cifrado asimetricos y algoritmos resumen
* Usado tanto como libro de contabilidad como de moneda

### 10.2.- ¿Que es Bitcoin?

* Una red de pagos descentralizada.
* Usa el protocolo Bitcoin
* La moneda es bitcoin


### 10.3.- ¿La red Bitcoin?

Libro de cuentas donde se escriben todos los pagos he impide su modificacion
Una copia del libro en cada nodo con las transacciones
Para escribir en el libro hace falta pasar una prueba de trabajo llamada mineria la cual por fuerza bruta resuelve un problema criptografico y recibe el bitcoin como pago por el trabajo y comision por las transacciones con maximo de 21 millones de bitcoins
Esta prueba se basa en hayar un hash el cual tiene que ser menor a un numero antes puesto que verifique todo el contenido del bloque. Esto se consigue alteranto un dato que va en todo los bloques de transacciones llanado nonce lo que hace que el hash cambie.

### 10.5.- Soluciones que aporta

* Todo el mundo tiene acceso a una cuenta
  * Descentralizado
* Desaparece la falta de privacidad
* Da igual el pais
  * Sin fronteras
* Elimina la inflacion
  * Suministro limitado

### 10.6.- Usos acutales

* Ahorro
* Tranferencias internacionales
  * Evitar pagos pequeños
  * Pagos rapidos
* Compras
* Especulacion financiera
  * Posibles perdidas
* Certificados de propiedad
* Certificados de existencia

## 11.- Seguridad en Sistemas Web

### 11.1.- Pentesting

Intentar penetrar en un sistema utilizando las mismas herramientas que un atacante para descubrir vulnerabilidades y arreglarlas.

### 11.2.- Principales vulnerabilidades

* Rotura de control de acceso
* Fallos criptograficos
* Inyeccion
* Diseño inseguro
* Configuracion de seguridad insuficiente
* Componenetes vulnerables y obsoletos
* Fallos de identificacion y autenticacion
* Fallos en la integridad de datos y software
* Fallos en la monitorizacion de la seguridad

### 11.3.- Rotura de control de acceso

#### 11.3.1.- Desripcion

Obligar al usuario a actuar solo dentro de unos limintes establecidos

#### 11.3.2.- Ejemplos

* Violar el priniipio de menor privilegio
* Acceso a recursos no autorizados
* Acceso a recursos de otros usuarios
* Escalada de privilegios

#### 11.3.3.- Prevencion

* Denegar por defecto resursos
* Controlar el acceso a los recursos
* Controlar el acceso a los datos
* Registrar los accesos
* Limitar el numero de intentos

### 11.4.- Fallos criptograficos

#### 11.4.1.- Descripcion

Exponer datos por no usar metodos criptograficos adecuados.

#### 11.4.2.- Ejemplos

* Almacenar datos en texto plano
* No usar canales seguros
* Usar algoritmos debiles
* Usar claves debiles
* Usar claves por defecto
* No gestionar las claves
  * Generacion
    * Evitar algoritmos debiles
  * Distribucion
    * Usar conexiones seguras
  * Uso
    * Solo las usan las personas autorizadas
  * Almacenamiento
    * Servicios en la nuve
    * HSM
  * Destruccion
    * Cuando una clave caduca se crea otra y se destruye la anterior encriptando los datos con la nueva clave.
* Certificados no validos
* Usar contraseñas en vez de claves
* Semillas no suficientemente aleatorias

#### 11.4.3.- Prevencion

* Gestionar las claves
  * No escribir las claves en el codigo
  * Principio de menor privilegio
  * Usar HSM
  * Automatizar la gestion de claves
  * Dividir el trabajo en varias personas
  * Dividir las claves en varias partes
* Clasificar los datos segun la sensibilidad
* Almacenar la menor cantidad de datos posible
* Cifrar todos los datos.
* Usar algoritmos criptograficos actuales
* Cifrar la transmision de datos
* No permitir el usao de cache
* Almacenar la contraseñas seguramente
* Usar semilals con mucha entropia

### 11.5.- Inyeccion

#### 11.5.1.- Descripcion

Introducir codigo en un sistema para que se ejecute.

#### 11.5.2.- Ejemplos

* Los datos no se validas, filtran o limpian
* No se parametrizan las consultas

#### 11.5.3.- Prevencion

* Revisar el codigo
* Usar testeos automatizados
* Usar herramientas de despliegue continuo
* Usar APIs seguras.
* Validar inputs
* Limitar consultas

### 11.6.- Diseño inseguro

#### 11.6.1.- Descripcion

Fallos en el diseño, antes del codigo

### 11.7.- Configuracion de seguridad insuficiente

#### 11.7.1.- Descripcion

Las configuraciones por defecto no son seguras

#### 11.7.2.- Ejemplos

* Permisos inadecuados
* Funcionalidades no desactivadas
* Cuentas por defecto
* Errores demasiado informativos
* Sistemas desactualizados
* Frameworks desactualizados o mal configurados
* Cabeceras HTTP mal configuradas

#### 11.7.3.- Prevencion

* Desarrollo automatizados y despliegue continuo
* Sistema minimalista

### 11.8.- Componenetes vulnerables y obsoletos

#### 11.8.1.- Descripcion

Usar componentes que tienen vulnerabilidades conocidas

#### 11.8.2.- Ejemplos

* No se conocen las versiones que usamos
* El software no tiene soporte, es vulnerable y obsoleto

#### 11.8.3.- Prevencion

* Quitar dependeciar innecesarias
* Inventario actualizado de componenetes de manera automatizada
* Solo componentes de confianza

### 11.9.- Fallos de identificacion y autenticacion

#### 11.9.1.- Descripcion

No se implementa bien la identificacion, autenticacion y gestion de sesion.

#### 11.9.2.- Ejemplos

* Permite ataques de fuerza bruta
* Contraseñas debiles
* Mecanismo de recuperacion de contraseña debil
* Almacenar contraseña en texto plano
* No usa autenticacion multifactor
* Exponer datos en la URL
* No invalidar la sesion

#### 11.9.3.- Prevencion

* Autenticacion multifactor
* No hacer despliegeus con credenciales por defecto
* Implementar validaciones "ligeras"
* Tener una buena politica de contraseñas
* Limitar los intentso de login

### 11.10.- Fallos en la integridad de datos y software

#### 11.10.1.- Descripcion

No se comprueba la integridad de los datos y software

#### 11.10.2.- Ejemplos

* Auto-Actualizacion sin test de integridad

#### 11.10.3.- Prevencion

* Usar firmas digitales para verificar el software
* Gestores de librerias
* Controles de integridad adecaudos en IC/DC
* No se envian datos a clientes sin firmar

### 11.11.- Fallos en la monitorizacion de la seguridad

#### 11.11.1.- Descripcion

No se monitoriza la seguridad

#### 11.11.2.- Ejemplos

* No se guardan eventos auditables
* Los errores no se guardan correctamente
* No se monitorea todo el sistema
* Sin copia de seguridad
* No hay respuestas automaticas a ataques
* No se usan herramientas de pentesting
* No se detectan amenazas a tiempo real

#### 11.11.3.- Prevencion

* Asgurar fallos de login, control de acceso, validaciones, etc
* Asegurar correcta generacion de logs
* Usar controles de integridad
* Establecer e implementar planes de respuesta a incidentes


## 12.- Seguridad Fisica

### 12.1.- Introduccion

* Proteger los activos fisicos
* Aplicar barreas fisicas y procedimientos de seguridad

Ejemplo: Camara acorazada en la CIA o centro de datos de google

* Debe ser coherente con el valor
* Medidas equilibradas
* Se deben aplicar a los servicios que ofrece la empresa

### 12.2.- Estandares

#### ISO

* ISO 27002 - Como gestionar la seguridad de un sistema
* ISO 27003 - Como diseñar un SGSI
* ISO 27004 - Como medir la eficacia de un SGSI
* ISO 27005 - Como gestionar los riesgos de un SGSI

#### AENOR

### 12.3.- SGSI

* Planificar
  * Analisis de riesgos
    * Identificar amenazas
    * Valorar perdidas
    * Estimar costes
  * Plan de contingencia
    * Tecnicas
      * Extintores
      * Detectores de humo
      * Salidas de emergencias
      * Equipos respaldo
    * Organizativas
      * Incendios
      * Alquiler de equipos
      * Backups
      * Procedimientos de actuacion
    * Humanas
      * Formacion
      * Responsables
      * Roles
    * Respaldo
      * Que hacer antes de que ocurra
      * Prevencir la amenaza
        * Simulacros
        * Copias de seguridad
    * Emergencia
      * Que hacer mientras ocurre
      * Paliar los efectos de la amenaza
        * Activar precontratos de alquiler
        * Restaurar backups
    * Recuperacion
      * Que hacer despues de que ocurra
      * Restaurar al estado antes de la amenaza
        * Trasladar datos de emergencia
        * Desactivar precontratos de alquiler
        * Reclamar seguros
* Hacer
  * Implementar las contramedidas oportunas
    * Atenuar riegos
    * Minimizar perdidas
    * Asegurar rapidez
* Comprobar
  * Revisar periodicamente
    * Puesta al dia
    * Comprovar funcionamiendo de SGSI
* Actuar
  * Resultado de la comprobacion
    * Revisar aspectos menores
    * Mejorar la eficiencia

### 12.4.- Amenazas

#### 12.4.1.- Humanas

* Establecer areas seguras
* Electromagnetismo
* Captar señales de componentes
* Instalaciones valladas y con control de acceso
* Control de acceso a las instalaciones
* Sistemas biometricos
* Visitar supervisadas
* Accesos auditados

#### 12.4.2.- Naturales

* Terremotos, Fuego, Tormentas electricas, inundaciones, etc

#### 12.4.3.- Entorno

* Temperaturas
* Polvo
* Insectos
* Sistemas de refrigeracion
* Limpieza
* Camaraz acorazadas
* Filtros en los conductos

#### 12.4.4.- Informacion en soporte fisico

* No se deben meter dispositivos que extraigan informacion

## 13.- Copias de seguridad

### 13.1.- Introduccion

* Se pierde mucho dinero en perdida de datos
* Se tarda mucho en detectar perdidas de datos
* Causas:
  * Errores de usuarios o administradores 29%
  * Errores de software
  * Errores de hardware 31%
  * Ataques o robo 29%
  * Desastres naturales

### 13.2.- Definiciones

* Backup: Duplicado de la informacion
* Recuperar informacion
* Tener un historico
* Auditorias
* Informatica forense

### 13.3.- Normativa

* ISO 27002
  * 12.3: Information Backup
  * Que copiar
  * DOnde copiar
  * Cada cuanto
  * Como recuperar
  * Igual que el UNE 71501

### 13.4.- Planificacion de las copias

* Minimo 3 copias
  * 2 en local y 1 offline
  * 1 en remoto
* Sincronizar archivos no vale
* Copias incrementales
* Encriptar
* Crear plan de prevencion
* Crear plan de recuperacion
* Elegir que copiar
  * Velocidad de copia
  * Prioridades
  * Datos mas valiosos
  * Tomar en cuenta costes

### 13.5.- Tipos de copias

#### 13.5.1.- Dia cero

* Copiar todo antes de empezar a usar el sistema
* Punto de partida

#### 13.5.2.- Completa

* Se realiza una copia de todos los datos
* Informacion duplicada
* Adecuada cuando hay muchos cambios desde la anterior
* Lenta y ocupa mucho

#### 13.5.3.- Incremental

* Se copian los datos cambiados respecto la ultima vez
* Rapida y ocupa poco
* Optima

#### 13.5.4.- Diferencial

* Se copian los datos cambiados respecto la ultima copia completa
* Rapida y ocupa poco
* Algo mas lenta que la incremental

### 13.6.- Restauracion de copias

* Dia cero: restaurar la copia
* Completa: restaurar la copia
* Incremental: restaurar la copia completa y luego la incremental
* Diferencial: restaurar la copia completa y luego la diferencial

### 13.7.- Frecuencia de copias

* Depende:
  * Valor de la informacion
  * Coste de no tener informacion
  * Cantidad de informacion
  * Cantidad de cambios
  * Coste de realizar la copia

### 13.8.- Proteccion de copias

* Las copias tambien sufren ataques
* Plan de proteccion:
  * Acceso
  * Disponibilidad
  * Proteccion
  * Tiempo de vida

### 13.9.- Comprobacion de copias

* Comprobar que las copias se hacen correctamente
* Hacer pruebas de restauracion

## 14.- Seguridad en redes

### 14.1.- Conexion a internet

* Confidencial e integridad
* Sistemas de autenticacion
* Control de accesos
* Supervisar el trafico
* Garantizar la disponibilidad
* Controlar los accesos
* Evitar los intentos de intrusion

### 14.2.- Defensa Perimetral

* Crear una barrera entre la red interna y la externa
* Filtrar el trafico
* Controlar las conexiones
* Normas mas laxas en la red interna

### 14.3.- Proxy

* Servidor intermediario
* El proxy se comunica con el exterior
* Mayor seguridad durante navegacion
* Aisla al usuario del mundo exterior
* NAT para convertir IPs
* Filtrar las comunicaciones
* Crear caches para acelerar la navegacion
* Auditar el ancho de banda
* Antivirus perimetral

### 14.4.- Proxy inverso

* Acceso controlado desde el exterior al servidor.
* alanceo de carga

### 14.5.- Firewall

* Elemento de red que filtra paquetes
* Establece conexiones directas
* Bloque trafico no autorizado
* Oculta los equipos internos
* Oculta informacion de la red
* Registra todo el trafico
* Redirecciona el trafico
* Limita el ancho de banda
* Da estadisticas sobre el ancho de banda
* Monitorea ataques 

### 14.6.- DMZ

* Zona donde estan los servicios
* Se crea entre uno o dos cortafuegos que limitan el acceso
* No se puede acceder a internet directamente

### 14.7.- ACL

* Reglas de filtrado

### 14.8.- Firewall

* Tipos:
  * A nivel de paquetes - Paquetes
  * Dinamicos - Paquetes y Flags
  * Pasarela - Reglas
* Lista blanca: Se deniega todo menos lo aceptado
* Lista negra: Se acepta todo menos lo denegado
* Bloquear paquetes por Broadcast
* Bloquear paquetes por Spoofing
* Bloquear paquetes con direcciones privadas
* Bloquear fuente HOME
* Bloquear paquetes ICMP
* BLoquear ICMP Redirect
* Bloquear paquetes con TTL 0
* Bloquear puertos
  * Telnet
  * SSH
  * FTP
  * NetBIOS
  * RPC
  * NFS
  * HTTP, SSL, SMTP, POP, IMAP, DNS, LDAP
* Ataques de ingenieria social
* Ataques por USL
* Ataques nivel protocolo
* Virus en portatiles del exterior

### 14.9.- Logs

* IP cliente
* ID cliente
* Nombre usuario
* Fechas y horas conexion
* Peticiones
* Estados
* Bytes enviados

### 14.10.- IPS

* Detectar y reaccionar de forma automatica
* Comprolar comportamiento red
* Comprobar comportamiento BBDD
* Eventos basados en BBDD
* Alarmas e informes
* Respuestas pasivas
  * Registrar intrusiones
* Respuestas activas
  * Bloquear intrusiones

### 14.11.- HIDS

* Detectar y avisar
* Comprobar comportamiento red
* Analizar logs kernel
* Analizar logs aplicaciones
* Auditoria periodicas
* Revisiones detalladas

### 14.12.- NIDS

* Monitorizar trafico
* Enrutamiento anormales
* IP spoofing
* DNS spoffing
* SYN flooding
* Fala correspondencia Mac-IP

### 14.13.- Honeypost

* Señuelos
* Detectar ataques
* Atraer atacantes
* Avisar de ataques
* Recoger informacion
* Avisar de vulnerabilidades

### 14.14.- VPN

* Red privada virtual
* Conectar en red no segura
* Autenticacion
* Integridad
* Confidencialidad
* No repudio

### 14.15.- Ataques

* Sniffing
* MITM
* Hijacking
* Spoofing
* DoS DDos

## 16.- Malware

### 16.1.- Definiciones

* Programa que provoca daño
* Virus, gusanos, troyanos, spyware, adware, etc
* No siempre tienen unos diferenciadores claros

### 16.2.- Gusanos

* Se reproduce a si mismo

### 16.3.- Troyanos

* Se mantiene oculto en un sistema para lleva a cabo una funcion

### 16.4.- Bomba logica

* Se activa cuando se cumple una condicion

### 16.5.- Backdoors

* Puerta trasera, permite acceso y control remoto

### 16.6.- Spyware

Recolecta y envia informacion privada

### 16.7.- Keylogger

Captura las teclas pulsadas

### 16.8.- Adware

Muestra anuncios

### 16.9.- Coinminer

Minar criptomonedas

### 16.10.- Instalacion

* Añadidura - Se añade en el EOF
* Insercion - Se inserta en un programa
* Reorientacion - Se cambia el flujo de ejecucion
* Sustitucion - Se sustituye un programa por otro

### 16.11.- Ocultacion

* Dispersion
* Compresion
* Camuflaje
* Sobrepasamiento
* Autocifrado
* Polimorfismo
* Blindaje

### 
