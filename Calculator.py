import tkinter as tk

def calculate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")
root=tk.Tk()
root.title('Simple Calculator')
entry= tk.Entry(root)
entry.pack()
calculate_button=tk.Button(root,text="Calculate",command=calculate)
calculate_button.pack()
result=tk.StringVar()
result_label=tk.Label(root,textvariable=result)
result_label.pack()
root.mainloop()           