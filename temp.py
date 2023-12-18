import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
ctk.set_widget_scaling(1.5)
root = ctk.CTk()
root.title("Calculator")
root.geometry("575x425")
root.resizable(False, False)
root.iconbitmap('calculator.ico')

sum_2 = count = 0
oper = tbt = ""
sum_1 = ""
def operators(op):
    global sum_1
    global sum_2
    global oper
    if op == "+":
        sum_2 = sum_1
        sum_1 = 0
        oper = "+"
    elif op == "-":
        sum_2 = sum_1
        sum_1 = 0
        oper = "-"
    elif op == "*":
        sum_2 = sum_1
        sum_1 = 0
        oper = "*"
    elif op == "/":
        sum_2 = sum_1
        sum_1 =0
        oper = "/"
    else:
        sum_2 = sum_1
        sum_1 = 0
        oper = "%"

def numbers(numb):
    global count
    global sum_1
    global tbt
    sum_1 += str(numb)

    textbox_1.insert("end", numb)

    print(sum_1)

    print(numb)


def ecuals():
    global oper
    global sum_1
    global count
    if oper == "+":
        count = sum_1 + sum_2
    elif oper == "-":
        count = sum_1 - sum_2
    elif oper == "*":
        count = sum_1 * sum_2
    elif oper == "/":
        count = sum_1 / sum_2
    else:
        count = (sum_1 / 100) * sum_2
    textbox_1.delete(0.0, "end")
    textbox_2.insert("end", count)

def acc():
    global sum_1
    global sum_2
    global count
    global oper
    global tbt
    sum_1 = sum_2 = count = 0
    oper = tbt = ""
    textbox_1.delete(0.0, "end")
    textbox_2.delete(0.0, "end")

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
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (operators('%')), text="%").grid(row=5, column=1, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (operators('/')), text="/").grid(row=5, column=2, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (operators('+')), text="+").grid(row=2, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (operators('-')), text="-").grid(row=3, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, height = 10, width = 75, command=lambda: (operators('*')), text="*").grid(row=4, column=3, padx=10, pady=10)
button = ctk.CTkButton(root, fg_color='green', height = 10, width = 75, command=ecuals, text="=").grid(row=5, column=3, padx=10, pady=10)
label = ctk.CTkLabel(root, text=f"CALC:").grid(row=0, column=0, padx=10, pady=10)
textbox_1 = ctk.CTkTextbox(root, height = 10, width = 75)
textbox_1.grid(row=0, column=1, padx=10, pady=10)
label = ctk.CTkLabel(root, text=f"RESULT:").grid(row=0, column=2, padx=10, pady=10)
textbox_2 = ctk.CTkTextbox(root, height = 10, width = 75)
textbox_2.grid(row=0, column=3, padx=10, pady=10)

root.mainloop()
