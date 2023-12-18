# Laboratorio 8 - IPTables

## IPTables CheatSheet

[IPTables CheatSheet](https://www.acens.com/comunicacion/wp-content/images/2014/07/wp-acens-iptables.pdf)

## Copia de seguridad de las reglas de iptables

```bash
sudo iptables-save > iptables.backup
```

## Definid las reglas necesarias para conseguir lo siguiente

### Que vuestro servidor GCP solo acepte conexiones SSH desde el servidor 35.190.223.37 y desde vuestra máquina local

> [!CAUTION]
> Si te equivocas en estos comandos puedes perder el acceso a tu servidor

```bash
sudo iptables -A INPUT -p tcp --dport 22 -s $IP -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -s 35.190.223.37 -j ACCEPT
```

### Instalad un servicio FTP en vuestro servidor Google Cloud y que solo acepte conexiones FTP desde máquinas de la red de ehu.eus

> [!WARNING]
> Recuerda abrir el puerto 20 y 21 para que funcione FTP correctamente.

```bash
# Instalar y configurar vsftpd
sudo apt update
sudo apt install vsftpd
sudo service vsftpd stop
echo "listen=YES
local_enable=NO
anonymous_enable=YES
write_enable=NO
anon_root=/var/ftp" | sudo tee /etc/vsftpd.conf > /dev/null
sudo mkdir /var/ftp
sudo touch /var/ftp/prueba.txt
sudo service vsftpd start
```

```bash
# Comprobar acceso
ftp $IP
# Usuario: anonymous
```

```bash
# Añadir reglas
sudo iptables  -A INPUT -p tcp --dport 21 -s $IP -j ACCEPT
```

> [!Note]
> Al no estar en la universidad en vez de ehu.eus he usado mi IP.

### Que vuestro servidor Google Cloud no acepte conexiones HTTP (Solo HTTPS)

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j DROP
```

### En vuestra maquina local, que no se pueda hacer conexiones salientes a twitter, facebook ni youtube

```bash
sudo iptables -A OUTPUT -p tcp -d twitter.com -j DROP
sudo iptables -A OUTPUT -p tcp -d facebook.com -j DROP
sudo iptables -A OUTPUT -p tcp -d youtube.com -j DROP
```

## Restaurar las reglas de iptables

```bash
sudo iptables-restore < iptables.backup
```
