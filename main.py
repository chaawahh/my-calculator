import tkinter as tk

class mycalculator:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title('my calaulator')

        self.label = tk.Label(self.root, text='my calculator', font=('Arial', 30))
        self.label.pack()

        self.button=tk.Button(self.root, text='Click here')
        self.button.place(x=20, y=50)

        self.root.mainloop()

mycalculator()