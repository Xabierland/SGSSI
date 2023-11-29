# Laboratorio 9 - TOR, ONION

## TOR

## Navegador TOR

### ¿Por qué crees que abundan los periodicos entre los sitios que ofrecen servicios ONION?

> Porque en muchos sitios del mundo se bloquean acceso a diferentes periodicos y medios de comunicación, por lo que se hace necesario que estos medios tengan una forma de llegar a sus lectores sin ser bloqueados.

## Servicio ONION en Google Cloud

## Instalar TOR

```bash
sudo nano /etc/apt/sources.list.d/tor.list
```

```list
deb     [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org jammy main

deb-src [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org jammy main
```

```bash
sudo su

wget -qO- https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | gpg --dearmor | tee /usr/share/keyrings/tor-archive-keyring.gpg >/dev/null
```

```bash
sudo apt update
sudo apt install tor deb.torproject.org-keyring
curl -x socks5h://localhost:9050 -s https://check.torproject.org/api/ip
```

## Configurar servicio ONION

```bash
sudo nano /etc/tor/torrc
```

```torrc
HiddenServiceDir /var/lib/tor/my-website/
HiddenServicePort 80 unix:/var/run/tor/my-website.sock
```
