import tkinter as tk

def add():
    result.set(float(entry1.get())+ float(entry2.get()))
def sub():
    result.set(float(entry1.get())- float(entry2.get()))
def mul():
    result.set(float(entry1.get())* float(entry2.get()))
def div():
    result.set(float(entry1.get())// float(entry2.get()))

root = tk.Tk()
root.title("simple calculator")

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

result = tk.DoubleVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

add_button = tk.Button(root, text="add", command=add)
add_button.pack()

sub_button = tk.Button(root, text="sub", command=sub)
sub_button.pack()

mul_button = tk.Button(root, text="mul", command=mul)
mul_button.pack()

div_button = tk.Button(root, text="div", command=div)
div_button.pack()

root.mainloop()
