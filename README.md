# turtle-Tmux-Python-Alpine-Docker
facilidad para dibujar un cuadrilatero en modo gráfico, utilizando  Turtle Tmux Python  Alpinelinux y Docker

## Para empezar
```
cd ~/docker/turtle
git clone https://github.com/cparodif/turtle-tmux-python-alpine-docker.git
cd turtle-tmux-python-alpine-docker
sudo su
chmod +x -v entrypoint.sh
xhost +
docker build . -t turtle:001
docker run -it -p 9092:9092 -p 2181:2181 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/docker/turtle:/turtleDocker turtle:001
```

## Para terminar

cerrar las dos ventanas gráficas

- demoturtle
- ejemCuadrilatero
- Cerrar ventanas tmux con click ratón derecho y kill

xhost -

## Reiniciar

$ cd ~/docker/turtle
$ sudo su
$ xhost +
$ docker start id_c -i
```
