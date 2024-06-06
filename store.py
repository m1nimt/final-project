from tkinter import * # type: ignore
from tkinter import messagebox
import random
from tokenize import String

root = Tk()

admin_off=Frame(root)
admin_off.config(bg="#FFFFFF")

#functions
def remove_text(ignore):
    code.set('')
    codeEntry.config(fg='#000000')

def add_text(ignore):
    codeEntry.config(fg='#8f8f8f')
    code.set('Coupon here')

    already_appliedLabel.grid_remove()
    bad_couponLabel.grid_remove()

    if new_subtotalLabel.grid_info != False:
        current_couponLabel.grid()


    
def atiba_store():
    messagebox.showinfo('Atiba Store','Welcome to the Atiba Store! We offer all sorts of products and goods.\nWe also offer a *FREE* cart editing planner!\nIt seems you currently are testing it out! Try clicking the "admin" swtich on the bottom left.')

def quantity_1():
    price = price1_value.get()
    quantity = spin1.get()
    price1.set(f'${price*quantity}')
    subtotalPrice.set(f'${(float(price1.get().replace('$',''))) + (float(price2.get().replace('$','')))}')


def quantity_2():
    price = price2_value.get()
    quantity = spin2.get()
    price2.set(f'${price*quantity}')
    subtotalPrice.set(f'${(int(price1.get().replace('$',''))) + (int(price2.get().replace('$','')))}')



def coupon_apply():
    global valid_coupons,already_applied,user_code
    #valid coupons is a list of coupons
    user_code = code.get()
    #users inputed coupon

    if user_code ==' ' or user_code == '' or user_code == 'Enter here':
        already_appliedLabel.grid_remove()
        bad_couponLabel.grid_remove()
    
    elif user_code.lower() == 'clear':
        already_appliedLabel.grid_remove()
        bad_couponLabel.grid_remove()
        new_subtotalLabel.grid_remove()
        current_couponLabel.grid_remove()
        subtotalPriceLabel.config(foreground='#000000')


    elif user_code not in valid_coupons:
        already_applied = user_code
        already_appliedLabel.grid_remove()
        bad_couponLabel.grid()
        

    elif user_code == already_applied:
        already_applied = user_code
        bad_couponLabel.grid_remove()
        current_couponLabel.grid_remove()
        already_appliedLabel.grid()

    else:
        already_appliedLabel.grid_remove()
        already_applied = user_code
        bad_couponLabel.grid_remove()
        

        value_of_coupon = ''
            
        for letter in user_code:
            if letter.isnumeric()==True:
                value_of_coupon+=letter

        value_of_coupon = (100 - int(value_of_coupon)) / 100
        
        subtotalPriceLabel.config(foreground='#ff0000')

        subtotalPrice_float = float(subtotalPrice.get().replace('$',''))
        
        new_subtotal.set(f'${round(subtotalPrice_float*value_of_coupon)}')
        new_subtotalLabel.grid()

        current_coupon.set(f'Coupon applied: {user_code}')
        current_couponLabel.grid()

#FRAMES
product1Frame=LabelFrame(admin_off,text='Suitcase - Blue',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))
product2Frame=LabelFrame(admin_off,text='Lorem ipsum',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))

#WHITESPACE
whitespace1=Label(product1Frame,bg='#FFFFFF')
whitespace2=Label(product1Frame,bg='#FFFFFF')
whitespace3=Label(product2Frame,bg='#FFFFFF')
whitespace4=Label(product2Frame,bg='#FFFFFF')


#BUTTONS
atibaStoreButton = Button(admin_off,text='Atiba Store',font=('Gill Sans',20),bg="#FFFFFF",activebackground='#FFFFFF',relief=FLAT,command=atiba_store)

applyButton = Button(admin_off,text='Apply',font=('Gill Sans',20),bg="#e39700",activebackground='#8c5e00',relief=RAISED,command=coupon_apply)

#SCALES
admin = IntVar()
adminScale = Scale(admin_off, from_=1, to=2, variable = admin, width = 20, length=50, orient=VERTICAL,bd=0,bg='#FFFFFF',fg='#000000',label='Admin Mode',font=('Gill Sans',10))

#IMAGES
suitcase = PhotoImage(file='images/suitcase.png')
suitcaseLabel = Label(product1Frame,image=suitcase,bd=0)

table = PhotoImage(file='images/table.png')
tableLabel = Label(product2Frame,image=table,bd=0)

#SPINBOX
spin1 = IntVar()
spin1.set(1)
prod1spin = Spinbox(product1Frame, width=3, textvariable=spin1, from_=1, to=random.randint(2,30),background='#FFFFFF',highlightbackground='#FFFFFF',foreground='#000000',command=quantity_1)

spin2 = IntVar()
spin2.set(1)
prod2spin = Spinbox(product2Frame, width=3, textvariable=spin2, from_=1, to=random.randint(2,30),background='#FFFFFF',highlightbackground='#FFFFFF',foreground='#000000',command=quantity_2)

#ENTRY
code = StringVar()
code.set('Coupon here')
codeEntry=Entry(admin_off,textvariable=code,width=10,fg='#8f8f8f',bg='#FFFFFF',bd=2)
codeEntry.bind("<FocusIn>", remove_text)
codeEntry.bind("<FocusOut>", add_text)

#COUPON LISTS
valid_coupons = [
    "15SUMMER", "40BONUS", "20WINTER", "25FALL", "10SPRING",
    "WELCOME30", "50HOLIDAY", "VIP35", "45NEWYEAR", "20AUTUMN",
    "60FLASHSALE", "5DISCOUNT", "55CLEARANCE", "25SPECIAL", "SAVE15",
    "30GIFT", "40EXTRA", "50BLACKFRIDAY", "45CYBERMONDAY", "20NEWBIE"
]


already_applied = ''

coupon_entered = ''

#LABELS
cartLabel = Label(admin_off,text='Your Cart',font=('Gill Sans',30),background='#FFFFFF',foreground='#000000')

quantityLabel = Label(admin_off,text='QUANTITY',font=('Gill Sans',10),background='#FFFFFF',foreground='#8f8f8f')
totalLabel = Label(admin_off,text='TOTAL',font=('Gill Sans',10),background='#FFFFFF',foreground='#8f8f8f')

price1 = StringVar()
price1_value = IntVar()
price1_value.set(random.randint(19,119))
price1.set(f'${price1_value.get()}')
price1Label = Label(product1Frame,textvariable=price1,font=('Gill Sans',15),background='#FFFFFF',foreground='#000000',width=4)

price2 = StringVar()
price2_value = IntVar()
price2_value.set(random.randint(19,119))
price2.set(f'${price1_value.get()}')
price2Label = Label(product2Frame,textvariable=price2,font=('Gill Sans',15),background='#FFFFFF',foreground='#000000',width=4)

discountLabel = Label(admin_off,text='COUPON',font=('Gill Sans',15),background='#FFFFFF',foreground='#8f8f8f')

out_of1Text = StringVar()
out_of1Label=Label(product1Frame,textvariable=out_of1Text,font=('Gill Sans',15),background='#FFFFFF',foreground='#fc0000')

out_of2Text = StringVar()
out_of1Label=Label(product2Frame,textvariable=out_of2Text,font=('Gill Sans',15),background='#FFFFFF',foreground='#fc0000')

subtotalLabel = Label(admin_off,text='SUBTOTAL',font=('Gill Sans',15),background='#FFFFFF',foreground='#000000')

subtotalPrice = StringVar()
subtotalPrice.set(f'${(int(price1.get().replace('$',''))) + (int(price2.get().replace('$','')))}')
subtotalPriceLabel=Label(admin_off,textvariable=subtotalPrice,font=('Gill Sans',15),background='#FFFFFF',foreground='#000000')

#errors with coupons - still Labels
already_appliedLabel = Label(admin_off,text='You already entered this code!',font=('Gill Sans',10),background='#FFFFFF',foreground='#ff0000')
bad_couponLabel = Label(admin_off,text="This code doesn't exist.",font=('Gill Sans',10),background='#FFFFFF',foreground='#ff0000')

current_coupon = StringVar()
current_couponLabel = Label(admin_off,textvariable=current_coupon,font=('Gill Sans',10),background='#FFFFFF',foreground='#0d8500')

new_subtotal=StringVar()
new_subtotalLabel = Label(admin_off,textvariable=new_subtotal,bg='#FFFFFF',font=('Gill Sans',15),fg='#0d8500')


#GRIDDING
admin_off.grid()

atibaStoreButton.grid(column=1,row=1)
cartLabel.grid(column=2,row=2)
quantityLabel.grid(column=3,row=3,sticky=W)
totalLabel.grid(column=4,row=3)

product1Frame.grid(row=4,column=1,columnspan=4,sticky=W,padx=5,pady=5)
product2Frame.grid(row=5,column=1,columnspan=4,sticky=W,padx=5)

#products
#...
suitcaseLabel.grid(column=1,row=1,columnspan=2,sticky=W)
prod1spin.grid(column=3,row=1)
whitespace1.grid(column=2,row=1,padx=125)
whitespace2.grid(column=4,row=1,padx=35)
price1Label.grid(column=5,row=1,padx=10,ipadx=5)

tableLabel.grid(column=1,row=1,columnspan=2,sticky=W)
prod2spin.grid(column=3,row=1)
whitespace3.grid(column=2,row=1,padx=100)
whitespace4.grid(column=4,row=1,padx=40)
price2Label.grid(column=5,row=1,padx=10,ipadx=5)
#'''

discountLabel.grid(row=6,column=3)
codeEntry.grid(row=7,column=3,sticky=E,ipady=3)
applyButton.grid(row=7,column=4,sticky=W)

adminScale.grid(row=7,column=1,sticky=W)

subtotalLabel.grid(column=3,row=9)
subtotalPriceLabel.grid(column=4,row=9,ipadx=5)

already_appliedLabel.grid(column=3,row=8,sticky=EW,columnspan=2)
already_appliedLabel.grid_remove()

bad_couponLabel.grid(column=3,row=8,columnspan=2,sticky=EW)
bad_couponLabel.grid_remove()

current_couponLabel.grid(column=3,row=8,columnspan=2,sticky=EW)
current_couponLabel.grid_remove()

new_subtotalLabel.grid(column=4,row=10)
new_subtotalLabel.grid_remove()

root.mainloop()
