from tkinter import * # type: ignore
from tkinter import messagebox
import random

root = Tk()

admin_off=Frame(root,bg="#FFFFFF")


admin_on=Frame(root,bg="#FFFFFF")


#functions
def admin_mode_toggle(ignore):
    global valid_coupons,coupon_listbox,coupon_list,new_code,no_number,current_image,current_image2,price_config_1,price_config_2
    if admin.get() == 1:
        #frames
        product1_configFrame = LabelFrame(admin_on,text='Product 1',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))
        product2_configFrame = LabelFrame(admin_on,text='Product 2',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))


        #spinbox
        price_config_1 = IntVar()
        price_config_1.set(price1_value.get())
        price_config_1Label = Spinbox(product1_configFrame, width=3, textvariable=price_config_1, from_=1, to=120,background='#FFFFFF',highlightbackground='#FFFFFF',foreground='#000000',command=change_price1)

        price_config_2 = IntVar()
        price_config_2.set(price2_value.get())
        price_config_2Label = Spinbox(product2_configFrame, width=3, textvariable=price_config_2, from_=1, to=120,background='#FFFFFF',highlightbackground='#FFFFFF',foreground='#000000',command=change_price2)

        #label
        no_number = Label(admin_on,text='You must include a number,\nthis will be your coupon value.\nNumbers will be read left to right and\ncan be anything above 0, and under 100.',font=('Gill Sans',10),background='#FFFFFF',foreground='#ff0000')

      
        #list
        coupon_list = StringVar()
        coupon_list.set(valid_coupons) # type: ignore
        coupon_listbox = Listbox( admin_on, listvariable=coupon_list,selectmode=SINGLE, font=('Gill Sans',15),bg='#FFFFFF',fg='#000000')
        
        #option menu
        images = [
            'Wallet','Speaker','Yoga Mat','Remote','Blender'
        ]

        current_image = StringVar()
        current_image.set(images[image_choice1-1])
        current_imageOptionMenu=OptionMenu(product1_configFrame,current_image,*images,command=set_image)
        current_imageOptionMenu.config(width=5,bd=0,bg='#FFFFFF',fg='#000000',activeforeground='#000000')



        current_image2 = StringVar()
        current_image2.set(images[image_choice2-1])
        current_imageOptionMenu2=OptionMenu(product2_configFrame,current_image2,*images,command=set_image2)
        current_imageOptionMenu2.config(width=5,bd=0,bg='#FFFFFF',fg='#000000',activeforeground='#000000')
        #buttons
        delete_allButton = Button(admin_on,text='Delete All',font=('Gill Sans',10),bg="#FFFFFF",command=delete_all_coupons,bd=0,highlightthickness=0)
        delete_singleButton = Button(admin_on,text='Delete Single',font=('Gill Sans',10),bg="#FFFFFF",command=delete_single_coupon,bd=0,highlightthickness=0)
        
        add_button = Button(admin_on,text='Add',font=('Gill Sans',10),bg="#FFFFFF",command=add_coupon,bd=0,highlightthickness=0)
        
        
        #entry
        new_code = StringVar()
        new_codeEntry=Entry(admin_on,textvariable=new_code,width=10,fg='#000000',bg='#FFFFFF',bd=2)
        
        
        #gridding
        admin_off.grid_remove()
        admin_on.grid()
        adminScale2.grid(row=4,column=1)
        coupon_listbox.grid(row=1,column=2,columnspan=2,rowspan=2,sticky=EW)
        delete_allButton.grid(row=3,column=3,sticky=EW)
        delete_singleButton.grid(row=3,column=2,sticky=EW)
        new_codeEntry.grid(row=4,column=2,sticky=EW)
        add_button.grid(row=4,column=3,sticky=EW)

        product1_configFrame.grid(row=1,column=1,padx=10)
        current_imageOptionMenu.grid(row=1,column=1)

        product2_configFrame.grid(row=2,column=1,padx=20)
        current_imageOptionMenu2.grid(row=1,column=1)
        
        price_config_1Label.grid(row=2,column=1)
        price_config_2Label.grid(row=2,column=1)

    else:
        admin_on.grid_remove()
        admin_off.grid()











########################

def change_price1():

    price1_value.set(price_config_1.get())

    spin1.set(1)
    code.set('clear')
    coupon_apply()

    quantity_1()

def change_price2():

    price2_value.set(price_config_2.get())

    spin2.set(1)
    code.set('clear')
    coupon_apply()

    quantity_2()

def set_image(ignore):
    x = current_image.get()
    if x == 'Remote':
        remoteLabel1.grid()
        blenderLabel1.grid_remove()
        speakerLabel1.grid_remove()
        walletLabel1.grid_remove()
        yogaLabel1.grid_remove()

        product1Frame.config(text='Remote')

    elif x == 'Wallet':
        remoteLabel1.grid_remove()
        blenderLabel1.grid_remove()
        speakerLabel1.grid_remove()
        walletLabel1.grid()
        yogaLabel1.grid_remove()

        product1Frame.config(text='Wallet')
    elif x == 'Blender':
        remoteLabel1.grid_remove()
        blenderLabel1.grid()
        speakerLabel1.grid_remove()
        walletLabel1.grid_remove()
        yogaLabel1.grid_remove()

        product1Frame.config(text='Blender')
    elif x == 'Speaker':
        remoteLabel1.grid_remove()
        blenderLabel1.grid_remove()
        speakerLabel1.grid()
        walletLabel1.grid_remove()
        yogaLabel1.grid_remove()

        product1Frame.config(text='Speaker')
    elif x == 'Yoga Mat':
        remoteLabel1.grid_remove()
        blenderLabel1.grid_remove()
        speakerLabel1.grid_remove()
        walletLabel1.grid_remove()
        yogaLabel1.grid()

        product1Frame.config(text='Yoga Mat')

    
def set_image2(ignore):
    y = current_image2.get()
    if y == 'Remote':
        remoteLabel2.grid()
        blenderLabel2.grid_remove()
        speakerLabel2.grid_remove()
        walletLabel2.grid_remove()
        yogaLabel2.grid_remove()

        product2Frame.config(text='Remote')

    elif y == 'Wallet':
        remoteLabel2.grid_remove()
        blenderLabel2.grid_remove()
        speakerLabel2.grid_remove()
        walletLabel2.grid()
        yogaLabel2.grid_remove()

        product2Frame.config(text='Wallet')
    elif y == 'Blender':
        remoteLabel2.grid_remove()
        blenderLabel2.grid()
        speakerLabel2.grid_remove()
        walletLabel2.grid_remove()
        yogaLabel2.grid_remove()

        product2Frame.config(text='Blender')
    elif y == 'Speaker':
        remoteLabel2.grid_remove()
        blenderLabel2.grid_remove()
        speakerLabel2.grid()
        walletLabel2.grid_remove()
        yogaLabel2.grid_remove()

        product2Frame.config(text='Speaker')
    elif y == 'Yoga Mat':
        remoteLabel2.grid_remove()
        blenderLabel2.grid_remove()
        speakerLabel2.grid_remove()
        walletLabel2.grid_remove()
        yogaLabel2.grid()

        product2Frame.config(text='Yoga Mat')

def add_coupon():
    global valid_coupons
    coupon = new_code.get()
    numbers = '123456789'
    proper = False

    for i in numbers:
      if i in coupon:
        proper = True
        break
    
    if proper == False:
        no_number.grid(row=5,column=2,columnspan=2)
    else:
        valid_coupons.append(coupon)
        coupon_list.set(valid_coupons) # type: ignore



def delete_all_coupons():
    global valid_coupons
    valid_coupons.clear()
    coupon_list.set(valid_coupons) # type: ignore

def delete_single_coupon():
    global valid_coupons
    to_delete = coupon_listbox.curselection()[0]

    if valid_coupons[to_delete] in current_coupon.get():   
        already_appliedLabel.grid_remove()
        bad_couponLabel.grid_remove()
        new_subtotalLabel.grid_remove()
        current_couponLabel.grid_remove()
        current_coupon.set('')
        subtotalPriceLabel.config(foreground='#000000')

    valid_coupons.pop(to_delete)
    coupon_list.set(valid_coupons) # type: ignore
    


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
    subtotalPrice.set(f'${(int(price1.get().replace('$',''))) + (int(price2.get().replace('$','')))}')
    
    value_of_coupon = ''
    for number in user_code:
        if number.isnumeric()==True:
            value_of_coupon+=number

    value_of_coupon = (100 - int(value_of_coupon)) / 100

    subtotalPrice_float = float(subtotalPrice.get().replace('$',''))
    
    new_subtotal.set(f'${round(subtotalPrice_float*value_of_coupon)}')
    new_subtotalLabel.grid()

def quantity_2():
    price = price2_value.get()
    quantity = spin2.get()
    price2.set(f'${price*quantity}')
    subtotalPrice.set(f'${(int(price1.get().replace('$',''))) + (int(price2.get().replace('$','')))}')
    
    value_of_coupon = ''
    for number in user_code:
        if number.isnumeric()==True:
            value_of_coupon+=number

    value_of_coupon = (100 - int(value_of_coupon)) / 100
    
    subtotalPrice_float = float(subtotalPrice.get().replace('$',''))
    
    new_subtotal.set(f'${round(subtotalPrice_float*value_of_coupon)}')
    new_subtotalLabel.grid()


def coupon_apply():
    global valid_coupons,already_applied,user_code

    #valid coupons is a list of coupons
    user_code = code.get()

    #users inputed coupon
    if user_code == ' ' or user_code == '' or user_code == 'Enter here':

        already_appliedLabel.grid_remove()
        bad_couponLabel.grid_remove()
        current_couponLabel.grid()
    
    elif user_code.lower() == 'clear':

        already_appliedLabel.grid_remove()
        bad_couponLabel.grid_remove()
        new_subtotalLabel.grid_remove()
        current_coupon.set('')
        already_applied = ''
        new_subtotal.set('')
        subtotalPriceLabel.config(foreground='#000000')


    elif user_code not in valid_coupons:

        already_applied = user_code
        already_appliedLabel.grid_remove()
        current_couponLabel.grid_remove()
        bad_couponLabel.grid()
        
            

    elif user_code == already_applied or user_code in current_coupon.get():

        already_applied = user_code
        bad_couponLabel.grid_remove()
        current_couponLabel.grid_remove()
        already_appliedLabel.grid()

    else:

        already_appliedLabel.grid_remove()
        already_applied = user_code
        bad_couponLabel.grid_remove()
        

        value_of_coupon = ''
            
        for number in user_code:
            if number.isnumeric()==True:
                value_of_coupon+=number

        value_of_coupon = (100 - int(value_of_coupon)) / 100
        
        subtotalPriceLabel.config(foreground='#ff0000')

        subtotalPrice_float = float(subtotalPrice.get().replace('$',''))
        
        new_subtotal.set(f'${round(subtotalPrice_float*value_of_coupon)}')
        new_subtotalLabel.grid()

        current_coupon.set(f'Coupon applied: {user_code}')
        current_couponLabel.grid()

#FRAMES
product1Frame=LabelFrame(admin_off,text='',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))
product2Frame=LabelFrame(admin_off,text='',background='#FFFFFF',foreground='#000000',font=('Gill Sans', 15))

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
admin.set(0)
adminScale = Scale(admin_off, from_=1, to=0, variable = admin, width = 20, length=50, orient=VERTICAL,bd=0,bg='#FFFFFF',fg='#000000',label='Admin Mode',font=('Gill Sans',10),highlightthickness=0,command=admin_mode_toggle)

adminScale2 = Scale(admin_on, from_=1, to=0, variable = admin, width = 20, length=50, orient=VERTICAL,bd=0,bg='#FFFFFF',fg='#000000',label='Admin Mode',font=('Gill Sans',10),highlightthickness=0,command=admin_mode_toggle)

#IMAGES
wallet = PhotoImage(file='images/wallet.png')
walletLabel1 = Label(product1Frame,image=wallet,bd=0,bg='#FFFFFF')
walletLabel2 = Label(product2Frame,image=wallet,bd=0,bg='#FFFFFF')

speaker = PhotoImage(file='images/speaker.png')
speakerLabel1 = Label(product1Frame,image=speaker,bd=0,bg='#FFFFFF')
speakerLabel2 = Label(product2Frame,image=speaker,bd=0,bg='#FFFFFF')

yoga = PhotoImage(file='images/yoga.png')
yogaLabel1 = Label(product1Frame,image=yoga,bd=0,bg='#FFFFFF')
yogaLabel2 = Label(product2Frame,image=yoga,bd=0,bg='#FFFFFF')

remote = PhotoImage(file='images/remote.png')
remoteLabel1 = Label(product1Frame,image=remote,bd=0,bg='#FFFFFF')
remoteLabel2 = Label(product2Frame,image=remote,bd=0,bg='#FFFFFF')

blender = PhotoImage(file='images/blender.png')
blenderLabel1 = Label(product1Frame,image=blender,bd=0,bg='#FFFFFF')
blenderLabel2 = Label(product2Frame,image=blender,bd=0,bg='#FFFFFF')

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
]


already_applied = ''

coupon_entered = ''

#LABELS
cartLabel = Label(admin_off,text='Your Cart',font=('Gill Sans',30),background='#FFFFFF',foreground='#000000')

quantityLabel = Label(admin_off,text='QUANTITY',font=('Gill Sans',10),background='#FFFFFF',foreground='#8f8f8f')
totalLabel = Label(admin_off,text='TOTAL',font=('Gill Sans',10),background='#FFFFFF',foreground='#8f8f8f')

price1 = StringVar()
price1_value = IntVar()
price1_value.set(random.randint(20,120))
price1.set(f'${price1_value.get()}')
price1Label = Label(product1Frame,textvariable=price1,font=('Gill Sans',15),background='#FFFFFF',foreground='#000000',width=4)

price2 = StringVar()
price2_value = IntVar()
price2_value.set(random.randint(20,120))
price2.set(f'${price2_value.get()}')
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
#images grid
walletLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
speakerLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
yogaLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
remoteLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
blenderLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
remoteLabel1.grid_remove()
blenderLabel1.grid_remove()
speakerLabel1.grid_remove()
walletLabel1.grid_remove()
yogaLabel1.grid_remove()

walletLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
speakerLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
yogaLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
remoteLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
blenderLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
remoteLabel2.grid_remove()
blenderLabel2.grid_remove()
speakerLabel2.grid_remove()
walletLabel2.grid_remove()
yogaLabel2.grid_remove()


image_choice1 = random.randint(1,5)

if image_choice1== 1:
    walletLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
    product1Frame.config(text='Wallet')
elif image_choice1 == 2:
    speakerLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
    product1Frame.config(text='Speaker')
elif image_choice1 == 3:
    yogaLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
    product1Frame.config(text='Yoga Mat')
elif image_choice1 == 4:
    remoteLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
    product1Frame.config(text='Remote')
elif image_choice1 == 5:
    blenderLabel1.grid(column=1,row=1,columnspan=2,sticky=W)
    product1Frame.config(text='Blender')

prod1spin.grid(column=3,row=1)
whitespace1.grid(column=2,row=1,padx=125)
whitespace2.grid(column=4,row=1,padx=35)
price1Label.grid(column=5,row=1,padx=10,ipadx=5)

while True:
    image_choice2 = random.randint(1,5)
    if image_choice2 != image_choice1: break

if image_choice2== 1:
    walletLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
    product2Frame.config(text='Wallet')
elif image_choice2 == 2:
    speakerLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
    product2Frame.config(text='Speaker')
elif image_choice2 == 3:
    yogaLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
    product2Frame.config(text='Yoga Mat')
elif image_choice2 == 4:
    remoteLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
    product2Frame.config(text='Remote')
elif image_choice2 == 5:
    blenderLabel2.grid(column=1,row=1,columnspan=2,sticky=W)
    product2Frame.config(text='Blender')

prod2spin.grid(column=3,row=1)
whitespace3.grid(column=2,row=1,padx=125)
whitespace4.grid(column=4,row=1,padx=35)
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

new_subtotalLabel.grid(column=4,row=10)
new_subtotalLabel.grid_remove()



root.mainloop()
