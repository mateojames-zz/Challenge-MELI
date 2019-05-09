# Docker Redis - Flask Restful API

Para levantar los containes, por cmd(lado servidor):

```sh
docker-compose build
docker-compose up
```

Para corroborar su funcionamiento, ademas abrimos una ventana de cmd (lado cliente) donde corremos los endpoints, y abrimos en un explorador la [Website Principal](http://192.168.99.100:5000/), donde despues de cada comando podemos dar refresh para ver los cambios concretados.

# Endpoints

## Pop
```sh
curl -H "Content-Type: application/json" -X POST http://192.168.99.100:5000/pop
```

## Push
```sh
curl -H "Content-Type: application/json" -X POST -d "{\"msg\":\"Camello\"}" http://192.168.99.100:5000/push
```

## Count

```sh
curl -H "Content-type: application/json" -X GET http://192.168.99.100:5000/count
```

## Restore

Si quisieramos volver a tener en la lista 3 palabras ejemplo, solo es necesario abrir la [Website de Restore](http://192.168.99.100:5000/restore) una vez y volver a la [Website Principal](http://192.168.99.100:5000/).
