# Laboratorio 9 - TOR, ONION

## TOR

> [https://www.torproject.org/es/](https://www.torproject.org/es/)

## Navegador TOR

> [https://www.torproject.org/es/download/](https://www.torproject.org/es/download/)

### ¿Por qué crees que abundan los periodicos entre los sitios que ofrecen servicios ONION?

> Dado que en muchos sitios del mundo se bloquean acceso a diferentes periodicos y medios de comunicación, por lo que se hace necesario que estos medios tengan una forma de llegar a sus lectores sin ser bloqueados.

## Servicio ONION en Google Cloud

> Inicia o crea una instancia de Google Cloud con Ubuntu 22.04. Recuerda tener abierto el puerto 80 en el firewall de la instancia.

## Instalar TOR

```bash
echo "deb     [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/tor.list

echo "deb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/tor.list

wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | sudo tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null

sudo apt update

sudo apt install tor deb.torproject.org-keyring

curl -x socks5h://localhost:9050 -s https://check.torproject.org/api/ip
```

## Configurar servicio ONION

```bash
echo "HiddenServiceDir /var/lib/tor/my-website/" | sudo tee -a /etc/tor/torrc

echo "HiddenServicePort 80 127.0.0.1:80" | sudo tee -a /etc/tor/torrc

sudo service tor restart

sudo cat /var/lib/tor/my-website/hostname
```
