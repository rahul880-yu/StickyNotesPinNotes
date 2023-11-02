import tkinter as tk
# install tkinter


def show():
    import time
    # import time
    current_time = time.strftime("%H:%M")
    # define time
    print("Heart fully thank you for using sticky notes, you can now create note's: ")
    # sleep for 2 second
    time.sleep(2)
    textIn = input("Drop your note's here:")
    note = ("*%s") % textIn
    time.sleep(2)
    # sleep for 2 second
    root = tk.Tk()
    root.title("Note your Note's")
    root.geometry("300x300")
    # dimention
    tk.Label(root, text=current_time).pack()
    tk.Label(root, text=note).pack()
    root.mainloop()


show()
