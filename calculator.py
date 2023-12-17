import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.5)

root = ctk.CTk()
root.title("Calculator")
root.geometry("625x425")
root.resizable(False, False)
root.iconbitmap('calculator.ico')
label = ctk.CTkLabel(root, text="КАЛЬКУЛЯТОР").grid(row=0, column=0, padx=10, pady=10)

button = ctk.CTkButton(root, fg_color='red', height = 15, width = 75, command=lambda: label.config(text="Clicked!"), text="ACC").grid(row=1, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 15, width = 75, command=lambda: label.config(text="Clicked!"), text="1").grid(row=2, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 15, width = 75, command=lambda: label.config(text="Clicked!"), text="2").grid(row=3, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 15, width = 75, command=lambda: label.config(text="Clicked!"), text="3").grid(row=4, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="4").grid(row=2, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="5").grid(row=3, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="6").grid(row=4, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="7").grid(row=2, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="8").grid(row=3, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="9").grid(row=4, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="0").grid(row=5, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="%").grid(row=5, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="/").grid(row=5, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="+").grid(row=2, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="-").grid(row=3, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="*").grid(row=4, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, fg_color='green', height = 10, width = 75, command=lambda: label.config(text="Clicked!"), text="=").grid(row=5, column=3, padx=10, pady=10)



root.mainloop()
