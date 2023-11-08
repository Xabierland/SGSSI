# Laboratorio 6 - Backups remotos

## Copias de seguridad remotas

### Recrea los ejercicios del laboratorio 5 sobre rsync, pero haz las copias de seguridad en el servidor remoto Google Cloud mediante SSH

> Voy a hacer un ejemplo y tirando, que pereza repetir todos.

```bash
rsync -avp $HOME/Seguridad/ xabier@34.105.232.127:~/Backups
```

### ¿En qué cambia el comando rsync sobre SSH?

> La diferencia esta en que hay que especificar el usuario y la IP del servidor remoto.

### ¿Como es la version del comando cp sobre SSH?

> No existe el comando cp sobre SSH, pero se puede usar el comando scp que es equivalente.

```bash
scp -r xabier@34.105.232.127:~/Backups $HOME/Seguridad/
```
