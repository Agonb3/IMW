# UT1-A1. Mis Series Favoritas.

Previamente habiendo instalado Nginx en nuestra máquina, comprobamos si se esta ejecutando.

![](./img/1.JPG)

Ahora eliminamos el enlace web por defecto (default), situandonos en la carpeta /etc/nginx/sites-enabled.

![](./img/2.JPG)

Dentro de nuestro directorio /home vamos a crear las carpetas /webapps/series y alojaremos nuestra página web dentro de la misma.

![](./img/5.JPG)

En el directorio /etc/nginx/sites-available vamos a crear un nuevo fichero llamado alua83p64100j.me con el siguiente contenido.

![](./img/3.JPG)

Ahora enlazaremos ese fichero con el directorio /etc/nginx/sites-enabled.

![](./img/4.JPG)

Vamos a comprobar que es visible desde nuestro navegador.

![](./img/6.JPG)

![](./img/7.JPG)

Aun no podemos visualizar la página mediante el dominio porque no hemos mapeado la ip en nuestras dns. Para ello vamos a editar el archivo de configuración /etc/hosts y añadiremos nuestra ip y el nombre de dominio al que apunta.

![](./img/302.JPG)

Comprobamos de nuevo esta vez mediante nuestro dominio.

![](./img/300.JPG)

![](./img/3001.JPG)
