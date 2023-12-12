# Laboratorio 5 - Backups

## Copias de seguridad en GNU/Linux

### Cread en el escritorio una carpeta llamada Seguridad y en su interior 5 ficheros de texto llamados a, b, c, d y e. Cada fichero puede tener el contenido que queráis (ej. $ echo "A" > A)

```bash
mkdir $HOME/Seguridad
echo "A" > $HOME/Seguridad/A
echo "B" > $HOME/Seguridad/B
echo "C" > $HOME/Seguridad/C
echo "D" > $HOME/Seguridad/D
echo "E" > $HOME/Seguridad/E
```

### Cread una carpeta llamada Backups en el directorio /var/tmp

```bash
sudo mkdir /var/tmp/Backups
```

### Ejecutad el siguiente comando 

```bash
sudo rsync -av $HOME/Seguridad /var/tmp/Backups
```

#### ¿Qué hace exactamente ese comando? ¿Qué implican las opciones “a” y “v” que hemos usado?

> El comando rsync copia los archivos de un directorio a otro. La opción “a” indica que se copien los archivos de forma recursiva, conservando los permisos, propietarios, grupos, etc. La opción “v” indica que se muestre información sobre el proceso de copia (verbose).

### Ejecutad otra vez el comando, pero esta vez con un slash “/” al final del primer argumento

```bash
sudo rsync -av $HOME/Seguridad/ /var/tmp/Backups
```

#### ¿Qué diferencia hay con el comando sin slash?

> La diferencia es que con el slash se copia el contenido del directorio, mientras que sin el slash se copia el directorio en sí.

### Modificad el contenido de los ficheros a y b de la carpeta Seguridad y cread un nuevo fichero llamado f

```bash
echo "a" >> $HOME/Seguridad/A
echo "b" >> $HOME/Seguridad/B
echo "F" > $HOME/Seguridad/F
```

### Cread dentro de la carpeta Backups una carpeta cuyo nombre sea la fecha actual en formato dd-mm-aaaa

```bash
sudo mkdir /var/tmp/Backups/$(date +%d-%m-%Y)
```

### Cread dentro de la carpeta Backups una carpeta cuyo nombre sea SeguridadLinkDest

```bash
sudo mkdir /var/tmp/Backups/SeguridadLinkDest
```

### Situaros mediante la terminal en la carpeta Seguridad

```bash
cd $HOME/Seguridad
```

### Ejecutad el siguiente comando, sustituyendo “fechaactual” por la fecha correspondiente en el formato indicado

```bash
rsync -av --link-dest=/var/tmp/Backups/SeguridadLinkDest . /var/tmp/Backups/$(date +%d-%m-%Y)
```

#### ¿Qué hace exactamente ese comando? ¿Qué aparece en el directorio con la fecha actual? ¿Qué significan los parametros “/var/tmp/Backups/SeguridadLinkDest”,”.”, y “/var/tmp/Backups/fechaactual” que se usan en el comando?

> El comando rsync copia los archivos de un directorio a otro. La opción “a” indica que se copien los archivos de forma recursiva, conservando los permisos, propietarios, grupos, etc. La opción “v” indica que se muestre información sobre el proceso de copia (verbose). La opción “--link-dest” indica que se creen enlaces simbólicos a los archivos que no han cambiado desde la última copia. El punto indica que se copie el directorio actual. El directorio “/var/tmp/Backups/SeguridadLinkDest” indica que se creen enlaces simbólicos a los archivos que no han cambiado desde la última copia. El directorio “/var/tmp/Backups/fechaactual” indica que se copien los archivos en ese directorio.

### En el directorio Seguridad borrad el fichero c, añadid cambios a los ficheros a y e, y cread un fichero g ($ echo "G" > G)

```bash	
rm $HOME/Seguridad/C
echo "a" >> $HOME/Seguridad/A
echo "e" >> $HOME/Seguridad/E
echo "G" > $HOME/Seguridad/G
```

### Vamos a simular el paso del tiempo. Cread dentro de la carpeta Backups una carpeta cuyo nombre sea la fecha de mañana en formato dd-mm-aaaa

```bash	
sudo mkdir /var/tmp/Backups/$(date -d tomorrow +%d-%m-%Y)
```

### Situaros mediante la terminal en el directorio Seguridad y ejecutad el siguiente comando, sustituyendo “fechamañana” por la fecha correspondiente en el formato indicado

```bash
cd $HOME/Seguridad
rsync -av --link-dest=/var/tmp/Backups/$(date +%d-%m-%Y) . /var/tmp/Backups/$(date -d tomorrow +%d-%m-%Y)
```

#### ¿Qué se encuentra en el directorio con la fecha de mañana? ¿Qué ha ocurrido y por qué?

> Se encuentran los archivos que no han cambiado desde la última copia. Esto ocurre porque se han creado enlaces simbólicos a los archivos que no han cambiado desde la última copia.

### Modificad el contenido del fichero g

```bash
echo "g" >> $HOME/Seguridad/G
```

#### ¿Qué comando sería necesario para realizar en la carpeta Backups/fechapasadomañana una copia de seguridad sólo con el fichero modificado desde la anterior copia de seguridad (La que tiene fecha de mañana)?

```bash
sudo rsync -av --link-dest=/var/tmp/Backups/$(date -d tomorrow +%d-%m-%Y) . /var/tmp/Backups/$(date -d "2 days" +%d-%m-%Y)
```

### Borrad todo el contenido del directorio Seguridad

```bash
rm -r $HOME/Seguridad/*
```

#### ¿Qué comandos son necesarios para restaurar el contenido completo a partir de la penúltima de las copias de seguridad (La que tiene fecha de mañana)?

```bash
sudo rsync -av /var/tmp/Backups/$(date -d tomorrow +%d-%m-%Y)/* $HOME/Seguridad
```

### Ejecutad el siguiente comando en varios directorios de la carpeta Backups

```bash
ls -ali /var/tmp/Backups/$(date tomorrow +%d-%m-%Y)
```

#### Hay dos números importantes a tener en cuenta: (1) Antes de los permisos, un número con muchos dígitos, por ejemplo 1150561; (2) Después de los permisos, un número pequeño, siempre 1 o mayor (1, 2, o 3 en este caso) ¿Qué significan? ¿Qué utilidad pueden tener a la hora de hacer copias de seguridad?

> El número de antes de los permisos es el número de inodo del archivo. El número de después de los permisos es el número de enlaces duros que tiene el archivo. Estos números pueden ser útiles para saber si un archivo ha sido modificado o no.

## Automatización de tareas

### Cread un script Cron que realice una copia de seguridad incremental de la carpeta Seguridad cada día a las 12 del mediodía. Cada copia se deberá realizar en una carpeta distinta, cuyo nombre será la fecha del día que se hizo la respectiva copia

```bash
crontab -e
0 12 * * * /bin/bash $HOME/backup.sh
```

#### Al trabajar con Cron, si el comando que tiene que ejecutar Cron es muy largo o la tarea está compuesta por varios comandos a la vez, es muy común crear un Shell Script que es el que es ejecutado por Cron

```bash
#!/bin/bash

sudo mkdir /var/tmp/Backups/$(date +%d-%m-%Y)
sudo rsync -av --link-dest=/var/tmp/Backups/$(date -d yesterday +%d-%m-%Y) $HOME/Seguridad /var/tmp/Backups/$(date +%d-%m-%Y)
```
