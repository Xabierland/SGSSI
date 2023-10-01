# Laboratorio 4 - Certificados

## 1.- Instalacion de Apache

```bash
sudo apt install apache2
```

## 2.- Creacion de un sitio seguro

## 2.1.- Instalacion de certbot (Let’s Encrypt)

```bash
sudo rm /var/www/html/index.html                        # Borramos el archivo de apache por defecto
sudo nano /var/www/html/index.html                      # Creamos un archivo index.html
    <h1>Conexion SSL</h1>
sudo apt-get install certbot python3-certbot-apache     # Instalamos certbot
sudo certbot --apache                                   # Configuramos certbot
```

## 2.2.- Certificado sin certbot

```bash
sudo rm /var/www/html/index.html                        # Borramos el archivo de apache por defecto
sudo nano /var/www/html/index.html                      # Creamos un archivo index.html
    <h1>Conexion SSL</h1>
sudo apt-get install openssl
openssl genpkey -algorithm RSA -out servidor.key
openssl req -new -key servidor.key -out servidor.csr
openssl x509 -req -in servidor.csr -signkey servidor.key -out servidor.crt
```