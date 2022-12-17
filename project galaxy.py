# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import * 
from tkinter import ttk
import math,random,os
from tkinter import messagebox

class GalaxyShop:
    def __init__(self,window):
        self.window = window
        self.window.geometry ("1350x700+0+0")
        self.window.title ("Galaxy  Computer Accessories Hub")
        global bg_color
        bg_color="#074663"
        title=Label(self.window,text="Galaxy  Computer Accessories Hub",bd=12,relief="groove",bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill="x")
              
            
        
class Customer(GalaxyShop):
    def __init__(self,window):
        self.window=window
        #==========================================Customer============================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill_text = StringVar()
        x=random.randint(1000,9999)
        self.c_bill_text.set(str(x))
        
        self.bill_btn = StringVar()
        
        #========================Customer Detail Frame====================
        F1=LabelFrame(self.window,bd=10,text="Customer Details",relief="groove",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        self.cname_text=Entry(F1,width=15,font="arial 15",textvariable=self.c_name,bd=7,relief="sunken").grid(row=0,column=1,padx=10,pady=5)
        
   
        cphone_label=Label(F1,text="Phone No.",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        self.cphone_text=Entry(F1,width=15,font="arial 15",textvariable=self.c_phone,bd=7,relief="sunken").grid(row=0,column=3,padx=10,pady=5)
        
        cbill_label=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        self.cbill_text=Entry(F1,width=15,font="arial 15",textvariable=self.c_bill_text,bd=7,relief="sunken").grid(row=0,column=5,padx=10,pady=5)
        
        bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=5,padx=10)
        
class Products:
    def __init__(self,window):
        self.window=window
        self.price = Prices(window)
        
        #=====================Products Frame==================
        F2=LabelFrame(self.window,bd=10,text="Products",relief="groove",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)

        laptop_label=Label(F2,text="Laptops",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=2,padx=10,pady=10,sticky="w")
        def comboclick1(event):
            selected_laptop= Label(F2,text=laptop_menu.get(),bg=bg_color,fg="white",font=("times new roman",16,"bold")).grid(row=2,column=6,pady=10,padx=5)
            
            if laptop_menu.get() == "Dell":
                self.price.l_price_text.set(24000)
            if laptop_menu.get() == "Apple":
                self.price.l_price_text.set(44000)
            if laptop_menu.get() == "Acer":
                self.price.l_price_text.set(18000)
            if laptop_menu.get() == "Lenovo":
                self.price.l_price_text.set(25000)
        
        options1 = ["Dell" , "Apple" , "Acer" , "Lenovo"]
        
        laptop_menu = ttk.Combobox(F2,value=options1)
        laptop_menu.grid(row=0,column=6,pady=10,padx=5)
        laptop_menu.set("Select")
        laptop_menu.bind("<<ComboboxSelected>>", comboclick1)
            
                
        tablet_label=Label(F2,text="Tablets",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=2,padx=10,pady=10,sticky="w")
        def comboclick2(event):
            selected_tablet= Label(F2,text=tablet_menu.get(),bg=bg_color,fg="white",font=("times new roman",16,"bold")).grid(row=6,column=6,pady=10,padx=5)
            if tablet_menu.get() == "QTab":
                self.price.t_price_text.set(4000)
            if tablet_menu.get() == "Apple":
                self.price.t_price_text.set(40000)
            if tablet_menu.get() == "Dany":
                self.price.t_price_text.set(8000)

        
        options2 = ["QTab" , "Apple" , "Dany" ]
        
        
        tablet_menu = ttk.Combobox(F2,value=options2)
        tablet_menu.grid(row=4,column=6,pady=10,padx=5)
        tablet_menu.set("Select")
        tablet_menu.bind("<<ComboboxSelected>>", comboclick2)
        
        
        headphone_label=Label(F2,text="Headphones",bg=bg_color,fg="lightgreen",font=("times new roman",16,"bold")).grid(row=8,column=2,padx=10,pady=10,sticky="w")
        def comboclick3(event):
            selected_headphone= Label(F2,text=headphone_menu.get(),bg=bg_color,fg="white",font=("times new roman",16,"bold")).grid(row=10,column=6,pady=10,padx=5)
                  
        options3 = ["Xpod" , "Apple" , "Audionic" ]
        
        headphone_menu = ttk.Combobox(F2,value=options3)
        headphone_menu.grid(row=8,column=6,pady=10,padx=5)
        headphone_menu.set("Select")
        headphone_menu.bind("<<ComboboxSelected>>", comboclick3)
        
        if headphone_menu.get() == "Xpod":
            self.price.h_price_text.set(4000)
        if headphone_menu.get() == "Audionic":
            self.price.h_price_text.set(10000)
        if headphone_menu.get() == "Apple":
            self.price.h_price_text.set(15000) 

class Quantity:
    def __init__(self,window):
        self.window = window
        #========================quantity Frame==================
        F3=LabelFrame(self.window,bd=10,text="Quantity",relief="groove",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)
        
        #==========================================quantity variables============================
        self.l_quantity_text = IntVar()
        self.t_quantity_text = IntVar()
        self.h_quantity_text = IntVar()

        lprice_label=Label(F3,text="No. of Laptop",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        self.lquantity_text=Entry(F3,width=6,font="arial 15",textvariable=self.l_quantity_text,bd=7,relief="sunken").grid(row=0,column=1,padx=10,pady=5)
        
        
        tquantity_label=Label(F3,text="No. of Tablet",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        self.tquantity_text=Entry(F3,width=6,font="arial 15",textvariable=self.t_quantity_text,bd=7,relief="sunken").grid(row=1,column=1,padx=10,pady=5)
        
        
        hquantity_label=Label(F3,text="No. of Headphones",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        self.hquantity_text=Entry(F3,width=6,font="arial 15",textvariable=self.h_quantity_text,bd=7,relief="sunken").grid(row=2,column=1,padx=1,pady=5)
        
        
class Prices:
    def __init__(self,window):
        self.window = window
        #===========Prices Variables======================================
        self.l_price_text = IntVar()
        self.t_price_text = IntVar()
        self.h_price_text = IntVar()

    
        #=====================Prices Frame=========================
        F4=LabelFrame(self.window,bd=10,text="Prices",relief="groove",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)  
 
        l_price__label=Label(F4,text="Laptop Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        self.lprice_text=Entry(F4,width=7,textvariable=self.l_price_text,font="arial 15",bd=7,relief="sunken").grid(row=0,column=1,padx=10,pady=5)

        
        t_price_label=Label(F4,text="Tablet Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=5)
        self.tprice_text=Entry(F4,width=7,textvariable=self.t_price_text,font="arial 15",bd=7,relief="sunken").grid(row=1,column=1,padx=10,pady=5)

        h_price_label=Label(F4,text="Headphone Price",bg=bg_color,fg="lightgreen",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=5)
        self.hprice_text=Entry(F4,textvariable=self.h_price_text,width=7,font="arial 15",bd=7,relief="sunken").grid(row=2,column=1,padx=10,pady=5)
       
        
class BillArea:
    def __init__(self,window):
        self.window=window
        self.Asad = Customer(window)
        self.price = Prices(window)
        self.quantity = Quantity(window)
        #======================Total Product Prices and Tax Variables==================
        self.m1_txt_var = StringVar()
        self.m2_txt_var = StringVar()
        self.m3_txt_var = StringVar()
        
        self.c1_txt_var = StringVar()
        self.c2_txt_var = StringVar()
        self.c3_txt_var = StringVar()
       
        #=======================================Bill Area===============================
        F5=Frame(self.window,bd=10,relief="groove")
        F5.place(x="1010",y="180",width="350",height="380")
        bill_title=Label(F5,text="Bill Area",font=("arial",15,"bold"),bd="7",relief="groove").pack(fill="x")
        scroll_y=Scrollbar(F5,orient="vertical")
        self.txtarea=Text(F5,yscrollcommand="scroll_y.set")
        scroll_y.pack(side="right",fill="y")
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill="both",expand=1)
                
        F6=LabelFrame(self.window,bd=10,relief="groove", text="Bill Menu",font=("timesnew roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
		
        m1_lbl=Label(F6,text="Total Laptop price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,stick="w")
        m1_txt=Entry(F6,width=18,font=("arial 10 bold"),textvariable=self.m1_txt_var,bd=7,relief="sunken").grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Tablet price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,stick="w")
        m2_txt=Entry(F6,width=18,font=("arial 10 bold"),textvariable=self.m2_txt_var,bd=7,relief="sunken").grid(row=1,column=1,padx=10,pady=1)
				
        m3_lbl=Label(F6,text="Total Headphone price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,stick="w")
        m3_txt=Entry(F6,width=18,font=("arial 10 bold"),textvariable=self.m3_txt_var,bd=7,relief="sunken").grid(row=2,column=1,padx=10,pady=1)
				
        c1_lbl=Label(F6,text="Laptop tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,stick="w")
        c1_txt=Entry(F6,width=18,font=("arial 10 bold"),textvariable=self.c1_txt_var,bd=7,relief="sunken").grid(row=0,column=3,padx=10,pady=1)
				
        c2_lbl=Label(F6,text="Tablet Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,stick="w")
        c2_txt=Entry(F6,width=18,font=("arial 10 bold"),textvariable=self.c2_txt_var,bd=7,relief="sunken").grid(row=1,column=3,padx=10,pady=1)
				
        c3_lbl=Label(F6,text="Headphone Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,stick="w")
        c3_txt=Entry(F6,width=18,font=("arial 10 bold"),textvariable=self.c3_txt_var,bd=7,relief="sunken").grid(row=2,column=3,padx=10,pady=1)
	
        
        btn_F=Frame(F6,bd=7,relief="groove")
        btn_F.place(x=750,width=580,height=105)
				
        total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
				
        generate_bill_btn=Button(btn_F,text="Generat Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
				
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
				
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)

        
    def total(self):
        self.total_laptop_price=float(self.price.l_price_text.get()*self.quantity.l_quantity_text.get())
        self.m1_txt_var.set("Rs. "+str(self.total_laptop_price))
        self.l_tax=round((self.total_laptop_price*0.05),2)
        self.c1_txt_var.set("Rs. "+str(self.l_tax))
        
        
        self.total_tablet_price=float(self.price.t_price_text.get()*self.quantity.t_quantity_text.get())
        self.m2_txt_var.set("Rs. "+str(self.total_tablet_price))
        self.t_tax=round((self.total_tablet_price*0.1),2)
        self.c2_txt_var.set("Rs. "+str(self.t_tax))
                            
        
        self.total_headphone_price=float(self.price.h_price_text.get()*self.quantity.h_quantity_text.get())
        self.m3_txt_var.set("Rs. "+str(self.total_headphone_price))
        self.h_tax=round((self.total_headphone_price*0.05),2)
        self.c3_txt_var.set("Rs. "+str(self.h_tax))
    
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to Galaxy Shop")
        self.txtarea.insert(END,f"\n Bill no :  {self.Asad.c_bill_text.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.Asad.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.Asad.c_phone.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")
    
    def bill_area(self):
        if self.Asad.c_name.get() == "" or self.Asad.c_phone.get() == "":
            messagebox.showerror("Error","Customer details are required")
        elif self.m1_txt_var.get() == "Rs. 0.0" and self.m2_txt_var.get() == "Rs. 0.0" and self.m3_txt_var.get() == "Rs. 0.0":
            messagebox.showerror("Error","No product selected")
        else:
            self.welcome_bill()
            self.Total_bill=float(
                              self.total_laptop_price+
                              self.total_tablet_price+
                              self.total_headphone_price+
                              self.l_tax+
                              self.t_tax+
                              self.h_tax
                              )
            #=====================Laptops=========================
            if self.quantity.l_quantity_text.get() != 0:
                self.txtarea.insert(END,f"\n Laptop\t\t{self.quantity.l_quantity_text.get()}\t\t{self.total_laptop_price}")
            
            #=====================Tablets==========================
            if self.quantity.t_quantity_text.get() != 0:
                self.txtarea.insert(END,f"\n Tablet\t\t{self.quantity.t_quantity_text.get()}\t\t{self.total_tablet_price}")
            
            #=====================Headphones=======================
            if self.quantity.h_quantity_text.get() != 0:
                self.txtarea.insert(END,f"\n Headphone\t\t{self.quantity.h_quantity_text.get()}\t\t{self.total_headphone_price}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            
            if self.c1_txt_var != "0.0":
                self.txtarea.insert(END,f"\n Laptop Tax\t\t\t\t{self.l_tax}")
            self.txtarea.insert(END,f"\n--------------------------------------")
    
            if self.c2_txt_var != "0.0":
                self.txtarea.insert(END,f"\n Tablet Tax\t\t\t\t{self.t_tax}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            
            if self.c3_txt_var != "0.0":
                self.txtarea.insert(END,f"\n Headphone Tax\t\t\t\t{self.h_tax}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            
            self.txtarea.insert(END,f"\n Total Prices\t\t\t Rs.{str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            
            self.save_bill()
            
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        try:
            if op>0:
                self.bill_data=self.txtarea.get('1.0',END)
                f1=open("Bills/"+str(self.Asad.c_bill_text.get())+".txt","w")
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill no : {self.Asad.c_bill_text.get()} saved succesfully")
            else:
                return
        except FileNotFoundError:
            print("Check spelling! Because no such file found")
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you really want to clear?")
        if op>0:
            #==========================================Customer============================
            self.Asad.c_name.set("")
            self.Asad.c_phone.set("")
            #==========================================quantity============================
            self.quantity.l_quantity_text.set(0)
            self.quantity.t_quantity_text.set(0)
            self.quantity.h_quantity_text.set(0)
            #====================================Prices Variables==========================
            self.price.l_price_text.set(0)
            self.price.t_price_text.set(0)
            self.price.h_price_text.set(0)
            #======================Total Product Prices and Tax Variables==================
            self.m1_txt_var.set("")
            self.m2_txt_var.set("")
            self.m3_txt_var.set("")
            
            self.c1_txt_var.set("")
            self.c2_txt_var.set("")
            self.c3_txt_var.set("")
            
            self.Asad.c_bill_text.set("")
            x=random.randint(1000,9999)
            self.Asad.c_bill_text.set(str(x))
            
            self.welcome_bill()
    
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.window.destroy()
        
    #These line of codes are optional"
            
    #def find_bill(self):
         #present="no"
         #for i in os.listdir("Bills/"):
            #if i.split('.')[0] == self.Asad.c_bill_text.get()
                #f1=open("Bills/ {i}","r")
                #self.txtarea.delete('1.0',END)
                #for d in f1:
                    #self.txtarea.insert(END,d)
                    #f1.close()
                    #present="yes"
            #if present="no":
                #messagebox.showerror("Error","Invalid Bill No.")

window = Tk()
galaxy = GalaxyShop(window)
Asad = Customer(window)
obj_products = Products(window)
quantity = Quantity(window)
price = Prices(window)
my_bill = BillArea(window)
window.mainloop()


