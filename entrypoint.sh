#!/bin/bash

MyWait=10s # tiempo de espera en segundos para arrancar cada servicio
echo " " > /ayuda.txt
echo "El botón derecho del ratón abre un menú contextual que permite cerrar kill cada panel" >> /ayuda.txt
echo "El ratón  debe estar activo para cambiar entre estas ventanas, y para cambiar entre los paneles. " >> /ayuda.txt
echo "La siguiente orden activa el ratón." >> /ayuda.txt
echo "tmux set-option -g mouse on" >> /ayuda.txt
echo "El script dibuja.py y la clase python Cuadrilatero están en el directorio /turtle" >> /ayuda.txt
echo "El usuario linux es root y el password toor" >> /ayuda.txt

touch /recibe.txt

tmux start-server 

tmux new-session -d -s MyTmux1 -n wEstado -d "/usr/bin/env sh -c \"python -m turtledemo\"; /usr/bin/env sh -i"
tmux split-window -h -t MyTmux1:wEstado  nano /recibe.properties
tmux split-window -h -t MyTmux1:wEstado  htop
tmux split-window -v -t MyTmux1:wEstado  mc
tmux select-layout -t MyTmux1:wEstado tiled


tmux new-window  -t MyTmux1 -n wAyuda -d  "/usr/bin/env sh -c \"cat /ayuda.txt\"; /usr/bin/env sh -i"
tmux split-window -h -t MyTmux1:wAyuda  "/usr/bin/env sh -c \"python -m dibuja.py\"; /usr/bin/env sh -i"
 
tmux set-option -g mouse on
tmux select-layout -t MyTmux1:wAyuda tiled

tmux attach-session -t MyTmux1:wAyuda
tmux attach-session -t MyTmux1:wEstado
