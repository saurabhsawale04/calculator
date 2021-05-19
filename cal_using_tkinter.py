# SAWALE SAURABH SURESH


from tkinter import *
from ast import literal_eval
import matplotlib.pyplot as plt



#from numpy import *
import numpy as np

class LeftFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master,bg="green")
        self.master = master
        self.grid(row=0, column=0,sticky=NW)
        master.grid_columnconfigure(0,weight=1)
        master.grid_rowconfigure(0,weight=1)
        self.textbox = Text(self,width=40,height=21,padx=10,pady=10,bd=5,bg="wheat",fg="black",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.textbox.insert(END,"Enter variable name here")
        self.textbox.grid(row=0,column=0,sticky=NW)

    def insert(self, ins_string):
        textbox.insert(END,ins_string)



class RightFrame(Frame):
    def __init__(self, master=None,lframe=None):
        Frame.__init__(self, master, bg="white")
        self.master = master
        self.lframe = lframe
        self.grid(row=0, column=1,sticky=N+E+W+S)
        master.grid_columnconfigure(1,weight=1)

        self.lab1 = Label(self,text="Expression :",width=20,height=5,padx=2,pady=2,bg="yellow",fg="black",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.lab1.grid(row=0,column=0,sticky=N+E+S+W)

        self.exprtext = Text(self,width=20,height=5,padx=2,pady=2,bg="orange",fg="black",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.exprtext.insert(END, "Enter exp here")
        self.exprtext.grid(row=0,column=1,sticky=S+N+E+W)

        self.lab2 = Label(self,text="Range (a, b) :",width=20,height=5, bg="yellow",fg="black",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.lab2.grid(row=1, column=0,sticky=S+N+E+W)

        self.variablevalue = Text(self,width=20,height=5,padx=2,pady=2,bg="orange",fg="black",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.variablevalue.insert(END, "Enter range here")
        self.variablevalue.grid(row=1,column=1,sticky=S+N+E+W)


        self.evaluatebutton = Button(self,text="Evaluate !",command=self.evaluate,width=20,height=4,padx=2,pady=2,bg="blue",fg="white",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.evaluatebutton.grid(row=2, column=0,sticky=S+N+E+W)

        self.plotbutton = Button(self,text="Plot", command=self.plot,width=20,height=5,padx=2,pady=2,bg="blue",fg="white",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.plotbutton.grid(row=2,column=1,sticky=S+N+E+W)

        self.exitbutton = Button(self, text="Exit", command=exit, width=20, height=5, padx=2, pady=2,bg="red",fg="black",font=("comicsansms", 15, "bold"),relief="raised",borderwidth=2)
        self.exitbutton.grid(row=3, column=0,columnspan=2, sticky=S+N+E+W)


    def plot(self):

        expr = self.exprtext.get(1.0, END)
       # print(expr)
        varval = self.variablevalue.get(1.0, END)
        #print(varval)
        a = literal_eval(varval)
       # self.lframe.textbox.delete(1.0, END)
        #print(a)
        y = []
        z = []
        for x in np.linspace(a[0], a[1], 100):
            expr = expr.strip('\n')
            z.append(x)
            y.append(eval(expr))
            #print(expr + ' ( ' + str(x) + ' ) ' + ' = ' + str(y))
            #self.lframe.textbox.insert(END, expr + ' ( ' + str(x) + ' ) ' + ' = ' + str(y) + '\n')



        plt.plot(z, y)
        plt.xlabel('x')
        plt.ylabel(expr)
        plt.title('x vs '+expr)
        plt.show()


    def evaluate(self):
        expr=self.exprtext.get(1.0,END)
        print(expr)
        varval=self.variablevalue.get(1.0,END)
        print(varval)
        a=literal_eval(varval)
        self.lframe.textbox.delete(1.0,END)
        print(a)
        for x in np.linspace(a[0],a[1],10):
            expr=expr.strip('\n')
            y=eval(expr)
            print(expr+' ( '+str(x)+' ) '+' = '+str(y))
            self.lframe.textbox.insert(END,expr+' ( '+str(x)+' ) '+' = '+str(y)+'\n')



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        master.geometry("1000x600")
        self.leftframe = LeftFrame(master)
        self.rightframe = RightFrame(master,self.leftframe)
        master.wm_title("expression calculator")
        self.grid(row=0,column=0,sticky="nsew")


# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Tkinter window")

# show window
root.mainloop()