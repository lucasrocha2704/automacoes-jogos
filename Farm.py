import pyautogui
import keyboard
import time
import threading

key_to_press = 'e'
stop_key = 'f8'
time_pressed = 3

print(f"Pressione'{stop_key}' para começar")

# Variável global para controle de execução
executando = False

def click_loop():
    global executando
    while True:
        if executando:
            pyautogui.click()
            time.sleep(0.01)
        else:
            time.sleep(0.1)

def press_key_loop():
    global executando
    while True:
        if executando:
            start_time = time.time()
            while time.time() - start_time < time_pressed:
                keyboard.press(key_to_press)
                time.sleep(0.1)  # Pequeno delay para manter a tecla pressionada
            keyboard.release(key_to_press)
            time.sleep(20)
        else:
            time.sleep(0.1)

# Inicia a thread para a função de clicar
click_thread = threading.Thread(target=click_loop)
click_thread.daemon = True
click_thread.start()

# Inicia a thread para a função de pressionar a tecla
press_key_thread = threading.Thread(target=press_key_loop)
press_key_thread.daemon = True
press_key_thread.start()

try:
    while True:
        if keyboard.is_pressed(stop_key):
            executando = not executando
            print(f"Executando: {executando}")
            time.sleep(0.5)  # Evita a leitura múltipla do mesmo pressionamento

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa interrompido manualmente.")
