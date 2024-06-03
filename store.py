from tkinter import *


root = Tk()
root.config(bg="#FFFFFF")


#FRAMES
product1Frame=LabelFrame(root,text='Suitcase - Blue',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))
product2Frame=LabelFrame(root,text='Lorem ipsum',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))

#WHITESPACE
whitespace1=Label(product1Frame,bg='#FFFFFF')
whitespace2=Label(product1Frame,bg='#FFFFFF')
whitespace3=Label(product2Frame,bg='#FFFFFF')
whitespace4=Label(product2Frame,bg='#FFFFFF')


#BUTTONS
atibaStoreButton = Button(root,text='Atiba Store',font=('Gill Sans',20),bg="#e39700",activebackground='#FFFFFF',relief=FLAT)

applyButton = Button(root,text='Apply',font=('Gill Sans',20),bg="#FFFFFF",relief=RAISED)

#LABELS
cartLabel = Label(root,text='Your Cart',font=('Gill Sans',30),background='#FFFFFF',foreground='#000000')

quantityLabel = Label(root,text='QUANTITY',font=('Gill Sans',10),background='#FFFFFF',foreground='#8f8f8f')
totalLabel = Label(root,text='TOTAL',font=('Gill Sans',10),background='#FFFFFF',foreground='#8f8f8f')

price1 = StringVar()
price1.set('$100')
price1Label = Label(product1Frame,textvariable=price1,font=('Gill Sans',15),background='#FFFFFF',foreground='#000000')

price2 = StringVar()
price2.set('$100')
price2Label = Label(product2Frame,textvariable=price1,font=('Gill Sans',15),background='#FFFFFF',foreground='#000000')

discountLabel = Label(root,text='COUPON',font=('Gill Sans',15),background='#FFFFFF',foreground='#8f8f8f')

#SCALES
admin = IntVar()
adminScale = Scale(root, from_=1, to=2, variable = admin, width = 20, length=50, orient=VERTICAL,bd=0,bg='#FFFFFF',fg='#000000',label='Admin Mode',font=('Gill Sans',10))

#IMAGES
suitcase = PhotoImage(file='images/suitcase.png')
suitcaseLabel = Label(product1Frame,image=suitcase,bd=0)

table = PhotoImage(file='images/table.png')
tableLabel = Label(product2Frame,image=table,bd=0)

#SPINBOX
spin1 = IntVar()
spin1.set(1)
prod1spin = Spinbox(product1Frame, width=3, textvariable=spin1, from_=1, to=999,background='#FFFFFF',highlightbackground='#FFFFFF',foreground='#000000')

spin2 = IntVar()
spin2.set(1)
prod2spin = Spinbox(product2Frame, width=3, textvariable=spin2, from_=1, to=999,background='#FFFFFF',highlightbackground='#FFFFFF',foreground='#000000')

#ENTRY
code = StringVar()
codeEntry=Entry(root,textvariable=code,width=10,fg='#000000',bg='#FFFFFF',bd=0)

#GRIDDING
atibaStoreButton.grid(column=1,row=1)
cartLabel.grid(column=2,row=2)
quantityLabel.grid(column=3,row=3,sticky=W)
totalLabel.grid(column=4,row=3)

product1Frame.grid(row=4,column=1,columnspan=4,sticky=W,padx=5,pady=5)
product2Frame.grid(row=5,column=1,columnspan=4,sticky=W,padx=5)

#products
#...
suitcaseLabel.grid(column=1,row=1)
prod1spin.grid(column=3,row=1)
whitespace1.grid(column=2,row=1,padx=125)
whitespace2.grid(column=4,row=1,padx=35)
price1Label.grid(column=5,row=1,padx=10)

tableLabel.grid(column=1,row=1)
prod2spin.grid(column=3,row=1)
whitespace3.grid(column=2,row=1,padx=100)
whitespace4.grid(column=4,row=1,padx=40)
price2Label.grid(column=5,row=1,padx=10)
#'''

discountLabel.grid(row=6,column=3)
codeEntry.grid(row=7,column=3,sticky=E,ipady=3)
applyButton.grid(row=7,column=4,sticky=W)

adminScale.grid(row=7,column=1,sticky=W)

root.mainloop()
