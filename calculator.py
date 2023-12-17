import customtkinter as ctk
import tkinter

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.5)
root = ctk.CTk()
root.title("Calculator")
root.geometry("625x425")
root.resizable(False, False)
root.iconbitmap('calculator.ico')

sum_1 = ""
count = 0
def numbers(numb):
    global sum_1
    sum_1 += str(numb)
    label = ctk.CTkLabel(root, text=f"{sum_1}").grid(row=1, column=1, padx=10, pady=10)



def ecuals():
    global sum_1
    global count
    count = eval(sum_1)
    label = ctk.CTkLabel(root, text=f"RES: {count}").grid(row=1, column=2, padx=10, pady=10)


def acc():
    global sum_1
    global count
    sum_1 = ""
    count = 0




button = ctk.CTkButton(root, fg_color='red', height = 15, width = 75, command=acc, text="ACC").grid(row=1, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(1)), text="1").grid(row=2, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(2)), text="2").grid(row=3, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(3)), text="3").grid(row=4, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(4)), text="4").grid(row=2, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(5)), text="5").grid(row=3, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(6)), text="6").grid(row=4, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(7)), text="7").grid(row=2, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(8)), text="8").grid(row=3, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(9)), text="9").grid(row=4, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers(0)), text="0").grid(row=5, column=0, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers('%')), text="%").grid(row=5, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers('/')), text="/").grid(row=5, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers('+')), text="+").grid(row=2, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers('-')), text="-").grid(row=3, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (numbers('*')), text="*").grid(row=4, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, fg_color='green', height = 10, width = 75, command=ecuals, text="=").grid(row=5, column=3, padx=10, pady=10)
# label = ctk.CTkLabel(root, text="КАЛЬК").grid(row=0, column=0, padx=10, pady=10)
#textbox = ctk.CTkTextbox(root, height = 10, width = 75).grid(row=0, column=0, padx=10, pady=10)



root.mainloop()
