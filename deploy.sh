#!/bin/bash
pid=$(lsof -i :7861 | awk 'NR==2 {print $2}')
if [ -z "$pid" ]; then
  echo "La variable pid está vacía. No se encontró ningún proceso escuchando en el puerto 7861."
else
  echo "El PID del proceso es: $pid"
fi

kill $pid

sleep 5

timestamp=$(date +"%d-%m-%Y %H:%M:%S")
echo "Proceso eliminado: $pid @ $timestamp"

cd
cd code/gradio-standalone-do/
source venv/bin/activate
python app.py &
PID=$(pgrep -f "python app.py")
timestamp2=$(date +"%d-%m-%Y %H:%M:%S")
echo "Proceso reiniciado: $PID @ $timestamp2"
