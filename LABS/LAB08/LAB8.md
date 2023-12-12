# Laboratorio 8 - IPTables

## Definid las reglas necesarias para conseguir lo siguiente:

### Que vuestro servidor GCP solo acepte conexiones SSH desde el servidor 35.190.223.37 y desde vuestra máquina local

```bash
-A INPUT -p tcp --dport 22 -s 88.14.6.187 -j ACCEPT
-A INPUT -p tcp --dport 22 -s 35.190.223.37 -j ACCEPT
```

### Instalad un servicio FTP en vuestro servidor Google Cloud y que solo acepte conexiones FTP desde máquinas de la red de ehu.eus

> No estoy en la uni asi que voy ha hacerlo con mi ip en vez de la de la uni

```bash
# Instalar vsftpd
```