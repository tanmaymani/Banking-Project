# Gmail importing -------in the program--
import gmail
email='xxxxxxx@gmail.com' # mention your gmail id only 
app_pass='xxxxxxx'         # metion your app pass for same gmail account ---

def send_mail_for_openacn(to_mail,uacno,uname,upass,udate):
    
        con=gmail.GMail(email,app_pass)
        sub="Account opened with DBD Bank"

        body=f"""Dear {uname},
        Your account has been opened successfully with DBD Bank and details are:-
AC={uacno} 
Pass={upass}
Open date={udate}

    Kindly change your password when you login for the first time

    Thanks and Regards 
    DBD Bank
    Noida(U.P),India
    """

        msg=gmail.Message(to=to_mail,subject=sub,text=body)
        con.send(msg)

def send_otp(to_mail,uname,uotp):
    con=gmail.GMail(email,app_pass)
    sub="OTP for password recovery"

    body=f"""Dear {uname},
        Your OTP to get password ={uotp} 
   
    Kindly verify this otp to application.

    Thanks and Regards 
    DBD Bank
    Noida(U.P),India
    """
    msg=gmail.Message(to=to_mail,subject=sub,text=body)
    con.send(msg)
          










