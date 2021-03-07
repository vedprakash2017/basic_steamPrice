import tkinter as tk
import math
root= tk.Tk(className='Ved')
multi = 1.7
canvas1 = tk.Canvas(root, width = 600, height = 300 , bg = '#8fc0eb')
canvas2 = tk.Canvas(root, width = 500, height = 700, bg = '#215b8f')
canvas1.pack()
sp_var=tk.StringVar()
bp_var=tk.StringVar()

def submit():
	sp=float(sp_var.get())
	bp=float(bp_var.get())
	prec = (bp*10)/sp*100

	# print("buff price is ", "{:.2f}". format(prec) ," %  of market \n")
	l1 = tk.Label(root, text = '%  of Market ', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(250, 25, window=l1)
	li1 = tk.Label(root, text = "{:.2f} % ". format(prec), font=('calibre',15, 'bold') )
	canvas2.create_window(250, 60, window=li1)


	l1 = tk.Label(root, text = 'Market Price', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(125, 125, window=l1)
	li1 = tk.Label(root, text = str(sp)+" ₹ ", font=('calibre',15, 'bold'))
	canvas2.create_window(125, 160, window=li1)	

	l1 = tk.Label(root, text = 'Buff Price', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(375, 125, window=l1)
	li1 = tk.Label(root, text = str(bp)+" ¥ ", font=('calibre',15, 'bold'))
	canvas2.create_window(375, 160, window=li1)


	
	pro = bp*multi*0.97*0.86*10
	overl = pro/sp
	
	# print("overall back price is ", "{:.2f}". format(pro) , ". Profit", "{:.2f}". format(overl) ,"\n")
	# print("according to this ratio profit %  in a month (if go in 10 days)", "{:.2f}". format(overl*overl*overl), "\n")

	l1 = tk.Label(root, text = 'Profit %', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(125, 225, window=l1)
	li1 = tk.Label(root, text = "{:.2f} %". format(overl), font=('calibre',15, 'bold'))
	canvas2.create_window(125, 260, window=li1)

	l1 = tk.Label(root, text = 'Profit %  in a Month', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(375, 225, window=l1)
	li1 = tk.Label(root, text = "{:.2f} %". format(overl*overl*overl), font=('calibre',15, 'bold'))
	canvas2.create_window(375, 260, window=li1)

	
	days = int(30/math.log(1.35,overl))
	
	# print("It must sell in ", days-7 ,"days on buff and in" , days ,"days on overall \n")

	l1 = tk.Label(root, text = 'Max Days on Buff ', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(125, 325, window=l1)
	li1 = tk.Label(root, text = str(days-7)+" days", font=('calibre',15, 'bold'))
	canvas2.create_window(125, 360, window=li1)	

	l1 = tk.Label(root, text = 'Max Overall Days', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(375, 325, window=l1)
	li1 = tk.Label(root, text = str(days)+" days", font=('calibre',15, 'bold'))
	canvas2.create_window(375, 360, window=li1)

	# print("Steam lowest price is ", "{:.2f}". format( bp*10*multi*0.97)," after tax we get ", "{:.2f}". format( pro) ,"\n")

	l1 = tk.Label(root, text = 'Steam Lowest Price', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(125, 425, window=l1)
	li1 = tk.Label(root, text = "{:.2f} ₹ ". format( bp*10*multi*0.97), font=('calibre',15, 'bold'))
	canvas2.create_window(125, 460, window=li1)

	l1 = tk.Label(root, text = 'After Tax', font=('calibre',15, 'bold'),bg='#215b8f',fg='#8fc0eb')
	canvas2.create_window(375, 425, window=l1)
	li1 = tk.Label(root, text = "{:.2f} ₹ ". format( pro), font=('calibre',15, 'bold'))
	canvas2.create_window(375, 460, window=li1)

	sp_var.set("")
	bp_var.set("")
	back_btn = tk.Button(text='back',command=back,font=('calibre',15,'normal'))
	canvas2.create_window(250, 570, window=back_btn)
	canvas1.pack_forget()
	canvas2.pack()

def back ():  
	canvas2.pack_forget()
	canvas1.pack()
	canvas2.delete("all")
     
sp_label = tk.Label(root, text = 'Steam Price', font=('calibre',15, 'bold'))
canvas1.create_window(150, 50, window=sp_label)

sp_entry = tk.Entry(root,textvariable = sp_var, font=('calibre',15,'normal'))
canvas1.create_window(150, 150, window=sp_entry)

bp_label = tk.Label(root, text = 'Buff Price', font=('calibre',15, 'bold'))
canvas1.create_window(450, 50, window=bp_label)

bp_entry = tk.Entry(root,textvariable = bp_var, font=('calibre',15,'normal'))
canvas1.create_window(450, 150, window=bp_entry)

sub_btn=tk.Button(root,text = 'Submit', command = submit , font=('calibre',15,'normal'))
canvas1.create_window(300, 250, window=sub_btn)


# sp_label.grid(row=0,column=0)
# sp_entry.grid(row=0,column=1)
# bp_label.grid(row=1,column=0)
# bp_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)
root.mainloop()
