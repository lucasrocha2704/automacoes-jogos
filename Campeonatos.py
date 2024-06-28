import pyautogui
import keyboard
import time


key_to_press = ' '

stop_key = 'f8'

print(f"Pressionando '{stop_key}' para iniciar")

executando = False

try:

    while True:
        if keyboard.is_pressed(stop_key):
            executando = not executando
            x, y = pyautogui.position()
            print(f"Posição atual do mouse: x={x}, y={y}")

            time.sleep(0.5)
            
            while executando:
                keyboard.press(key_to_press)
                time.sleep(0.01)
                keyboard.release(key_to_press)
                # Clica na posição atual do mouse
                pyautogui.click(x, y)

                # time.sleep(0.01)

                if keyboard.is_pressed(stop_key):
                    executando = not executando
                    print(f"executando: {executando}")
                    time.sleep(0.5)  # Evita a leitura múltipla do mesmo pressionamento

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa interrompido manualmente.")
