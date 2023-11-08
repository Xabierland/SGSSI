# Laboratorio 7 - Firewall Google Cloud

## Instalar Docker en el servidor remoto

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

```bash
sudo groupadd docker
```

```bash
sudo usermod -aG docker $USER
```

```bash
newgrp docker
```

## Desplegar proyecto web

```bash
git clone -b entrega_1 https://github.com/Xabierland/SGSSI-Proyecto.git

cd SGSSI-Proyecto

docker-compose up -d --build
```

## Crear reglas de firewall

### ¿En qué puertos escucha nuestro proyecto? (Pista: netstat)

```bash
netstat -ntlp | grep "LISTEN"
```

### ¿Cómo se pueden abrir esos puertos en Google Cloud? (Pistas: Red de VPC, etiqueta http-server, 0.0.0.0/0)

> Se podria crear una regla de firewall en [GCC](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/)

### ¿Cómo cerrarías los puertos 80 y 443 al tráfico entrante?

> Modificaria la instancia de GCC y eliminaria la regla de firewall

### ¿Cómo impedirías el tráfico saliente a la página https://en.wikipedi.org desde tu servidor Google Cloud? (Pistas: wget, ping)

> Se podria crear una regla de firewall en [GCC](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/) y añadirla a la instancia

### ¿Cómo impedirías el tráfico entrante en el puerto 8890 desde tu IP actual? (Pista: What is my IP?)

> Se podria crear una regla de firewall en [GCC](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/) y añadirla a la instancia