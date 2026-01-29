from pynput import keyboard
import time

actividad = []

ultimo_movimiento = time.time()

def on_press(key):
    global ultimo_movimiento
    ultimo_movimiento = time.time()
    actividad.append(ultimo_movimiento)
    print("Tecla presionada", key)

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Medidor de productividad iniciado")

try:
    while True:
        time.sleep(10)
        inactivo = time.time() - ultimo_movimiento
        if inactivo > 60:
            print("Sin actividad")

except KeyboardInterrupt:
    print("\nResumen del dia")
    if actividad:
        total_tiempo = (actividad[-1] - actividad[0]) / 60
        print(f"Duracion del registro: {total_tiempo:.1f}minutos")
        print(f"Teclas presionadas: {len(actividad)}")
    else:
        print("Sin actividad")
