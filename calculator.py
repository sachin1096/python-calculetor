from tkinter import *
from tkinter.ttk import Frame, Button, Entry, Style
from tkinter.simpledialog import askfloat
class calculator(Frame):
	def __init__(self,m):
		super().__init__(m)
		self.opr=''
		self.x1=0.0
		self.y1=0.0
		per=0.0
		Style().configure("TButton", padding=(0, 5, 0, 5),font='algerian 10')
		
		self.b1=Button(self,text='1',command=self.one)
		self.b2=Button(self,text='2',command=self.two)
		self.b3=Button(self,text='3',command=self.three)
		self.b4=Button(self,text='4',command=self.four)
		self.b5=Button(self,text='5',command=self.five)
		self.b6=Button(self,text='6',command=self.six)
		self.b7=Button(self,text='7',command=self.seven)
		self.b8=Button(self,text='8',command=self.eight)
		self.b9=Button(self,text='9',command=self.nine)
		self.b10=Button(self,text='0',command=self.zero)
		self.b11=Button(self,text='+',command=self.plus)
		self.b12=Button(self,text='-',command=self.minus)
		self.b13=Button(self,text='*',command=self.multi)
		self.b14=Button(self,text='/',command=self.divide)
		self.b15=Button(self,text='=',command=self.equal)
		self.b16=Button(self,text='B',command=self.back)
		self.b17=Button(self,text='clear',command=self.clear)
		self.b18=Button(self,text='close',command=self.close)
		self.b19=Button(self,text='%',command=self.per)
		self.b20=Button(self,text='.',command=self.dot)
		self.t1=Entry(self,justify='center',font=('algerian',12))
		self.rowconfigure(index=0,pad=3)
		self.rowconfigure(index=1,pad=3)
		self.rowconfigure(index=2,pad=3)
		self.rowconfigure(index=3,pad=3)
		self.rowconfigure(index=4,pad=3)
		self.rowconfigure(index=5,pad=3)
		self.columnconfigure(index=0,pad=3)
		self.columnconfigure(index=1,pad=3)
		self.columnconfigure(index=2,pad=3)
		self.columnconfigure(index=3,pad=3)
        
		self.t1.grid(columnspan=4,sticky=W+E)
        
		self.b1.grid(row=1,column=0)
		self.b2.grid(row=1,column=1)
		self.b3.grid(row=1,column=2)
		self.b11.grid(row=1,column=3)
        
		self.b4.grid(row=2,column=0)
		self.b5.grid(row=2,column=1)
		self.b6.grid(row=2,column=2)
		self.b12.grid(row=2,column=3)
		
		self.b7.grid(row=3,column=0)
		self.b8.grid(row=3,column=1)
		self.b9.grid(row=3,column=2)
		self.b13.grid(row=3,column=3)
		
		self.b15.grid(row=4,column=0)
		self.b10.grid(row=4,column=1)
		self.b16.grid(row=4,column=2)
		self.b14.grid(row=4,column=3)
		
		self.b17.grid(row=5,column=0)
		self.b18.grid(row=5,column=1)
		self.b19.grid(row=5,column=2)
		self.b20.grid(row=5,column=3)
		
		self.pack()
	def one(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b1['text']
		self.t1.insert(0,v1+v2)
	def two(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b2['text']
		self.t1.insert(0,v1+v2)
	def three(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b3['text']
		self.t1.insert(0,v1+v2)
	def four(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b4['text']
		self.t1.insert(0,v1+v2)
	def five(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b5['text']
		self.t1.insert(0,v1+v2)
	def six(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b6['text']
		self.t1.insert(0,v1+v2)
	def seven(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b7['text']
		self.t1.insert(0,v1+v2)
	def eight(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b8['text']
		self.t1.insert(0,v1+v2)
	def nine(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b9['text']
		self.t1.insert(0,v1+v2)
	def zero(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b10['text']
		self.t1.insert(0,v1+v2)
	def plus(self):
		self.opr='+'
		self.x1=(float)(self.t1.get())
		self.t1.delete(0,'end')
	def minus(self):
		self.opr='-'
		self.x1=(float)(self.t1.get())
		self.t1.delete(0,'end')
	def multi(self):
		self.opr='*'
		self.x1=(float)(self.t1.get())
		self.t1.delete(0,'end')
	def divide(self):
		self.opr='/'
		self.x1=(float)(self.t1.get())
		self.t1.delete(0,'end')
	def equal(self):
		self.y1=(float)(self.t1.get())
		if self.opr=='+':
			self.x1+=self.y1
		elif self.opr=='-':
			self.x1-=self.y1
		elif self.opr=='*':
			self.x1*=self.y1
		elif self.opr=='/':
			self.x1/=self.y1
		elif self.opr=='%':
			self.x1=self.x1*(self.y1/100)
		self.t1.delete(0,'end')
		self.t1.insert(0,str(self.x1))
	def back(self):
		x=self.t1.get()
		self.t1.delete(0,'end')
		l=len(x)
		l=l-1
		x=x[:l]
		self.t1.insert(0,x)
	def clear(self):
		self.t1.delete(0,'end')
	def close(self):
		exit(0)
	def per(self):
		self.opr='%'
		self.x1=(float)(self.t1.get())
		self.t1.delete(0,'end')
	def dot(self):
		v1=self.t1.get()
		self.t1.delete(0,'end')
		v2=self.b20['text']
		self.t1.insert(0,v1+v2)
		
root=Tk()
ob=calculator(root)
root.title('Calculator')
root.geometry('420x220')
root.mainloop()