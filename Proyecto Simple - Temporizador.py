"""Temporizador"""
import tkinter as tk
import tkinter.messagebox as mb
from sys import exit
from datetime import timedelta
class Tempo:
    def __init__(self):
        self.run=True
        self.ven=tk.Tk()
        self.ven.title("Temporizador")
        la1=tk.Label(self.ven,text="Horas: ")
        la1.grid(column=0,row=0,padx=5,pady=5)
        la2=tk.Label(self.ven,text="Minutos: ")
        la2.grid(column=0,row=1,padx=5,pady=5)
        la3=tk.Label(self.ven,text="Segundos: ")
        la3.grid(column=0,row=2,padx=5,pady=5)
        self.hor=tk.StringVar()
        self.min=tk.StringVar()
        self.seg=tk.StringVar()
        self.t_hor=self.hor.trace_add("write",self.compro)
        self.t_min=self.min.trace_add("write",self.compro)
        self.t_seg=self.seg.trace_add("write",self.compro)
        self.en1=tk.Entry(self.ven,width=5,textvariable=self.hor)
        self.en1.grid(column=1,row=0,padx=5,pady=5)
        self.en2=tk.Entry(self.ven,width=5,textvariable=self.min)
        self.en2.grid(column=1,row=1,padx=5,pady=5)
        self.en3=tk.Entry(self.ven,width=5,textvariable=self.seg)
        self.en3.grid(column=1,row=2,padx=5,pady=5)
        self.la=tk.Label(self.ven,text="00:00:00",font=("Arial",40))
        self.la.grid(column=0,row=3,columnspan=2,rowspan=2)
        self.bo1=tk.Button(self.ven,text="Iniciar",command=self.ini,state="disabled")
        self.bo1.grid(column=0,row=5,padx=5,pady=5)
        self.bo2=tk.Button(self.ven,text="Pausar",command=self.pau,state="disabled")
        self.bo2.grid(column=1,row=5,padx=5,pady=5)
        self.bo3=tk.Button(self.ven,text="Continuar",command=self.cont,state="disabled")
        self.bo3.grid(column=0,row=6,padx=5,pady=5)
        self.bo4=tk.Button(self.ven,text="Reiniciar", command=self.reini,state="disabled")
        self.bo4.grid(column=1,row=6,padx=5,pady=5)
        self.ti=self.ven.after(1000,self.actu)
        self.ven.mainloop()
    def compro(self, *_):
        num=[]
        cond=[]
        num.append(self.hor.get())
        num.append(self.min.get())
        num.append(self.seg.get())
        for x in range (len(num)):
            cond.append(self.digitos(num[x]))
        if (cond[0]==True)&(cond[1]==True)&(cond[2]==True):
            self.bo1.configure(state="normal") 
        else:
            self.bo1.configure(state="disabled")
    def digitos(self,a):
        if a.isdigit():
            return True
        else:
            return False
    def ini(self):
        self.hor.trace_remove("write",self.t_hor)
        self.min.trace_remove("write",self.t_min)
        self.seg.trace_remove("write",self.t_seg)
        self.run=True
        self.bo2.configure(state="normal")
        self.bo3.configure(state="normal")
        self.bo4.configure(state="normal")
        a1=self.hor.get()
        a2=self.min.get()
        a3=self.seg.get()
        a=a1+":"+a2+":"+a3
        self.segu=self.conve(a)
        self.sec=0
        self.actu()
    def pau(self):
        self.run=False
        self.ven.after_cancel(self.ti)
        self.sec-=1
    def conve(self,a):
        #sumatoria de los resultados de convertir cada valor a segundos
        #i for i va desde 0 a 2, de tal forma que quedaria:
        #seg * (60^0); min * (60^1); hora * 60^2
        return sum(int(x) * 60 ** i for i, x in enumerate(reversed(a.split(':'))))
    def actu(self):
        try:
            self.sec+=1
            if (self.sec<=self.segu)&(self.run==True):
                tt=str(timedelta(seconds=self.sec))
                self.la.configure(text=tt)
                self.ven.after(1000,self.actu)
            else:
                self.ven.after_cancel(self.ti)
        except AttributeError:
            pass
    def cont(self):
        self.run=True
        self.actu()
    def reini(self):
        self.la.configure(text="00:00:00")
        self.run=False
        self.hor.set("")
        self.min.set("")
        self.seg.set("")
        self.t_hor=self.hor.trace_add("write",self.compro)
        self.t_min=self.min.trace_add("write",self.compro)
        self.t_seg=self.seg.trace_add("write",self.compro)
app=Tempo()