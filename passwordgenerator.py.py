import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        password_label.config(text="Please enter a valid integer for password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and place widgets in the window
length_label = tk.Label(window, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(window)
length_entry.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=20)

password_label = tk.Label(window, text="")
password_label.pack(pady=10)

# Run the main loop
window.mainloop()
