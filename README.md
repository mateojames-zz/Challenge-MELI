# Docker Redis - Flask Restful API

Para levantar los containes, por CMD (lado servidor):

```sh
docker-compose build
docker-compose up
```

Para corroborar su funcionamiento, ademas abrimos una ventana de CMD (lado cliente) donde corremos los endpoints.
Si se esta usando Docker nativamente, accedemos a http://0.0.0.0:5000 o http://localhost:5000 en nuestro explorador.
Si en cambio se esta usando una VM, corremos en una ventana de CMD el siguiente comando:
```sh
docker-machine ip
```
Abriendo un explorador, colocamos la ip obtenida de manera http://X.X.X.X:5000, remplzando las X con la ip (repetimos esto para los endpoints).
En esta pagina podremos visualizar los cambios concretados a la cola actualizandola despues de cada comando realizado.

# Endpoints

## Pop
```sh
curl -H "Content-Type: application/json" -X POST http://X.X.X.X:5000/api/queue/pop
```

## Push
```sh
curl -H "Content-Type: application/json" -X POST -d "{\"msg\":\"CAMELLO\"}" http://X.X.X.X:5000/api/queue/push
```
Reemplazando CAMELLO con la palabra deseada a agregar.

## Count

```sh
curl -H "Content-type: application/json" -X GET http://X.X.X.X:5000/api/queue/count
```

## Restore

Si quisieramos volver a tener en la lista 3 palabras ejemplo, solo es necesario abrir la Website de Restore http://X.X.X.X:5000/restore una vez y volver a la Website Principal http://X.X.X.X:5000/.
