import readline
import atexit
import os

# History file path (you can choose your own location)
history_file = os.path.expanduser("~/.py_history")

# Load history if exists
if os.path.exists(history_file):
    readline.read_history_file(history_file)

# Save history on exit
atexit.register(readline.write_history_file, history_file)

# Optional: limit history size
readline.set_history_length(1000)

# Loop with input
while True:
    try:
        cmd = input(">>> ")
        if cmd.strip().lower() in ('exit', 'quit'):
            break
        print("You typed:", cmd)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt (Ctrl+C)")
        continue
    except EOFError:
        print("\nExit (Ctrl+D)")
        break