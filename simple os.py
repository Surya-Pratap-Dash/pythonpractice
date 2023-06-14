import tkinter as tk

def handle_button_click():
    label.config(text="Button clicked!")

root = tk.Tk()

# Create a label
label = tk.Label(root, text="Hello, World!")
label.pack()

# Create a button
button = tk.Button(root, text="Click me!", command=handle_button_click)
button.pack()

# Start the main event loop
root.mainloop()
