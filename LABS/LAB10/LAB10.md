# Laboratorio 10 - NMap

> [!IMPORTANT]
> Es necesario tener instalado nmap para poder realizar este laboratorio. Para instalarlo en Ubuntu se puede usar el comando `sudo apt install nmap`.

## Puertos abiertos en scanme.nmap.org y en tu servidor Google Cloud, servicios y version de servicios

```bash
# scanme.nmap.org
nmap scanme.nmap.org
```

```text
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-12 22:30 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.18s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
9929/tcp  open  nping-echo
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 19.42 seconds
```

```bash
# GCP
nmap $IP
```

```text
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-12 22:28 CET
Nmap scan report for 127.232.105.34.bc.googleusercontent.com (34.105.232.127)
Host is up (0.043s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE  SERVICE
21/tcp   open   ftp
22/tcp   open   ssh
80/tcp   open   http
443/tcp  closed https
3389/tcp closed ms-wbt-server

Nmap done: 1 IP address (1 host up) scanned in 4.75 seconds
```

## ¿Que maquionas estan activas en la red desde tu maquina a tu servidor remoto?

> [!NOTE]
> Para esto se puede usando la flag `--traceroute` que hace un traceroute a la maquina, y muestra los hops que hace el paquete para llegar a la maquina. Tambien existe un programa de mismo nombre que la flag que hace lo mismo.

```bash
sudo nmap --traceroute $IP
```

```text
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-12 22:31 CET
Nmap scan report for 127.232.105.34.bc.googleusercontent.com (34.105.232.127)
Host is up (0.045s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE  SERVICE
21/tcp   open   ftp
22/tcp   open   ssh
80/tcp   open   http
443/tcp  closed https
3389/tcp closed ms-wbt-server

TRACEROUTE (using port 3389/tcp)
HOP RTT      ADDRESS
1   0.31 ms  Xabier-Desktop (172.31.16.1)
2   1.06 ms  192.168.1.1
3   ... 4
5   17.32 ms 205.red-88-28-91.dynamicip.rima-tde.net (88.28.91.205)
6   ... 7
8   19.15 ms 213.140.36.172
9   ...
10  42.11 ms 127.232.105.34.bc.googleusercontent.com (34.105.232.127)

Nmap done: 1 IP address (1 host up) scanned in 11.41 seconds
```

## ¿Que puertos tiene abiertos una de las maquinas activas de la red?

```bash
nmap $IP
```


## ¿Que versiones de los servicios está usando una de las máquinas activas de la red?

> [!NOTE]
> Para esto se puede usar el flag `-sV` que hace un scan de versiones de los servicios. [NMap Service and Version Detection](https://nmap.org/man/es/man-version-detection.html)

```bash
sudo nmap -sV $IP
```

## ¿Que sistema operativo está usando una de las máquinas activas de la red?

> [!NOTE]
> Para esto se puede usar el flag `-O` o `-A` que hace un scan de OS. [NMap OS Detection](https://nmap.org/man/es/man-os-detection.html)

```bash
sudo nmap -O $IP
```

## ¿Que sistema operativo tiene scanme.nmap.org?

```bash
sudo nmap -O scanme.nmap.org
```

```text
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-12 22:19 CET
Nmap scan report for scanme.nmap.org (45.33.32.156)
Host is up (0.18s latency).
Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
Not shown: 996 closed tcp ports (reset)
PORT      STATE    SERVICE
22/tcp    open     ssh
80/tcp    filtered http
9929/tcp  open     nping-echo
31337/tcp open     Elite
Device type: general purpose|broadband router|storage-misc|WAP|media device
Running (JUST GUESSING): Linux 5.X|3.X|4.X|2.6.X (92%), HP embedded (90%), Ubiquiti embedded (89%), Ubiquiti AirOS 5.X (89%), Netgem embedded (88%)
OS CPE: cpe:/o:linux:linux_kernel:5.0 cpe:/o:linux:linux_kernel:3 cpe:/h:hp:p2000_g3 cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:2.6.32 cpe:/h:ubnt:airmax_nanostation cpe:/o:ubnt:airos:5.2.6 cpe:/h:netgem:n7700
Aggressive OS guesses: Linux 5.0 (92%), Linux 5.0 - 5.4 (92%), OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (90%), HP P2000 G3 NAS device (90%), Linux 4.15 - 5.8 (90%), Linux 5.3 - 5.4 (90%), Linux 2.6.32 (89%), Linux 2.6.32 - 3.1 (89%), Ubiquiti AirMax NanoStation WAP (Linux 2.6.32) (89%), Linux 3.7 (89%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 21 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.93 seconds
```

El sistema operativo es GNU/Linux y la version del kernel es 5.0

## Una vez determinado el sistema operativo, ¿que vulnerabilidades tiene?

Tras buscar en [https://cve.mitre.org/](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=Linux+5.0) Linux 5.0 se pueden ver 27 CVEs que afectan a esta version del kernel.

## ¿Como se puede usar nmap para detectar si una maquina tiene firewall?

> [!WARNING]
> No hay ninguna herramienta mágica (u opción de Nmap) que permita detectar y evitar cortafuegos y sistemas IDS. Se puede usar la opcion `-f` para fragmentar los paquetes, y `-D` para usar decoys pero no hay ninguna opcion que permita detectar y evitar cortafuegos y sistemas IDS.
