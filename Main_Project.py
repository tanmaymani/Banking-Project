from tkinter import Tk,Label,Frame,Entry,Button,messagebox,filedialog         #label for title of project of class=label
import os,shutil
import time
from PIL import Image,ImageTk
from tkinter.ttk import Combobox # drop down--
import random
import project_tables
import sqlite3
import project_mails
from tkinter import Listbox
from tkinter.ttk import Scrollbar
from tkinter import ttk

 # function returns captcha----

def generate_captcha():    
    captcha=[]
    for i in range(3):
        c=chr(random.randint(65,91))
        captcha.append(c)
        n=random.randint(0,9)
        captcha.append(str(n))

    random.shuffle(captcha)
    captcha=' '.join(captcha) 
    return captcha

def refresh():
    captcha=generate_captcha()
    captcha_lbl.configure(text=captcha)


root=Tk() # object of root window
root.state("zoomed")  # maxm size of root window 
root.configure(bg="Powder Blue") #root window background colour---
root.title("DBD Bank")  #title of the root window
root.resizable(width=False,height=False) #no resizability

title_lbl=Label(root,text="Banking Automation",font=('Arial',45,"bold","underline"),bg="powder blue")
title_lbl.pack()

today_lbl=Label(root,text=time.strftime("%A,%d %B %Y"),bg='powder blue',font=('Arial',16,'bold'),fg='purple')
today_lbl.pack(pady=10)

Img=Image.open("images/logo.jpg").resize((310,150))
Img_bitmap=ImageTk.PhotoImage(Img,master=root)

logo_lbl=Label(root,image=Img_bitmap,fg='powder blue')     #image= arugment
logo_lbl.place(relx=0,rely=0)

Img2=Image.open("images/logo.jpg").resize((250,150))
Img2_bitmap=ImageTk.PhotoImage(Img2,master=root)

logo2_lbl=Label(root,image=Img2_bitmap)     #image= arugment
logo2_lbl.place(relx=.8,rely=0)

footer_lbl=Label(root,text="Developed By:xxxxxxxxxxxx",bg='powder blue',fg="black",font=('Arial',16
,'bold'))
footer_lbl.pack(side='bottom')

def main_screen():
    def forgot():
        frm.destroy()
        forgot_screen()

    def reset():
        acn_entry.delete(0,'end')
        pass_entry.delete(0,'end')
        user_combo.delete(0,'end')
        inputcap_entry.delete(0,'end')

    def login():
        uacn=acn_entry.get()
        upass=pass_entry.get()
        ucap=inputcap_entry.get()
        utype=user_combo.get()
        actual_cap=captcha_lbl.cget('text')
        actual_cap=actual_cap.replace(" ",'')
    

        
        if utype=="Admin":
            if uacn=='0' and upass=='admin':
                if ucap==actual_cap:
                    frm.destroy() # FREEING THE FRAME THE MEMORY ---TO REDIRECTING ON OTHER FRAME/WINDOW
                    admin_screen()
                    #messagebox.showinfo("LogIn",'Welcome')
                else:
                    messagebox.showerror("LogIn","Invalid Captcha")
            else:
                messagebox.showerror("LogIn","Invalid A/C/Pass/Type")
        elif utype=="User":
            if ucap==actual_cap:
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='select * from accounts where accounts_acno=? and accounts_pass=?'
                curobj.execute(query,(uacn,upass))

                tup=curobj.fetchone()
                conobj.close()

                if tup==None:
                    messagebox.showerror("User Login","Invalid account or password")
                                    
                else:
                    frm.destroy()
                    user_screen(uacn)
            else:
                 messagebox.showerror("Login","Invalid Captcha")

        else:              
                messagebox.showerror('LogIn','Kindly slect the valid user type')
    
    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.75)

    #user type and its selection with label------
    user_lbl=Label(frm,text='User Type',bg="pink",font=("Arial",15,"bold"))
    user_lbl.place(relx=.3,rely=.1)

    user_combo=Combobox(frm,values=['Admin','User',"---------------Select-------------"],font=("Arial",14),state="readonly")
    user_combo.current(2) # choosing default valaue--
    user_combo.place(relx=.40,rely=.1)

    # a/c no label& entry of it ----
    acn_lbl=Label(frm,text='A/C',bg="pink",font=("Arial",15,"bold"))
    acn_lbl.place(relx=.3,rely=.2)

    acn_entry=Entry(frm,font=("Arial",16,"bold"),bd=4,bg="powder blue")
    acn_entry.place(relx=.4,rely=.2)
    acn_entry.focus() #for cursor position---

    #pass label and entry-----
    pass_lbl=Label(frm,text='Pass',bg="pink",font=("Arial",15,"bold"))
    pass_lbl.place(relx=.3,rely=.3)

    pass_entry=Entry(frm,font=("Arial",16,"bold"),bd=4,show="#",bg="powder blue")
    pass_entry.place(relx=.4,rely=.3)
    #captcha------make it global
    global captcha_lbl
    captcha_lbl=Label(frm,text=generate_captcha(),font=('Arial',17,'bold'),bg='white')
    captcha_lbl.place(relx=.4,rely=.41)
    #refresh button after importing button
    refresh_btn=Button(frm,text="Refresh",bg="white",fg="Black",font=('Arial',14,"bold"),command=refresh)
    refresh_btn.place(relx=.52,rely=.4)

    inputcaptcha_lbl=Label(frm,text='Enter',bg="pink",font=("Arial",17,"bold"))
    inputcaptcha_lbl.place(relx=.3,rely=.5)

    inputcap_entry=Entry(frm,font=("Arial",16,"bold"),bd=4,bg="powder blue")
    inputcap_entry.place(relx=.4,rely=.5)

    cap_label=Label(frm,text='Captcha',font=('Arial',17,'bold'),bg='pink')
    cap_label.place(relx=.3,rely=.41)

    #buttons-------login, reset, forgot----------
    login_btn=Button(frm,command=login,text="Log In",font=('Arial',14,"bold"),bd=4)
    login_btn.place(relx=.4,rely=.6)

    reset_btn=Button(frm,command=reset,text="Reset",font=('Arial',14,"bold"),bd=4)
    reset_btn.place(relx=.53,rely=.6)

    forgot_btn=Button(frm,command=forgot,text="Forgot Password",font=('Arial',15,"bold"),bd=4)
    forgot_btn.place(relx=.42,rely=.7)

#new frame for ---new windows

def admin_screen():
    
    def open_acn():
        def open_acn_db():
            uname=name_entry.get()
            uemail=email_entry.get()
            umob=mobile_entry.get()
            ugender=gender_combo.get()
            ubal=0.0
            uopendate=time.strftime("%A,%d %B %Y")
            upass=generate_captcha().replace(" ","")

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()

            query='insert into accounts values(Null,?,?,?,?,?,?,?)'
            curobj.execute(query,(uname,upass,uemail,umob,ugender,uopendate,ubal))
            conobj.commit()
            conobj.close()

        
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()

            query="select max (accounts_acno) from accounts"
            curobj.execute(query)

            uacno=curobj.fetchone()[0]
            conobj.close()

            try:
                project_mails.send_mail_for_openacn(uemail,uacno,uname,upass,uopendate)
                msg=f'Account opened with AC{uacno} and mail sent to {uemail},Kindly check spam also'
                messagebox.showinfo('Open Account',msg)
            except Exception as msg:
                 messagebox.showerror("Open Account",msg)

        def reset():
            name_entry.delete(0,'end')
            email_entry.delete(0,'end')
            mobile_entry.delete(0,'end')
            gender_combo.current(2)
            name_entry.focus()


        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

        title_lbl=Label(ifrm,text='Open Acccount Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
        #title_lbl.place(relx=.0,rely=0)
        title_lbl.pack()

        name_lbl=Label(ifrm,text='Name',font=('Arial',15,'bold'),bd=4)
        name_lbl.place(relx=.1,rely=.1)
        name_entry=Entry(ifrm,font=("Arial",15),bd=4,bg='powder blue')
        name_entry.place(relx=.1,rely=.2)

        email_lbl=Label(ifrm,text='Email',font=('Arial',15,'bold'),bd=4)
        email_lbl.place(relx=.1,rely=.35)

        email_entry=Entry(ifrm,font=('Arial',15,'bold'),bd=4,bg='powder blue')
        email_entry.place(relx=.1,rely=.45)

        mobile_lbl=Label(ifrm,text='Mobile',font=('Arial',15,'bold'),bd=4)
        mobile_lbl.place(relx=.6,rely=.1)

        mobile_entry=Entry(ifrm,font=("Arial",15),bd=4,bg='powder blue')
        mobile_entry.place(relx=.6,rely=.2)

        gender_lbl=Label(ifrm,text='Gender',font=('Arial',14,'bold'),bd=4)
        gender_lbl.place(relx=.6,rely=.35)

        gender_combo=Combobox(ifrm,values=['Female','Male','Others'],font=("Arial",15),state="readonly")
        gender_combo.current(2) # choosing default valaue--
        gender_combo.place(relx=.585,rely=.45)

        open_btn=Button(ifrm,command=open_acn_db,text="Open A/C",font=('Arial',15,"bold"),bd=4)
        open_btn.place(relx=.3,rely=.63)

        reset_btn=Button(ifrm,command=reset,text="Reset",font=("Arial",15,'bold'),bd=4)
        reset_btn.place(relx=.53,rely=.63)

    
    def delete_acn():
        def send_otp():
            uacn=acn_entry.get()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            query='select * from accounts where accounts_acno=?'
            curobj.execute(query,(uacn,))

            tup=curobj.fetchone()
            conobj.close()
            if tup==None:
                messagebox.showerror("Delete Account","Record not found")
            else:
                otp=str(random.randint(1000,9999))
                project_mails.send_otp(tup[3],tup[1],otp)
                messagebox.showinfo("Delete Account",'OTP sent to the given/registered mail id ')

                otp_entry=Entry(ifrm,width=12,font=("Arial",15),bd=4)
                otp_entry.place(relx=.43,rely=.65)

                def verify():
                    uotp=otp_entry.get()
                    if otp==uotp:
                        resp=messagebox.askyesno("Delete Account",f"Do you really want to delete")
                        if not resp:
                            frm.destroy()
                            admin_screen()                    
                            return

                        conobj=sqlite3.connect(database='bank.sqlite')
                        curobj=conobj.cursor()
                        query='delete from accounts where accounts_acno=?'
                        curobj.execute(query,(uacn))
                        conobj.commit()
                        conobj.close()                                   
                        messagebox.showinfo("Delete Account","Account deleted" )
                        frm.destroy()
                        admin_screen()
                    else:
                            messagebox.showerror("Delete Account","Incorrect OTP")


                verify_btn=Button(ifrm,command=verify,text="Verify",bg="Powder Blue",font=("Arial",14),bd=4)
                verify_btn.place(relx=.47,rely=.8)


        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

        title_lbl=Label(ifrm,text='Delete Acccount Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
        title_lbl.place(relx=.0,rely=0)
        title_lbl.pack()

        acn_lbl=Label(ifrm,text='A/C',bg="white",font=("Arial",15,"bold"))
        acn_lbl.place(relx=.3,rely=.2)

        acn_entry=Entry(ifrm,font=("Arial",16,"bold"),bd=4,bg="powder blue")
        acn_entry.place(relx=.4,rely=.2)
        acn_entry.focus()

        otp_btn=Button(ifrm,command=send_otp,text="Send OTP",bg="Powder Blue",fon=("Arial",15),bd=4)
        otp_btn.place(relx=.45,rely=.4)

    def view_acn():
        def view_details():
            uacn=acn_entry.get()
            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            query='select * from accounts where accounts_acno=?'
            curobj.execute(query,(uacn,))

            tup=curobj.fetchone()
            conobj.close()
            if tup== None:
                messagebox.showerror("View Account","Record not found")
            else:
                details=f"""User Name={tup[1]}
Avail Bal = {tup[7]}
AC Open date ={tup[6]}
Email= {tup[3]}
Mob={tup[4]}
"""
                messagebox.showinfo("View Account",details)

        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='white')
        ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

        view_lbl=Label(ifrm,text='View Acccount Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
        view_lbl.place(relx=.0,rely=0)
        view_lbl.pack()

        
        acn_lbl=Label(ifrm,text='A/C',bg="white",font=("Arial",15,"bold"))
        acn_lbl.place(relx=.27,rely=.2)

        acn_entry=Entry(ifrm,font=("Arial",16,"bold"),bd=4,bg="powder blue")
        acn_entry.place(relx=.378,rely=.2)
        acn_entry.focus()

        view_btn=Button(ifrm,command=view_details,text='View',bg='powder blue',font=("Arial",15),bd=4)
        view_btn.place(relx=.5,rely=.5)


    def logout():
        resp=messagebox.askyesno("Logout","Do you want to logout?")
        if resp:
                frm.destroy()
                main_screen()

    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.75)

    #add label of Welcome message-----
    Wel_lbl=Label(frm,text='Welcome,Admin',bg="pink",font=("Arial",17,"bold"))
    Wel_lbl.place(relx=.0,rely=0)

    Logout_btn=Button(frm,command=logout,text="Log Out",bg="powder blue",font=('Arial',15,"bold"),bd=4)
    Logout_btn.place(relx=.92,rely=.0)

    open_btn=Button(frm,command=open_acn,text="Open A/C",bg="powder blue",font=('Arial',15,"bold"),bd=4)
    open_btn.place(relx=.25,rely=.0)

    delete_btn=Button(frm,command=delete_acn,text="Delete A/C",bg="powder blue",font=('Arial',15,"bold"),bd=4)
    delete_btn.place(relx=.46,rely=.0)

    view_btn=Button(frm,command=view_acn,text="View A/C",bg="powder blue",font=('Arial',15,"bold"),bd=4)
    view_btn.place(relx=.7,rely=.0)

def forgot_screen():
    def back(): # to return back on the main screen----
        frm.destroy()
        main_screen()

    def reset():
        acn_entry.delete(0,'end')
        email_entry.delete(0,'end')
        inputcap_entry.delete(0,'end')

    def send_otp():
        uacn=acn_entry.get()
        uemail=email_entry.get()
        ucaptcha=inputcap_entry.get()
        if ucaptcha!=forgot_captcha.replace(' ',''):
                messagebox.showerror('Forgot Password','Invalid captch')
                return # to stop function
        #authenticate the acn and email then # send otp---and generating entry for otp------
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        query='select * from accounts where accounts_acno=? and accounts_email=? '
        curobj.execute(query,(uacn,uemail))

        tup=curobj.fetchone()
        curobj.close()
        if tup==None:
             messagebox.showerror("Forgot Password","Record not found")
        else:
            otp=str(random.randint(1000,9999))
            project_mails.send_otp(uemail,tup[1],otp)
            messagebox.showinfo("Forgot Password",'OTP sent to the given/registered mail id ')

            otp_entry=Entry(frm,width=9,font=("Arial",15),bd=4)
            otp_entry.place(relx=.4,rely=.8)
            def verify():
                 uotp=otp_entry.get()
                 if otp==uotp:
                      messagebox.showinfo("Forgot Password",f"Your Pass={tup[2]}" )
                 else:
                      messagebox.showerror("Forgot Password","Incorrect OTP")


            verify_btn=Button(frm,command=verify,text="Verify",bg="Powder Blue",fon=("Arial",14),bd=4)
            verify_btn.place(relx=.52,rely=.8)


    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.75)
# back button----
    back_btn=Button(frm,text="Back",bg='powder blue',font=('Arial',15,'bold'),command=back)
    back_btn.place(relx=0,rely=0)
    #acn lbl and ac entry----to recover pass---
    acn_lbl=Label(frm,text='A/C',bg="pink",font=("Arial",15,"bold"))
    acn_lbl.place(relx=.3,rely=.2)

    acn_entry=Entry(frm,font=("Arial",16,"bold"),bd=4,bg="powder blue")
    acn_entry.place(relx=.4,rely=.2)
    acn_entry.focus()

    email_lbl=Label(frm,text='Email',bg="pink",font=("Arial",15,"bold"))
    email_lbl.place(relx=.3,rely=.4)

    email_entry=Entry(frm,font=("Arial",16,"bold"),bd=4,bg="powder blue")
    email_entry.place(relx=.4,rely=.4)

    global captcha_lbl
    forgot_captcha=generate_captcha()
    captcha_lbl=Label(frm,text=forgot_captcha,font=('Arial',17,'bold'),bg='white')
    captcha_lbl.place(relx=.4,rely=.5)
    
    refresh_btn=Button(frm,text="Refresh",bg="white",fg="Black",font=('Arial',14,"bold"),command=refresh)
    refresh_btn.place(relx=.52,rely=.5)

    inputcap_entry=Entry(frm,font=("Arial",15),bd=4)
    inputcap_entry.place(relx=.4,rely=.6)

    otp_btn=Button(frm,command=send_otp,text="Send OTP",bg="Powder Blue",fon=("Arial",15),bd=4)
    otp_btn.place(relx=.4,rely=.7)

    reset_btn=Button(frm,command=reset,text="Reset",bg="powder blue",font=("Arial",15),bd=4)
    reset_btn.place(relx=.52,rely=.7)

def user_screen(uacn=None):
    def logout():
        resp=messagebox.askyesno("Logout","Do you want to logout?")
        if resp:
            frm.destroy()
            main_screen()

    def update_btn_screen():
        def update_db():
            uname=name_entry.get()
            upass=pass_entry.get()
            uemail=email_entry.get()
            umob=mobile_entry.get()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()

            query='update accounts set accounts_name=?,accounts_pass=?,accounts_email=?,accounts_mob=? where accounts_acno=?'
            curobj.execute(query,(uname,upass,uemail,umob,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Details","Profile Updated")
            frm.destroy()
            user_screen(uacn)

        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg='powder blue')
        ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

        update_lbl=Label(ifrm,text='Update Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
        update_lbl.place(relx=.0,rely=0)
        update_lbl.pack()

        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select * from accounts where accounts_acno=?',(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        name_lbl=Label(ifrm,text='Name',font=('Arial',15,'bold'),bd=4)
        name_lbl.place(relx=.1,rely=.1)

        name_entry=Entry(ifrm,font=("Arial",15),bd=4,)
        name_entry.place(relx=.1,rely=.2)
        name_entry.insert(0,tup[1])
        name_entry.focus()

        email_lbl=Label(ifrm,text='Email',font=('Arial',15,'bold'),bd=4)
        email_lbl.place(relx=.1,rely=.35)

        email_entry=Entry(ifrm,font=('Arial',15,'bold'),bd=4)
        email_entry.place(relx=.1,rely=.45)
        email_entry.insert(0,tup[3])


        mobile_lbl=Label(ifrm,text='Mobile',font=('Arial',15,'bold'),bd=4)
        mobile_lbl.place(relx=.6,rely=.1)

        mobile_entry=Entry(ifrm,font=("Arial",15),bd=4)
        mobile_entry.place(relx=.6,rely=.2)
        mobile_entry.insert(0,tup[4])

        pass_lbl=Label(ifrm,text='Pass',font=('Arial',14,'bold'),bd=4)
        pass_lbl.place(relx=.6,rely=.35)

        pass_entry=Entry(ifrm,font=('Arial',15,'bold'),bd=4)
        pass_entry.place(relx=.585,rely=.45)
        pass_entry.insert(0,tup[2])


        update_btn=Button(ifrm,command=update_db,text="Update",font=('Arial',15,"bold"),bd=4)
        update_btn.place(relx=.42,rely=.63)

    def deposit_btn_screen():
            def deposit():

                uamt=float(amt_entry.get())
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='update accounts set accounts_bal=accounts_bal+? where accounts_acno=?'
                curobj.execute(query,(uamt,uacn))
                conobj.commit()
                conobj.close()

                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='select accounts_bal from accounts where accounts_acno=?'
                curobj.execute(query,(uacn,))
                ubal=curobj.fetchone()[0]
                conobj.close()


                t=str(time.time())
                utxnid='txn'+t[:t.index('.')]
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='insert into stmts values( ?,?,?,?,?,?)'
                curobj.execute(query,(uacn,uamt,'CR.',time.strftime("%d-%m-%Y %r"),ubal,utxnid))
                conobj.commit()
                conobj.close()

                messagebox.showinfo("Deposit",f"{uamt} Amount Deposited")
                frm.destroy()
                user_screen(uacn)



            ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
            ifrm.configure(bg='powder blue')
            ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

            deposit_lbl=Label(ifrm,text='  Deposit Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
            deposit_lbl.place(relx=0.3,rely=0)
            deposit_lbl.pack()

            amt_lbl=Label(ifrm,text='Amount',font=("Arial",15,'bold'))
            amt_lbl.place(relx=.3,rely=.2)

            amt_entry=Entry(ifrm,font=('Arial',15),bd=4)
            amt_entry.place(relx=.45,rely=.2)
            amt_entry.focus()

            dep_btn=Button(ifrm,command=deposit,text="Deposit",font=('Arial',15,'bold'))
            dep_btn.place(relx=.5,rely=.4)


    def withdraw_btn_screen():
            def withdraw():

                uamt=float(amt_entry.get())
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='select accounts_bal from accounts where accounts_acno=?'
                curobj.execute(query,(uacn,))
                ubal=curobj.fetchone()[0]
                conobj.close()

                if ubal>=uamt:


                    conobj=sqlite3.connect(database='bank.sqlite')
                    curobj=conobj.cursor()
                    query='update accounts set accounts_bal=accounts_bal-? where accounts_acno=?'
                    curobj.execute(query,(uamt,uacn))
                    conobj.commit()
                    conobj.close()



                    t=str(time.time())
                    utxnid='txn'+t[:t.index('.')]
                    conobj=sqlite3.connect(database='bank.sqlite')
                    curobj=conobj.cursor()
                    query='insert into stmts values( ?,?,?,?,?,?)'
                    curobj.execute(query,(uacn,uamt,'DB.',time.strftime("%d-%m-%Y %r"),ubal-uamt,utxnid))
                    conobj.commit()
                    conobj.close()

                    messagebox.showinfo("Withdrawn",f"{uamt} Amount withdrawn")
                    frm.destroy()
                    user_screen(uacn)

                else:
                     messagebox.showerror("Withdraw",f"Insufficent Bal{ubal}")
            ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
            ifrm.configure(bg='powder blue')
            ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

            withdraw_lbl=Label(ifrm,text=' Withdraw Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
            withdraw_lbl.place(relx=.0,rely=0)
            withdraw_lbl.pack()

            amt_lbl=Label(ifrm,text='Amount',font=("Arial",15,'bold'))
            amt_lbl.place(relx=.3,rely=.2)

            amt_entry=Entry(ifrm,font=('Arial',15),bd=4,bg="white")
            amt_entry.place(relx=.45,rely=.2)
            amt_entry.focus()

            wd_btn=Button(ifrm,command=withdraw,text="Withdraw",bg='White',font=('Arial',15,'bold'))
            wd_btn.place(relx=.5,rely=.4)



    def check_btn_screen():
            ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
            ifrm.configure(bg='powder blue')
            ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

            check_lbl=Label(ifrm,text='Account Details Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
            check_lbl.place(relx=.0,rely=0)
            check_lbl.pack()

            conobj=sqlite3.connect(database='bank.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select * from accounts where accounts_acno=?',(uacn,))
            tup=curobj.fetchone()
            conobj.close()


            details=f'''Account No. ={tup[0]}
            Opening date= {tup[6]}

            Available Bal= {tup[7]}

            Email ID= {tup[3]}

            Mob No. ={tup[4]}

'''
            details_lbl=Label(ifrm,text=details,fg='black',font=('Arial',15,'bold'),bg='powder blue')
            details_lbl.place(relx=.2,rely=.2)



    def history_btn_screen():
        ifrm = Frame(frm, highlightthickness=2, highlightbackground='black')
        ifrm.configure(bg='powder blue')
        ifrm.place(relx=.23, rely=.2, relwidth=.6, relheight=.65)

        history_lbl = Label(ifrm, text='Transaction History', bg="powder blue", font=("Arial", 17, "bold"), fg='purple')
        history_lbl.pack()

        listbox = Listbox(ifrm, font=('Arial',10,'bold'),bg='powder blue', width=88, height=30)
        listbox.pack(pady=10, padx=10)
        scrollbar = Scrollbar(ifrm, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        try:
            with sqlite3.connect('bank.sqlite') as conobj:
                curobj = conobj.cursor()
                curobj.execute('select * from stmts where stmts_acn=? order by stmts_date desc', (uacn,))
                transactions = curobj.fetchall()
            if not transactions:
                listbox.insert('end', "No transactions found.")
            else:
                for t in transactions:
                    listbox.insert('end', f"ID: {t[5]}, Amount: {t[1]}, Type: {t[2]}, Date: {t[3]}, Balance: {t[4]}")
        except sqlite3.Error as e:
            messagebox.showerror("History", f"Database error: {e}")

    def transfer_btn_screen():
            def transfer():
                toacn=to_entry.get()
                uamt=float(amt_entry.get())

                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='select *  from accounts where accounts_acno=?'
                curobj.execute(query,(toacn,))
                to_tup=curobj.fetchone()
                conobj.close()

                if to_tup==None:
                    messagebox.showerror("Transfer","To AC does not exists")
                    return
                
                conobj=sqlite3.connect(database='bank.sqlite')
                curobj=conobj.cursor()
                query='select accounts_bal from accounts where accounts_acno=?'
                curobj.execute(query,(uacn,))
                ubal=curobj.fetchone()[0]
                conobj.close()
                    
                if ubal>=uamt:
                    conobj=sqlite3.connect(database='bank.sqlite')
                    curobj=conobj.cursor()
                    query_deduct='update accounts set accounts_bal=accounts_bal-? where accounts_acno=?'
                    query_credit='update accounts set accounts_bal=accounts_bal+? where accounts_acno=?'
                    curobj.execute(query_deduct,(uamt,uacn))
                    curobj.execute(query_credit,(uamt,toacn))

                    conobj.commit()
                    conobj.close()



                    t=str(time.time())
                    utxnid1='txn_db'+t[:t.index('.')]
                    utxnid2='txn_cr'+t[:t.index('.')]
                    conobj=sqlite3.connect(database='bank.sqlite')
                    curobj=conobj.cursor()
                    query1='insert into stmts values( ?,?,?,?,?,?)'
                    query2='insert into stmts values( ?,?,?,?,?,?)'

                    curobj.execute(query1,(uacn,uamt,'DB.',time.strftime("%d-%m-%Y %r"),ubal-uamt,utxnid1))
                    time.sleep(1)
                    curobj.execute(query2,(toacn,uamt,'CR.',time.strftime("%d-%m-%Y %r"),ubal+uamt,utxnid2))
                    conobj.commit()
                    conobj.close()

                    messagebox.showinfo("Transfer",f"{uamt} Amount Transfered")
                    frm.destroy()
                    user_screen(uacn)

                else:
                     messagebox.showerror("Transfer",f"Insufficent Bal{ubal}")
                 
            ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
            ifrm.configure(bg='powder blue')
            ifrm.place(relx=.23,rely=.2,relwidth=.6,relheight=.65)

            transfer_lbl=Label(ifrm,text=' Transfer Screen',bg="powder blue",font=("Arial",17,"bold"),fg='purple')
            transfer_lbl.place(relx=.0,rely=0)
            transfer_lbl.pack()

            
            to_lbl=Label(ifrm,text='To AC',font=("Arial",15,'bold'))
            to_lbl.place(relx=.3,rely=.25)

            to_entry=Entry(ifrm,font=('Arial',15),bd=4)
            to_entry.place(relx=.45,rely=.25)
            to_entry.focus()

            amt_lbl=Label(ifrm,text='Amount',font=("Arial",15,'bold'))
            amt_lbl.place(relx=.3,rely=.4)

            amt_entry=Entry(ifrm,font=('Arial',15),bd=4)
            amt_entry.place(relx=.45,rely=.4)
          
            tr_btn=Button(ifrm,command=transfer,text="Transfer",font=('Arial',15,"bold"))
            tr_btn.place(relx=.5,rely=.54)
           
    def getdetails():
        conobj=sqlite3.connect(database='bank.sqlite')
        curobj=conobj.cursor()
        query='select * from accounts where accounts_acno=?'
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        return tup
    
    def update_picture():
        path=filedialog.askopenfilename()
        shutil.copy(path,f"images/{uacn}.png")

        profile_img=Image.open(f"images/{uacn}.png").resize((130,140))
        bitmap_profile_img=ImageTk.PhotoImage(profile_img,master=root)
        profile_img_lbl.image=bitmap_profile_img
        profile_img_lbl.configure(image=bitmap_profile_img)


    frm=Frame(root)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.2,relwidth=1,relheight=.75)

    #add label of Welcome message-----
    Wel_lbl=Label(frm,text=f'Welcome,{getdetails()[1]}',bg="pink",font=("Arial",15,"bold"))
    Wel_lbl.place(relx=.0,rely=0)

    Logout_btn=Button(frm,command=logout,text="Log Out",bg="powder blue",font=('Arial',15,"bold"),bd=4)
    Logout_btn.place(relx=.92,rely=.0)
    
    if os.path.exists(f"images/{uacn}.png"):
        path=f"images/{uacn}.png"
    else:
        path=f"images/default.png"

    profile_img=Image.open(path).resize((130,140))
    bitmap_profile_img=ImageTk.PhotoImage(profile_img,master=root)
    profile_img_lbl=Label(frm,image=bitmap_profile_img)
    profile_img_lbl.image=bitmap_profile_img
    profile_img_lbl.place(relx=0.0,rely=.052)

    update_pic_btn=Button(frm,command=update_picture,width=12,text='Update Picture',bg='powder blue',font=('Arial',13,'bold'))
    update_pic_btn.place(relx=.0,rely=.34)

    check_btn=Button(frm,command=check_btn_screen,width=12,text='Check Details',bg='powder blue',font=('Arial',13,'bold'))
    check_btn.place(relx=.0,rely=.44)

    deposit_btn=Button(frm,command=deposit_btn_screen,text="Deposit",width=12,font=('Arial',13,'bold'),bg='green')
    deposit_btn.place(relx=0,rely=.54)

    withdraw_btn=Button(frm,command=withdraw_btn_screen,text="Withdraw",width=12,bg='red',font=('Arial',13,'bold'))
    withdraw_btn.place(relx=0,rely=.64)

    update_btn=Button(frm,command=update_btn_screen,text="Update",width=12,font=('Arial',13,'bold'))
    update_btn.place(relx=0,rely=.74)

    transfer_btn=Button(frm,command=transfer_btn_screen,text="Transfer",width=12,bg='red',font=('Arial',13,'bold'))
    transfer_btn.place(relx=0,rely=.84)

    history_btn=Button(frm,command=history_btn_screen,text="TXN History",width=12,font=('Arial',13,'bold'))
    history_btn.place(relx=0,rely=.94)


main_screen()
root.mainloop()    # root window will be visible--
