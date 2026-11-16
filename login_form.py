import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Login Form")
root.geometry("400x350")
root.configure(bg="black")
title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Times New Roman", 25, "bold"),
    bg="black",
    fg="yellow"
)
title_label.pack(pady=5)
username_label = tk.Label(
    root,
    text="Username",
    font=("Times New Roman", 12),
    bg="black",
    fg="yellow"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Times New Roman", 11),
    width=25
)
username_entry.pack(pady=5)

password_label = tk.Label(
    root,
    text="Password",
    font=("Times New Roman", 12),
    bg="black",
    fg="yellow"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Times New Roman", 12),
    width=25,
    show="*"
)
password_entry.pack(pady=5)


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin_jai" and password == "081806":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )

login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Times New Roman", 12, "bold"),
    bg="black",
    fg="yellow",
    width=20,
    command=login
)
login_button.pack(pady=20)

root.mainloop()