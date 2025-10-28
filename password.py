import customtkinter as ctk
import random
import string
from tkinter import messagebox

# App setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("✨ Password Generator ✨")
app.geometry("450x450")

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4 or length > 32:
            messagebox.showerror("Invalid", "Password length should be between 4 and 32")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length")
        return

    chars = string.ascii_lowercase
    if upper_var.get():
        chars += string.ascii_uppercase
    if num_var.get():
        chars += string.digits
    if sym_var.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    output_entry.delete(0, "end")
    output_entry.insert(0, password)
    messagebox.showinfo("Success", "Password Generated Successfully! 🔐")

# Copy password
def copy_password():
    app.clipboard_clear()
    app.clipboard_append(output_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Title
title = ctk.CTkLabel(app, text="🔒 Secure Password Generator 🔒", font=("Arial Rounded MT Bold", 20))
title.pack(pady=20)

# Length input
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

length_label = ctk.CTkLabel(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = ctk.CTkEntry(frame, width=100)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Options
upper_var = ctk.BooleanVar()
num_var = ctk.BooleanVar()
sym_var = ctk.BooleanVar()

upper_check = ctk.CTkCheckBox(app, text="Include Uppercase", variable=upper_var)
upper_check.pack()
num_check = ctk.CTkCheckBox(app, text="Include Numbers", variable=num_var)
num_check.pack()
sym_check = ctk.CTkCheckBox(app, text="Include Symbols", variable=sym_var)
sym_check.pack()

# Output
output_entry = ctk.CTkEntry(app, width=300, font=("Consolas", 14))
output_entry.pack(pady=20)

# Buttons
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

generate_btn = ctk.CTkButton(btn_frame, text="Generate Password", command=generate_password)
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = ctk.CTkButton(btn_frame, text="Copy Password", command=copy_password)
copy_btn.grid(row=0, column=1, padx=10)

# Footer
footer = ctk.CTkLabel(app, text="✨ Created by Priyanka ✨", font=("Arial", 12))
footer.pack(pady=15)

app.mainloop()
