import ctypes
import pyautogui
import keyboard
import time
import threading

key_to_press = 'e'
stop_key = 'f8'
time_pressed = 3

print(f"Pressione '{stop_key}' para começar")

# Variável global para controle de execução
executando = False

# Defina os dois pontos entre os quais o mouse deve clicar
point1 = (1823, 620)
point2 = (1823, 350)

# Defina o delay entre os cliques
click_delay = 0.01

# Carrega a DLL user32
user32 = ctypes.windll.user32

def move_mouse(x, y):
    # Define a posição do mouse
    user32.mouse_event(0x0001, x, y, 0, 0)

def click_mouse():
    # Simula um clique de mouse
    user32.mouse_event(0x0002, 0, 0, 0, 0)  # Pressiona o botão esquerdo do mouse
    user32.mouse_event(0x0004, 0, 0, 0, 0)  # Solta o botão esquerdo do mouse

def move_and_click(start_point, end_point):
    steps = 100
    x_step = (end_point[0] - start_point[0]) / steps
    y_step = (end_point[1] - start_point[1]) / steps

    for step in range(steps):
        move_mouse(int(x_step), int(y_step))
        click_mouse()
        time.sleep(click_delay)

def click_loop():
    global executando
    while True:
        if executando:
            move_and_click(point1, point2)
            move_and_click(point2, point1)
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

def toggle_execution():
    global executando
    executando = not executando
    print(f"Executando: {executando}")
    time.sleep(0.5)  # Evita a leitura múltipla do mesmo pressionamento

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
            toggle_execution()

        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programa interrompido manualmente.")