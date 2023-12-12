# Laboratorio 4 - Certificados

## 1.- Instalacion de Apache

```bash
sudo apt install apache2
```

## 2.- Creacion de un sitio seguro

## 2.1.- Certificado con certbot (Let’s Encrypt)

```bash
# 0. Configuramos servidor Apache
sudo rm /var/www/html/index.html                       
sudo nano /var/www/html/index.html                      
    <h1>Conexion SSL</h1>

# 1. Instalamos certbot
sudo apt-get install certbot python3-certbot-apache     
sudo certbot --apache                                  
```

## 2.2.- Certificado sin certbot

```bash
# 0. Configuramos servidor Apache
sudo rm /var/www/html/index.html                     
sudo nano /var/www/html/index.html                      
    <h1>Conexion SSL</h1>

# 1. Creamos el certificado SSL
sudo apt-get install openssl
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt

# 2. Configurar Apache para usar SSl
sudo cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf.bak
sudo nano /etc/apache2/sites-available/default-ssl.conf
    + ServerAdmin xgabina001@ehu.eus
    + ServerName 34.105.232.127
    + SSLCertificateFile      /etc/ssl/certs/apache-selfsigned.crt
    + SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key
sudo nano /etc/apache2/sites-available/000-default.conf
    + Redirect permanent "/" "https://34.105.232.127/"

# 3. Aplicar cambios en Apache
sudo a2enmod ssl
sudo a2enmod headers
sudo a2ensite default-ssl
sudo apache2ctl configtest
sudo systemctl restart apache2
```