import tkinter as tk

def add():
    lbx.insert(tk.END, to_do_item.get())
    to_do_itementery.delete(0, tk.END)

def del_item():
    lbx.delete(delItem.get()-1)
    delItementry.delete(0, tk.END)

def main():
    global to_do_item, to_do_itementery, lbx, delItem, delItementry
    r=tk.Tk()
    r.geometry('400x400')
    r.title('To Do List')
    r.config(bg='#2a9d8f')
    tk.Label(r, fg='#264653', text='To Do List', font='Arial 20 bold', bg='#2a9d8f').pack(pady=10)
    
    f=tk.Frame(r, bg='#2a9d8f')
    f.pack(pady=10)
    tk.Label(f, text='Add task:', font='Arial 12', bg='#2a9d8f').grid(row=0, column=0, padx=10)
    to_do_item=tk.StringVar()
    to_do_itementery=tk.Entry(f, textvariable=to_do_item, width=25, font='Arial 12')
    to_do_itementery.grid(row=0, column=1, padx=10)
    tk.Button(f, text='Add', bg='green', fg='white', font='Arial 12', command=add).grid(row=0, column=2, padx=10)
    
    f2=tk.Frame(r, bg='#2a9d8f')
    f2.pack(pady=10, fill=tk.BOTH, expand=True)
    lbx= tk.Listbox(f2, width=50, height=10, font='Arial 12')
    lbx.grid(row=0, column=0, sticky='nsew')
    scrollbar=tk.Scrollbar(f2, orient=tk.VERTICAL, command=lbx.yview)
    scrollbar.grid(row=0, column=1, sticky='ns')
    lbx.config(yscrollcommand=scrollbar.set)
    f2.columnconfigure(0, weight=1)
    f2.rowconfigure(0, weight=1)

    f3=tk.Frame(r, bg='#2a9d8f')
    f3.pack(pady=10)
    tk.Label(f3, text="Dlete task (Position):", font='Arial 12', bg='#2a9d8f').grid(row=0, column=0, padx=10)
    delItem=tk.IntVar()
    delItementry=tk.Entry(f3, textvariable=delItem, width=5, font='Arial 12')
    delItementry.grid(row=0, column=1, padx=10)
    tk.Button(f3, text='Delete', bg='Red', fg='white', font='Arial 12', command=del_item).grid(row=0, column=2, padx=10)
    r.mainloop()

if __name__ == "__main__":
    main()