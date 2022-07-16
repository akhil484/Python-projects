import random,tkinter
from tkinter import *
def fn():
	print ("Magic 8 ball");
	a=input("Enter your question:");
	print ("..............");
	print ("thinking........");
	a=['yes Definitely','yes','without a doubt','ask again later','cannot predict now','Better not tell you now',
		'sign points to yes','you may rely on it','outlook good','As i see it,yes','it is certain'];
	print (a[random.randint(0,10)]);
def ex():
	exit();
root=Tk();
root.title("Magic 8 ball");
root.geometry("500x200");
app=Frame(root);
app.grid();
button1=Button(app,text="Ask",command=fn);
button1.grid();
button2=Button(app,text="play again",command=fn);
button2.grid();
button3=Button(app,text="quit",command=ex);
button3.grid();
root.mainloop();

