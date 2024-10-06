from tkinter import Tk, Button, Label, StringVar

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry('335x500')
        self.master.title('Calculator')
        self.master.config(bg='#111')
        self.master.resizable(False, False)
        
        self.char = ''
        self.result = StringVar()
        self.variable = ""
        
        self.result_label = Label(self.master, textvariable=self.result, font='Arial, 40', width='20', height='1', bg='gray', fg='white', anchor='e')
        self.result_label.pack(pady=15)
        
        Button(self.master, font='Arial, 30', text='0', width=2, bg='gray', command=lambda:self.calc("0")).place(x = 90, y = 420)
        Button(self.master, font='Arial, 30', text='1', width=2, bg='gray', command=lambda:self.calc("1")).place(x = 10, y = 345)
        Button(self.master, font='Arial, 30', text='2', width=2, bg='gray', command=lambda:self.calc("2")).place(x = 90, y = 345)
        Button(self.master, font='Arial, 30', text='3', width=2, bg='gray', command=lambda:self.calc("3")).place(x = 170, y = 345)
        Button(self.master, font='Arial, 30', text='4', width=2, bg='gray', command=lambda:self.calc("4")).place(x = 10, y = 270)
        Button(self.master, font='Arial, 30', text='5', width=2, bg='gray', command=lambda:self.calc("5")).place(x = 90, y = 270)
        Button(self.master, font='Arial, 30', text='6', width=2, bg='gray', command=lambda:self.calc("6")).place(x = 170, y = 270)
        Button(self.master, font='Arial, 30', text='7', width=2, bg='gray', command=lambda:self.calc("7")).place(x = 10, y = 195)
        Button(self.master, font='Arial, 30', text='8', width=2, bg='gray', command=lambda:self.calc("8")).place(x = 90, y = 195)
        Button(self.master, font='Arial, 30', text='9', width=2, bg='gray', command=lambda:self.calc("9")).place(x = 170, y = 195)
        
        Button(self.master, font='Arial, 30', text='.', width=2, bg='gray', command=lambda:self.calc(".")).place(x = 10, y = 420)
        Button(self.master, font='Arial, 30', text='+', width=2, bg='gray', command=lambda:self.calc("+")).place(x = 170, y = 420)
        Button(self.master, font='Arial, 30', text='-', width=2, bg='gray', command=lambda:self.calc("-")).place(x = 250, y = 345)
        Button(self.master, font='Arial, 30', text='=', width=2, bg='orange', fg='white', command=lambda:self.calc("=")).place(x = 250, y = 420)
        Button(self.master, font='Arial, 30', text='×', width=2, bg='gray', command=lambda:self.calc("*")).place(x = 250, y = 270)
        Button(self.master, font='Arial, 30', text='÷', width=2, bg='gray', command=lambda:self.calc("/")).place(x = 250, y = 195)
        Button(self.master, font='Arial, 30', text='C', width=2, bg='gray', command=lambda:self.clear("all")).place(x = 250, y = 120)
        Button(self.master, font='Arial, 30', text=')', width=2, bg='gray', command=lambda:self.calc(")")).place(x = 170, y = 120)
        Button(self.master, font='Arial, 30', text='(', width=2, bg='gray', command=lambda:self.calc("(")).place(x = 90, y = 120)
        Button(self.master, font='Arial, 30', text='⌫', width=2, bg='gray', command=lambda:self.clear("last")).place(x = 10, y = 120)
        
        
    def calc(self, value):
        try:
            if value == '=':
                try:
                    self.solve = eval(self.variable)
                    if '.' in str(self.solve):
                        self.part = str(self.solve).split('.')
                        if len(self.part[1]) > 1:
                            if len(self.part[1]) > 6:
                                self.solve = f'~{round(self.solve,6)}'
                                self.result.set(self.solve)
                            else:
                                self.result.set(self.solve)
                        else:
                            if '.0' in str(self.solve):
                                self.result.set(int(self.solve))
                            else:
                                self.result.set(self.solve)
                    else:
                        if len(str(self.solve)) > 25:
                                self.solve = "Too big number"
                                self.result_label.config(font='Arial, 30')
                                self.result.set(self.solve)
                        else:
                            self.result.set(int(self.solve))
                except ValueError:
                    self.solve = "Too big number"
                    self.result_label.config(font='Arial, 30')
                    self.result.set(self.solve)
                except:
                    if self.variable == "":
                        pass
                    else:
                        self.result.set('Error!')
            else:
                self.variable += str(value)
                self.result.set(self.variable)
        except:
            self.result.set("Error!")
        
    def clear(self, value):
        if value == "all":
            self.variable = ""
            self.result.set(self.variable)
            self.solve = ""
            self.result_label.config(font='Arial, 40')
        elif value == "last":
            self.variable = self.variable[:-1]
            self.result.set(self.variable)
        else:
            pass

root = Tk()
app = App(root)
root.mainloop()