#cuberoot, integrals, matrix, square, cube

from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="#232323")
root.resizable(width=False, height=False)
root.geometry("480x570+20+20")

"""root1=TK()
root1.title("Conversion")
root1.configure(background="Gray")
root1.resizable(width=False, height=False)
root1.geometry("944x624+20+20")
"""
calc = Frame(root,bg="#545454")
calc.grid()


#=============Functions==================================================================================================

class Calc():
    def _init_(self):
        self.total=0
        self.current=""
      #  self.input_value=True
      #  self.check_sum=False
        self.op=""
      #  self.result=False
        self.expression=""
        self.ans=""
    def numberEnter(self, num):
       # self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
       # if self.input_value:
        self.current=secondnum
        #    self.input_value=False
        #else:
        if secondnum=='.':
            if secondnum in firstnum:
                    return
        if(txtDisplay.get()=="0"):
                self.current=secondnum
                self.expression =secondnum
                print("Empty string found")

        else:
                self.current=firstnum+secondnum
                self.expression = str(self.expression) + str(secondnum)
        #print("initial exp",self.expression)

        print(self.expression)
        self.display(self.expression)


    def sum_of_total(self):
       # self.result=True
       # self.current=float(self.current)
       # if self.check_sum==True:
           # self.input_value = True
        #    self.check_sum = False
        try:
                self.total=eval(self.expression)
        except Exception as e:
                self.expression="ERROR"
                print("Exception : ",e)

        self.ans = self.total
        #else:
        #self.total=float(txtDisplay.get())
        self.expression=self.total
        self.display(self.expression)


    def operation(self, op):
        #self.current=float(self.current)
        self.op=op

        if self.op=="add":
            self.expression=str(self.expression)+"+"
            print("plus added : ",self.expression)
        if self.op=="sub":
            self.expression=str(self.expression)+"-"
        if self.op=="multi":
            self.expression=str(self.expression)+"*"
        if self.op=="divide":
            self.expression=str(self.expression)+"/"
        if self.op=="mod":
            self.expression=str(self.expression)+"%"
        if self.op=="inv":
            self.expression=str(1)+"/"+str(self.expression)
        self.display(self.expression)

       # if not self.result:
        #self.total=self.current
        self.ans=self.total
        #    self.input_value=True
       # self.check_sum=True
        self.op=op
        #self.result=False

    def Clear_Entry(self):
       # self.result=False
        self.current=0
        self.expression=0
        self.display(0)
       # self.input_value=True
        print("Clr")

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0
        self.expression=""
        print("All clr")
    def tanh(self):
        self.reult=False
        self.current=math.tanh(math.radians(float(txtDisplay.get())))
        self.expression = "tanh(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)

    def tan(self):
        self.reult=False
        self.current=math.tan(math.radians(float(txtDisplay.get())))
        self.expression="tan("+str(txtDisplay.get())+")="+str(self.current)
        print(self.expression)
        self.display(self.expression)

    def sinh(self):
        self.reult=False
        self.current=math.sinh(math.radians(float(txtDisplay.get())))
        self.expression = "sinh(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)


    def sin(self):

        self.current=math.sin(math.radians(float(txtDisplay.get())))
        self.expression = "sin(" + txtDisplay.get()+")="+str(self.current)
        print(self.expression)
        self.display(self.expression)

    def log(self):
        self.reult=False

        self.current=math.log(float(txtDisplay.get()))
        self.expression = "log(" + str(txtDisplay.get()) +")="+str(self.current)
        print("log : ",self.expression)
        print(self.expression)
        self.display(self.expression)

    def exp(self):
        self.reult=False
        self.current=math.exp(float(txtDisplay.get()))
        self.expression = self.expression + "e" + txtDisplay.get()
        print(self.expression)
        self.display(self.current)

    def mathsPM(self):
        self.reult=False
        self.current=-(float(txtDisplay.get()))
        self.expression=self.current
        self.display(self.expression)

    def squared(self):
        self.current=math.sqrt(float(txtDisplay.get()))
        self.expression = "sqrt(" + str(txtDisplay.get())+")="+str(self.current)
        print(self.expression)
        self.display((self.expression))

    def cos(self):
       # self.reult=False
        self.current=math.cos(math.radians(float(txtDisplay.get())))
       # self.display(self.current)
        self.expression ="cos(" + str(txtDisplay.get())+")="+str(self.current)
        print(self.expression)
        self.display(self.expression)

    def cosh(self):
        self.reult=False
        self.current=math.cosh(math.radians(float(txtDisplay.get())))
        self.expression = "cosh(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)


    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
        print("total : ",self.total,"current: ",self.current,"expression : ",self.expression,"ans = ",self.ans)
    def pi(self):
        self.reult=False
        self.current=math.pi
        self.expression="pi="+str(self.current)
        self.display(self.expression)


    def e(self):
        self.reult=False
        self.current=math.e
        self.expression = "e = " + str(self.current)
        self.display(self.expression)

    def acosh(self):
       # self.result=False
        self.current=math.acosh(float(txtDisplay.get()))
        self.expression = "acosh(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)
    def asinh(self):
       # self.result=False
        self.current=math.asinh(float(txtDisplay.get()))
        self.expression = "asinh(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)


    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.expression = "degrees(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)

    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.expression="log2("+str(txtDisplay.get())+")="+str(self.current)
        self.display(self.expression)

    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.expression = "log10(" + str(txtDisplay.get()) +")=" + str(self.current)
        self.display(self.expression)


added_value=Calc()

#================Display================================================================================================


txtDisplay = Entry(calc, relief=SUNKEN, font=('arial', 20, 'bold'), bg="#578", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

#==================Numbers==============================================================================================

numberpad = "789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'),bg="#121212",fg="white", bd=2, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"]=lambda x=numberpad[i]: added_value.numberEnter(x)
        i+=1

#========================Standard Function==============================================================================================================================================

#btnClear=Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#f47", command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)
btnAllClear=Button(calc, text="CLR", width=6, height=2, font=('arial', 20, 'bold'), bd=2, bg="#f47",fg="white", command=added_value.all_Clear_Entry).grid(row=1, column=0, pady=1)

btnSq=Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4,fg="white", bg="#35f", command=added_value.squared).grid(row=1, column=1, pady=1)
btnAdd=Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#35f",fg="white", command=lambda:added_value.operation("add")).grid(row=1, column=3, pady=1)

btnSub=Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#35f",fg="white", command=lambda:added_value.operation("sub")).grid(row=2, column=3, pady=1)


vtnMult=Button(calc,text="x",width=6,height=2,font=('arial',20,'bold'),bd=4,bg="#35f",fg="white",command=lambda :added_value.operation(("multi"))).grid(row=3,column=3,pady=1)
btnDiv=Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#35f",fg="white" ,command=lambda:added_value.operation("divide")).grid(row=4, column=3, pady=1)
btnZero=Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,fg="white", bg="#39c", command=lambda:added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

btnZero=Button(calc, text="00", width=6, height=2, font=('arial', 20, 'bold'), bd=4,fg="white", bg="#39c", command=lambda:added_value.numberEnter("00")).grid(row=5, column=2, pady=1)

btnDot=Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#111",fg="white", command=lambda:added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
btnPM=Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4,fg="white", bg="#35f", command=added_value.mathsPM).grid(row=1, column=2, pady=1)

btnEquals=Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="#3c8", fg="white",command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

#===================Scientific Calculator====================================================================================================================================================

btnPi=Button(calc, text='π', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.pi).grid(row=1, column=4, pady=1)
btnCos=Button(calc, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.cos).grid(row=1, column=5, pady=1)

btnTan=Button(calc, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.tan).grid(row=1, column=6, pady=1)
btnSin=Button(calc, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.sin).grid(row=3, column=5, pady=1)

#btn2Pi=Button(calc, text='2π', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.tau).grid(row=2, column=4, pady=1)
btnCosh=Button(calc, text="cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.cosh).grid(row=2, column=5, pady=1)

btnTanh=Button(calc, text="tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.tanh).grid(row=2, column=6, pady=1)
btnSinh=Button(calc, text="sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.sinh).grid(row=3, column=6, pady=1)

btnLog=Button(calc, text='log', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log).grid(row=3, column=4, pady=1)
btninv=Button(calc, text="Inv", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=lambda:added_value.operation("inv")).grid(row=5, column=5, pady=1)

btnMod=Button(calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4, command=lambda:added_value.operation("mod")).grid(row=5, column=4, pady=1)
btnE=Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.e).grid(row=2, column=4, pady=1)

btnLog2=Button(calc, text='log2', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log2).grid(row=4, column=4, pady=1)
btnDeg=Button(calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.degrees).grid(row=4, column=5, pady=1)

btnAcosh=Button(calc, text="acosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.acosh).grid(row=4, column=6, pady=1)
btnAsinh=Button(calc, text="asinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.asinh).grid(row=5, column=6, pady=1)

#btnLog10=Button(calc, text='log10', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log10).grid(row=5, column=4, pady=1)
#btnLog1p=Button(calc, text="log1p", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.log1p).grid(row=5, column=5, pady=1)

#btnExpm1=Button(calc, text="expm1", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.expm1).grid(row=5, column=6, pady=1)
#btnLgamma=Button(calc, text="lgamma", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Aqua", command=added_value.lgamma).grid(row=5, column=7, pady=1)








#=======================Menu and function===========================================================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("830x570+20+20")
    #txtDisplay.configure(width="55")
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x570+20+20")


menubar = Menu(calc)


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label = "Standadrd", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)


#====================Main Loop=============================================================================

root.config(menu=menubar)
root.mainloop()