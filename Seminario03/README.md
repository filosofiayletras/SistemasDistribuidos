# Grupo 21
# Seminario 4
Programa en python que geolocaliza al usuario y muestra los tweets más recientes en un radio de 10 kilómetros.
Los marcadores en el mapa son personalizados (foto de perfil del usuario), por lo que es necesario disponer de la última versión de la extensión de Google Maps para Flask. Para ello, puede instalarla desde el repositorio `https://github.com/rochacbruno/Flask-GoogleMaps.git`

## Imágenes
![Captura de pantalla](http://i61.tinypic.com/10py73l.png)

## Uso
Ejecute `python twitmap.py` y acceda en su navegador a la dirección `localhost:5000`. Su navegador le pedirá acceso a su ubicación (esta solo se usa para mostrar los tweets de tu alrededor). Debe dar acceso a ella. Tras geolocalizarle, será redirigido al mapa.
Si quiere conocer los tweets alrededor de una ubicación distinta a la suya, puede hacerlo accediendo a la página `localhost:5000/<latitud>,<longitud>`

##Componentes
	Jose Manuel Vidal
	Manuel Francisco
