import os 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, StringVar # tkinter is used for gui
import sqlite3 # sqlite is used to store data

class loginPage:
    def __init__(self) -> None:
        # build ui
        self.login = tk.Tk()
        self.login.configure(background="#cce4c9", height=500, width=700)
        self.login.resizable(False, False)
        self.login.title("Log In")


        self.frame_logIn = ttk.Frame(self.login)
        self.frame_logIn.configure(height=200, width=200)
        self.title_logIn = ttk.Label(self.frame_logIn)
        self.title_logIn.configure(anchor="center",
                                   font="{Cambria} 36 {bold italic}",
                                   justify="center",
                                   text='LOGIN')
        self.title_logIn.grid(column=0,
                              padx=200,
                              pady="40 20",
                              row=0,
                              sticky="n")
        
        self.username_entry = StringVar(value = "Username")
        self.username = ttk.Entry(self.frame_logIn, textvariable = self.username_entry)
        self.username.configure(font="{aria} 12 {bold}", width=25)
        self.username.delete("0", "end")
        self.username.insert("0", 'Username')
        self.username.grid(column=0, row=1)
        self.username.bind("<Button-1>", self.userName_onClick)

    
        self.password_entry = StringVar(value = "Password")
        self.password = ttk.Entry(self.frame_logIn, textvariable = self.password_entry)
        self.password.configure(font="{aria} 12 {bold}", width=25)
        self.password.delete("0", "end")
        self.password.insert("0", 'Password')
        self.password.grid(column=0, row=2)
        self.password.bind("<Button-1>", self.password_onClick)

        self.frame_logInButton = ttk.Frame(self.frame_logIn)
        self.frame_logInButton.configure(height=200, width=200)

        self.signin_button = ttk.Button(self.frame_logInButton, command = self.check_login)
        self.signin_button.configure(text='Sign In', width=33)
        self.signin_button.pack(side="top")

        self.register_button = ttk.Button(self.frame_logInButton, command = self.registerUser)
        self.register_button.configure(text='Register', width=33)
        self.register_button.pack(side="top")

        self.frame_logInButton.grid(column=0, pady=30, row=3, sticky="s")
        self.frame_logIn.grid(column=0, row=0, sticky="n")

        # establish sqlite database connection
        relative_path = "db"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, relative_path, "restaurantSystem.db")
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

        # create log in table and insert initial data
        self.create_logInTable()

        # Main widget
        self.login_window = self.login
        self.login_window.protocol("WM_DELETE_WINDOW", self.break_login)
        self.login_window.bind('<Return>', self.check_login)

    def break_login (self) -> None:
        if messagebox.askokcancel("Exiting Login", "The login window will be closed") == True:
            self.login_window.destroy() # close the window
            exit(0) 

    def create_logInTable (self) -> None:
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS users (
                    username   TEXT PRIMARY KEY,
                    password   TEXT NOT NULL
                );
            """
        )
        self.conn.commit()
        self.cur.execute(
            """
                SELECT * FROM users
            """
        )
        queryResult = self.cur.fetchall()
        if len(queryResult) > 0:
            return
        else:
            self.cur.execute(
            """
                INSERT INTO users VALUES
                ('ADMIN', 'abc123'),
                ('USER', '0123456');
            """
        )
        self.conn.commit()
        
    def check_login (self, event) -> None:
        name = self.username_entry.get()
        password = self.password_entry.get()
        self.cur.execute(
            """
                SELECT * FROM users 
                WHERE username = ? and
                      password = ?
            """, (name, password)
        )
        queryResult = self.cur.fetchall()
        if len(queryResult) > 0:
            messagebox.showinfo("Log In Success", "Log in sucessful!")
            self.login_window.quit()
        else:
            messagebox.showerror("Error", "The username or password is incorrect")

    def get_user_info (self) -> str:
        username = self.username_entry.get()
        return username

    def registerUser (self) -> None: # register interface
        self.title_logIn.config(text="Register")
        self.username_entry.set("Enter your username")
        self.password_entry.set("Create a password")
        self.signin_button.config(text = "Confirm", command = self.insert_newUser)
        self.register_button.config(text = "Back", command = self.revert_to_logIn)
        self.password.config(show = "")
        self.login_window.focus()
        self.login_window.bind("<Return>", self.insert_newUser)
        self.login_window.title("Register")

    def insert_newUser (self) -> None:
        name = self.username_entry.get()
        password = self.password_entry.get()
        self.cur.execute(
            """
                SELECT username FROM users
                WHERE username = ?
            """, (name,)
        )
        queryResult = self.cur.fetchall()
        if len(queryResult) > 0:
            messagebox.showerror("Error", "Username already exist")
            self.username_entry.set('Choose your username')
            self.login_window.focus()
        if (len(name) == 0 or len(password) == 0 or len(name) > 20 or len(password) > 20 or name.lower() == "create a password" or password.lower() == "choose your username"):
            messagebox.showerror("Error", "Invalid username or password, the username and password shall not be more than 20 characters")
            self.username_entry.set('Choose your username')
            self.password_entry.set('Create a password')
            self.password.config(show = "")
            self.login_window.focus()
        else:
            self.cur.execute(
                """
                INSERT INTO users VALUES 
                (?,?)
                """, (name, password)
            )
            messagebox.showinfo("Registration success", "User registered")
            self.conn.commit()
            self.revert_to_logIn()

    def revert_to_logIn (self) -> None:
        self.title_logIn.config(text = "Login")
        self.signin_button.config(text = "Sign In", command = self.check_login)
        self.register_button.config(text="Register", command = self.registerUser)
        self.username_entry.set('Username')
        self.password_entry.set('Password')
        self.password.config(show='')
        self.signin_button.config(state='normal')
        self.login_window.focus()
        self.login_window.bind('<Return>',self.check_login)
        self.login_window.title('Login')

    def userName_onClick (self, event) -> None:
        if self.username_entry.get() in ("Username", "Enter your username"):
            self.username.delete(0, "end")

    def password_onClick (self, event) -> None:
        if self.password_entry.get() in ("Password", "Create a password"):
            self.password.delete(0, "end")
            self.password.config(show="*")

    def run (self) -> None:
        self.login_window.mainloop()

# for individual module testing

if __name__ == "__main__":
    app = loginPage()
    app.run()