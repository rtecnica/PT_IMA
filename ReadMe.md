# Prueba Técnica Alliot

## Setup
Para correr la aplicación se tienen dos opciones, Docker y manual
### Docker
1) [Instalar Docker](https://docs.docker.com/get-docker/)
2) Correr el siguiente comando:
    
    ```$ docker run rtecnica/pt_ima -p 8080:8080```

    Con esto el servidor comenzará a ejecutarse, desplegando el servidor web en el puerto `tcp/8080` de la máquina virtual.
3) Para acceder al servidor, se debe utilizar algun comando de listado de interfases de red como `ifconfig`.

    Un resultado de ejemplo:

            docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
                inet6 fe80::42:5ff:feba:4337  prefixlen 64  scopeid 0x20<link>
                ether 02:42:05:ba:43:37  txqueuelen 0  (Ethernet)
                RX packets 7406  bytes 783684 (783.6 KB)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 6495  bytes 17790098 (17.7 MB)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    En este caso el servidor web estaría contactable en `http://172.17.0.1:8080`

### Manual
1) Instalar [Python 3.9](https://www.python.org/downloads/)
2) Clonar el [repositorio](https://github.com/rtecnica/PT_IMA) y cambiar al directorio raíz del proyecto
3) Instalar paquetes contenidos en `requirements.txt`

    Puede realizarse con el comando siguiente: 
        
    `$pip install -r requirements.txt`

4) Ejecutar el proyecto con el comando siguiente:
   
   `$ python main.py`
   
## Supuestos
### Payloads
Los payloads se asumen completos, salvo por la estampa de tiempo que se imprime al ingerirlo a la base de datos
Se diferencian los payloads bajo el criterio que son iguales si todos sus campos son iguales
### MongoDB
La estructura de la base de datos fue asumida como colección única.
Hubiera sido posible separar en una colección por gateway (gw) o por origen (IMEI), sin embargo tuve problemas para reflejar esa estructura en la API Rest por lo que no fue implementada
### API Rest
Dado los requerimientos inmediatos de funcionalidad, sólo fueron implementadas completamente las funciones GET y POST para los recursos estipulados.
El endpoint que lista los recursos disponibles en la base de datos es `/payloads` y cada recurso está disponible en `/payloads/<payload_id>`

## Comentarios
Idealmente la base de datos estaría organizada por identificadores de dispositivos u origen, dependiendo de la arquitectura del sistema.
Además, me sucedió que las implementaciones de regex usadas por web.py me son poco familiares y aprenderlos me tomaría más tiempo del dispuesto para este proyecto.

