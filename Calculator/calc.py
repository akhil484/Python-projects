from tkinter import *
root=Tk()

root.title('Calculator')
e1=Entry(root,justify='right',borderwidth='5')
e1.grid(row=0,column=0,columnspan=6,padx=20,pady=5)


def button_click(number):
	current=e1.get()
	e1.delete(0,END)
	e1.insert(0,str(current)+str(number))


def button_clear():
	e1.delete(0,END)


def button_add():
	num1=e1.get()
	global f_num
	global math
	math = "addition"
	f_num=int(num1)
	e1.delete(0,END)



def button_Equal():
	num2=e1.get()
	e1.delete(0,END)
	num2=int(num2)
	if math=="addition":
		num2=int(num2)
		sum=f_num+num2
		e1.insert(0,sum)
	elif math=="subtraction":
		num2=int(num2)
		sub=f_num-num2
		e1.insert(0,sub)
	elif math=="Multiplication":
		num2=int(num2)
		mul=f_num*num2
		e1.insert(0,mul)
	elif math=="Division":
		num2=float(num2)
		div=f_num/num2
		e1.insert(0,div)



def button_sub():
	num1=e1.get()
	global f_num
	global math
	math = "subtraction"
	f_num=int(num1)
	e1.delete(0,END)



def button_mul():
	num1=e1.get()
	global f_num
	global math
	math = "Multiplication"
	f_num=int(num1)
	e1.delete(0,END)


def button_div():
	num1=e1.get()
	global f_num
	global math
	math = "Division"
	f_num=float(num1)
	e1.delete(0,END)


button1=Button(root,text='1',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(1))
button2=Button(root,text='2',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(2))
button3=Button(root,text='3',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(3))
button4=Button(root,text='4',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(4))
button5=Button(root,text='5',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(5))
button6=Button(root,text='6',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(6))
button7=Button(root,text='7',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(7))
button8=Button(root,text='8',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(8))
button9=Button(root,text='9',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(9))
button0=Button(root,text='0',padx=30,pady=20,bg="lightblue",font=('arial','10','bold'),command=lambda:button_click(0))
button_Add=Button(root,text='+',padx=27,pady=20,bg="Grey",font=('arial','10','bold'),command=button_add)
button_Sub=Button(root,text='-',padx=30,pady=20,bg="Grey",font=('arial','10','bold'),command=button_sub)
button_Mul=Button(root,text='*',padx=29,pady=20,bg="Grey",font=('arial','10','bold'),command=button_mul)
button_Div=Button(root,text='/',padx=30,pady=20,bg="Grey",font=('arial','10','bold'),command=button_div)
button_EQ=Button(root,text='=',padx=28,pady=20,bg="Grey",font=('arial','10','bold'),command=button_Equal)
button_CLR=Button(root,text='Clear',padx=17,pady=20,bg="Pink",font=('arial','10','bold'),command=button_clear)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
button0.grid(row=4,column=0)
button_Add.grid(row=1,column=3)
button_Sub.grid(row=2,column=3)
button_Mul.grid(row=3,column=3)
button_Div.grid(row=4,column=3)
button_EQ.grid(row=4,column=2)
button_CLR.grid(row=4,column=1)

root.resizable(0,0)
root.mainloop()


