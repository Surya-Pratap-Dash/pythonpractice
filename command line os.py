import os

while True:
    command = input("$ ")
    
    if command == "exit":
        break
    
    # Split the command into command and arguments
    parts = command.split()
    cmd = parts[0]
    args = parts[1:]
    
    # Execute the command
    try:
        result = os.system(command)
        if result != 0:
            print(f"Command '{cmd}' returned non-zero exit status.")
    except OSError as e:
        print(f"Error executing command: {e}")
