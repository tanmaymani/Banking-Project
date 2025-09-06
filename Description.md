🏦 Bank Automation Project (Python + Tkinter) A simple and interactive Bank Automation System with a GUI built using Python and Tkinter. It includes a user login system, secure password reset with OTP verification, and a clean interface for user interaction.

✅ Features 🔐 User Registration and Login System

Secure sign-up and login functionality Validates existing users from a stored record (file/database) 📧 Forgot Password with OTP Verification

Users can request an OTP to reset their password OTP verification ensures account security Password is displayed upon successful verification 🖥️ Simple GUI Interface

Built using Tkinter for a responsive desktop experience Easy navigation and clean layout 🧩 Code Structure 'main.py`: Main file containing the full application code.

The application is modularized using classes and functions:

login_screen: Manages user login and new registration forgot_screen: Interface for password recovery via OTP verify: Verifies OTP and displays the user's password 💻 Requirements Python 3.x Tkinter (usually comes pre-installed with Python) Sqlite3 You can install Python from python.org. 🚀 How to Run Clone or download this repository: git clonehttps://github.com/tanmaymani/Banking-Project cd bank-automation-tkinter Run the application:

bash Copy Edit python main.py 📝 Make sure any required files (user data or OTP files) are present in the same directory if the script expects them.

📌 Notes This is a standalone desktop application and does not require an internet connection unless email functionality is added.

OTP is currently assumed to be handled internally or via simulated logic. You can integrate real email or SMS services like SMTP or Twilio for production use.
