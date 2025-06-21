'''

# CLI Version Command Line Calculator
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Error: Divition error by zero"
    return a / b

print("Simple CIL Calcultor")
print("Operations: + - * /")


while True:
    try:

        num1 = int(input("Enter first number: "))
        op  = input("Enter Operator: ")
        num2 = int(input("Enter second number: "))

        if op == '+':
            print("result: ",add(num1, num2))
        elif op == '-':
            print("result:",subtract(num1, num2))
        elif op == '*':
            print("result:",multiply(num1, num2))
        elif op == '/':
            print("result:",divide(num1, num2))
        else:
            print("Invalid operator.")

        again = input("do you want calculate agian pls (y/n): ")
        if again.lower() != 'y':
            break
    except ValueError:
        print("Invalid input. Pls enter numbers.")
'''
import tkinter as tk 

def click(event):
    text  = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0,tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "c":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("simple Calculator")
root.geometry("300x400")


entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()