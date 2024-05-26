import os
import sqlite3 # sqlite is used to store data
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, StringVar # tkinter is used for gui
from datetime import datetime, timedelta
import matplotlib.pyplot as plt # matplotlib is used to generate financial graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates 

class adminInterface:
    def __init__(self) -> None:
        
        # build initial ui
        
        self.admin = tk.Tk()
        self.admin.resizable(False, False)
        self.admin.title("Restaurant System (Admin)")
        self.admin.protocol("WM_DELETE_WINDOW", self.breakWindow)

        self.topBar = ttk.Frame(self.admin)
        self.topBar.configure(height=100, width=200)
        self.system_label = ttk.Label(self.topBar)
        self.system_label.configure(font="{Times New Roman} 20 {bold}",
                                    padding="325 0",
                                    text='Restaurant System',
                                    width=18)
        self.system_label.grid(column=0, row=0, rowspan=1, sticky="ns")

        self.accountDetail = ttk.Frame(self.topBar)
        self.accountDetail.configure(height=200)


        self.displayUser = tk.Text(self.accountDetail)
        self.displayUser.configure(background="grey",
                                   font="{Arial} 12 {}",
                                   height=1,
                                   width=26)
        self.displayUser.grid(column=0, padx=5, pady=5, row=0, sticky="e")

        self.button_logOut = ttk.Button(self.accountDetail, command=self.logout)
        self.button_logOut.configure(text='Log Out', width=7)
        self.button_logOut.grid(column=0, padx=5, pady=5, row=1)
        self.accountDetail.grid(column=1, row=0)
        self.topBar.grid(column=0, row=0, rowspan=1)


        self.menuBar = ttk.Frame(self.admin)
        self.menuBar.configure(height=200)

        # menu buttons

        self.menu_reservation = ttk.Button(self.menuBar, command = self.reserve)
        self.menu_reservation.configure(text='Reservation', width=36, state = "disable")
        self.menu_reservation.grid(column=0, row=0)

        self.menu_dineIn = ttk.Button(self.menuBar, command = self.dineIn)
        self.menu_dineIn.configure(text='Dine In', width=37)
        self.menu_dineIn.grid(column=1, row=0)

        self.menu_financial = ttk.Button(self.menuBar, command = self.financial)
        self.menu_financial.configure(text='Financial', width=37)
        self.menu_financial.grid(column=2, row=0)

        self.menu_kitchen = ttk.Button(self.menuBar, command = self.kitchen)
        self.menu_kitchen.configure(text='Kitchen', width=37)
        self.menu_kitchen.grid(column=4, row=0)

        self.menu_tables = ttk.Button(self.menuBar, command = self.table_management)
        self.menu_tables.configure(text='Tables', width=36)
        self.menu_tables.grid(column=5, row=0)

        self.menuBar.grid(column=0, row=1)


        self.body = ttk.Frame(self.admin)
        self.body.configure(height=200, width=1154)
        self.body.grid(column=0, row=2, sticky="n")

        # hint text for entry field

        self.text_name = tk.Text(self.body)
        self.text_name.configure(background="#c0c0c0",
                                 font="{Arial} 12 {}",
                                 height=1,
                                 state="disabled",
                                 width=18)
        _text_ = 'Name:'
        self.text_name.configure(state="normal")
        self.text_name.insert("0.0", _text_)
        self.text_name.configure(state="disabled")
        self.text_name.grid(column=0, padx="370 5", pady="25 5", row=0)
        
        self.text_reserveDate = tk.Text(self.body)
        
        self.text_reserveDate.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Reserve Date:'
        self.text_reserveDate.configure(state="normal")
        self.text_reserveDate.insert("0.0", _text_)
        self.text_reserveDate.configure(state="disabled")
        self.text_reserveDate.grid(column=0, padx="370 5", pady=5, row=1)
        
        self.text_reserveTime = tk.Text(self.body)
        self.text_reserveTime.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Reserve Time:'
        self.text_reserveTime.configure(state="normal")
        self.text_reserveTime.insert("0.0", _text_)
        self.text_reserveTime.configure(state="disabled")
        self.text_reserveTime.grid(column=0, padx="370 5", pady=5, row=2)
        
        self.text_peopleNum = tk.Text(self.body)
        self.text_peopleNum.configure(background="#c0c0c0",
                                      font="{Arial} 12 {}",
                                      height=1,
                                      state="disabled",
                                      width=18)
        _text_ = 'Number of people:'
        self.text_peopleNum.configure(state="normal")
        self.text_peopleNum.insert("0.0", _text_)
        self.text_peopleNum.configure(state="disabled")
        self.text_peopleNum.grid(column=0, padx="370 5", pady=5, row=3)
        
        self.text_foodReserve = tk.Text(self.body)
        self.text_foodReserve.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Food reserve:'
        self.text_foodReserve.configure(state="normal")
        self.text_foodReserve.insert("0.0", _text_)
        self.text_foodReserve.configure(state="disabled")
        self.text_foodReserve.grid(column=0, padx="370 5", pady=5, row=4)
        
        # entry field styling

        self.name = StringVar()
        self.name.set("")
        self.entry_name = ttk.Entry(self.body, textvariable = self.name)
        self.entry_name.configure(font="{Arial} 12 {}", width=26)
        self.entry_name.grid(column=1, padx="5 370", pady="25 5", row=0)
        
        self.reserveDate = StringVar()
        self.reserveDate.set("")
        self.entry_reserveDate = ttk.Entry(self.body, textvariable = self.reserveDate)
        self.entry_reserveDate.configure(font="{Arial} 12 {}", width=26)
        self.entry_reserveDate.grid(column=1, padx="5 370", pady=5, row=1)
        
        self.reserveTime = StringVar()
        self.reserveTime.set("")
        self.entry_reserveTime = ttk.Entry(self.body, textvariable = self.reserveTime)
        self.entry_reserveTime.configure(font="{Arial} 12 {}", width=26)
        self.entry_reserveTime.grid(column=1, padx="5 370", pady=5, row=2)
        
        self.peopleNum = StringVar()
        self.peopleNum.set("")
        self.entry_peopleNum = ttk.Entry(self.body, textvariable = self.peopleNum)
        self.entry_peopleNum.configure(font="{Arial} 12 {}", width=26)
        self.entry_peopleNum.grid(column=1, padx="5 370", pady=5, row=3)
        
        self.foodReserve = StringVar()
        self.foodReserve.set("")
        self.entry_foodReserve = ttk.Entry(self.body, textvariable = self.foodReserve)
        self.entry_foodReserve.configure(font="{Arial} 12 {}", width=26)
        self.entry_foodReserve.grid(column=1, padx="5 370", pady=5, row=4)
        

        self.button_checkTable = ttk.Button(self.body, command= self.checkTableUI)
        self.button_checkTable.configure(text='Check Table')
        self.button_checkTable.grid(column=0, row=5, sticky="e")
        
        # confirm button

        self.button_confirm = ttk.Button(self.body)
        self.button_confirm.configure(text='Confirm', command = self.confirmOrder)
        self.button_confirm.grid(column=1,
                                 padx="0 480",
                                 pady=20,
                                 row=5,
                                 sticky="e")
        
        self.body.grid(column=0, ipady=219, row=2, sticky="n")

        # establish sqlite database connection

        relative_path = "db"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, relative_path, "restaurantSystem.db")
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

        # create required tables and views, inject some data into the tables

        self.runsql()
        self.insert_initial_data()

        # main widget

        self.mainwindow = self.admin

    # other functions

    def changeUserName (self, username: str) -> None: # change user name at the top right corner
        username = f"Username: {username}"
        self.displayUser.delete("1.0", tk.END)
        self.displayUser.insert(tk.END, username)

    def logout (self) -> None: # exit the window
        if messagebox.askokcancel("Leaving", "The Application would be closed") == True:
            self.admin.destroy()

    def runsql (self) -> None: # create necessary tables and views
        relative_path = "sql"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sql_path = os.path.join(script_dir, relative_path, "script.sql")
        with open(sql_path, 'r') as sql_file:
            sql_script = sql_file.read()

        self.cur.executescript(sql_script)
        self.conn.commit

    def insert_initial_data (self) -> None: # insert data into table storing food menu and details
        self.cur.execute(
            """
                SELECT * FROM dish_list
            """
        )
        result = self.cur.fetchone()
        if result:
            return
        else:
            relative_path = "sql"
            script_dir = os.path.dirname(os.path.abspath(__file__))
            sql_path = os.path.join(script_dir, relative_path, "insert_initial.sql")
            with open(sql_path, 'r') as sql_file:
                sql_script = sql_file.read()
            self.cur.executescript(sql_script)
            self.conn.commit

    def breakWindow (self) -> None: # exit the window
        if messagebox.askokcancel("Leaving", "The Application would be closed") == True:
            self.admin.destroy() 
            exit(0) 

    def clearBody (self) -> None: # remove the body content
        for widget in self.body.winfo_children():
            widget.grid_forget()

        self.body.grid_forget()

    def resetMenu (self) -> None: # revert the state of every other menu buttons to normal
        for menuButton in self.menuBar.winfo_children():
            menuButton.configure(state = "normal")

    def run(self) -> None: # run the tkinter main widget
        self.mainwindow.mainloop()

    # reservation body 

    def reserve (self) -> None:
        self.clearBody()
        self.resetMenu()
        self.menu_reservation.configure(state = "disable")

        self.text_name = tk.Text(self.body)
        self.text_name.configure(background="#c0c0c0",
                                 font="{Arial} 12 {}",
                                 height=1,
                                 state="disabled",
                                 width=18)
        _text_ = 'Name:'
        self.text_name.configure(state="normal")
        self.text_name.insert("0.0", _text_)
        self.text_name.configure(state="disabled")
        self.text_name.grid(column=0, padx="370 5", pady="25 5", row=0)
        
        self.text_reserveDate = tk.Text(self.body)
        self.text_reserveDate.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Reserve Date:'
        self.text_reserveDate.configure(state="normal")
        self.text_reserveDate.insert("0.0", _text_)
        self.text_reserveDate.configure(state="disabled")
        self.text_reserveDate.grid(column=0, padx="370 5", pady=5, row=1)
        
        self.text_reserveTime = tk.Text(self.body)
        self.text_reserveTime.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Reserve Time:'
        self.text_reserveTime.configure(state="normal")
        self.text_reserveTime.insert("0.0", _text_)
        self.text_reserveTime.configure(state="disabled")
        self.text_reserveTime.grid(column=0, padx="370 5", pady=5, row=2)
        
        self.text_peopleNum = tk.Text(self.body)
        self.text_peopleNum.configure(background="#c0c0c0",
                                      font="{Arial} 12 {}",
                                      height=1,
                                      state="disabled",
                                      width=18)
        _text_ = 'Number of people:'
        self.text_peopleNum.configure(state="normal")
        self.text_peopleNum.insert("0.0", _text_)
        self.text_peopleNum.configure(state="disabled")
        self.text_peopleNum.grid(column=0, padx="370 5", pady=5, row=3)
        
        self.text_foodReserve = tk.Text(self.body)
        self.text_foodReserve.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Food reserve:'
        self.text_foodReserve.configure(state="normal")
        self.text_foodReserve.insert("0.0", _text_)
        self.text_foodReserve.configure(state="disabled")
        self.text_foodReserve.grid(column=0, padx="370 5", pady=5, row=4)
        

        self.name = StringVar()
        self.name.set("")
        self.entry_name = ttk.Entry(self.body, textvariable = self.name)
        self.entry_name.configure(font="{Arial} 12 {}", width=26)
        self.entry_name.grid(column=1, padx="5 370", pady="25 5", row=0)
        
        self.reserveDate = StringVar()
        self.reserveDate.set("")
        self.entry_reserveDate = ttk.Entry(self.body, textvariable = self.reserveDate)
        self.entry_reserveDate.configure(font="{Arial} 12 {}", width=26)
        self.entry_reserveDate.grid(column=1, padx="5 370", pady=5, row=1)
        
        self.reserveTime = StringVar()
        self.reserveTime.set("")
        self.entry_reserveTime = ttk.Entry(self.body, textvariable = self.reserveTime)
        self.entry_reserveTime.configure(font="{Arial} 12 {}", width=26)
        self.entry_reserveTime.grid(column=1, padx="5 370", pady=5, row=2)
        
        self.peopleNum = StringVar()
        self.peopleNum.set("")
        self.entry_peopleNum = ttk.Entry(self.body, textvariable = self.peopleNum)
        self.entry_peopleNum.configure(font="{Arial} 12 {}", width=26)
        self.entry_peopleNum.grid(column=1, padx="5 370", pady=5, row=3)
        
        self.foodReserve = StringVar()
        self.foodReserve.set("")
        self.entry_foodReserve = ttk.Entry(self.body, textvariable=self.foodReserve)
        self.entry_foodReserve.configure(font="{Arial} 12 {}", width=26)
        self.entry_foodReserve.grid(column=1, padx="5 370", pady=5, row=4)
        

        self.button_checkTable = ttk.Button(self.body, command=self.checkTableUI)
        self.button_checkTable.configure(text='Check Table')
        self.button_checkTable.grid(column=0, row=5, sticky="e")
        
        self.button_confirm = ttk.Button(self.body, command=self.confirmOrder)
        self.button_confirm.configure(text='Confirm')
        self.button_confirm.grid(column=1,
                                 padx="0 480",
                                 pady=20,
                                 row=5,
                                 sticky="e")
        self.body.grid(column=0, ipady=219, row=2, sticky="n")

    # reservation functions

    def confirmOrder (self) -> None:
        
        # get str from entry field

        name = self.name.get()
        reserveDate = self.reserveDate.get()
        reserveTime = self.reserveTime.get()
        peopleNum = self.peopleNum.get()
        foodReserve = self.foodReserve.get()

        # check for user entry

        if not name or not reserveDate or not reserveTime or not peopleNum or not foodReserve:
            messagebox.showerror("Error", "Please fill in the required information")
            return
        else:
            reserveDateTime = self.validateTime(reserveDate, reserveTime)
            
            if not reserveDateTime:
                return
            else:
                reserveDate = reserveDateTime.strftime('%Y-%m-%d')
                endDateTime = reserveDateTime + timedelta(hours = 1)
                endTime = endDateTime.time().strftime('%H:%M') + ":00"
                reserveTime = reserveTime + ":00"
        
        try:
            peopleNum = int(peopleNum)
            if (peopleNum < 1) or (peopleNum > 12):
                messagebox.showwarning("Error", "Invalid input on Number of People or Number of People more than 12.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of people.")
            return
            
        # get in-use table

        table_inUse = self.getInUseTable(peopleNum, reserveDate, reserveTime, endTime)

        # simple check if all slots are full

        if len(table_inUse) >= 10:
            messagebox.showerror("Full Slot", "No more empty table left at the time.")
            return
        else:
            pass

        # prioritize based on number of people

        if (peopleNum >= 6):
            tableidALL = list(range(1, 4))
        else:
            tableidALL = list(range(4, 11))

        available_tables = []

        for table_id in tableidALL:
            if table_id not in table_inUse:
                available_tables.append(table_id)
        
        if len(available_tables) == 0: # when best fit are not available at the moment
            tableidALL = list(range(1, 11))
            for table_id in tableidALL:
                if table_id not in table_inUse:
                    available_tables.append(table_id)
        else:
            pass

        # check availability again

        selected_table = int(available_tables[0])
        if selected_table:
            pass
        else:
            messagebox("Full slot", "No more empty table left at the time")
            return
        
        self.addReserve(name, reserveDate, reserveTime, selected_table, foodReserve, endTime)
        messagebox.showinfo("Reservation Success", "Your reservation is recorded successfully")

        # check food reserve entry

        try: 
            foodReserve = int(foodReserve)
            if foodReserve < 0 or foodReserve > 1:
                messagebox.showerror("Error", "Please enter only integers of 0 and 1 for food reserve")
                return
            else:
                pass
        except ValueError:
            messagebox.showerror("Error", "Please enter only 0 and 1 in Food reserve, each represent False and True")
            return

        if foodReserve == 0:
            self.generateReserveReceipt(foodReserve_bool=0)
            return
        elif foodReserve == 1:
            self.foodReserveUI()
            return


    def addReserve(self, name : str, reserveDate : str, reserveTime : str, table_id : int, foodReserve : str, endTime : str) -> None:
        
        # record reservation details into database
        
        self.cur.execute(
            """
                INSERT INTO reservation (name, reserve_date, reserve_time, table_id, dish_bool) VALUES
                (?,?,?,?,?);
            """, (name, reserveDate, reserveTime, table_id, foodReserve)
        )
        self.conn.commit()

        self.cur.execute(
            """
                SELECT id FROM reservation 
                WHERE name = ? AND
                reserve_date = ? AND
                reserve_time = ? AND
                table_id = ?
            """, (name, reserveDate, reserveTime, table_id)
        )
        result = self.cur.fetchone()

        if result: 
            self.reserve_id = result[0]

        self.cur.execute(
            """
                INSERT INTO table_in_use (table_id, date, start_time, end_time) VALUES
                (?,?,?,?)
            """,(table_id, reserveDate, reserveTime, endTime)
        )
        self.conn.commit()

    def validateTime(self, reserveDate: str, reserveTime:str) -> datetime:

        # check user entried time

        currDateTime = datetime.now()
        openTime = datetime.strptime('10:00', '%H:%M')
        closeTime = datetime.strptime('22:00', '%H:%M')

        try:
            reserveDateTime = datetime.strptime(reserveDate + ' ' + reserveTime, '%Y-%m-%d %H:%M')

            if reserveDateTime.date() >= currDateTime.date() and openTime.time() <= reserveDateTime.time() <= closeTime.time():
                if reserveDateTime.date() == currDateTime.date(): 
                    if reserveDateTime.time() >= currDateTime.time():
                        return reserveDateTime
                    else:
                        messagebox.showerror("Invalid reservation date and time", "Please choose a time not in the past.")
                        return
                else:
                    return reserveDateTime
            else:
                messagebox.showerror("Invalid reservation date and time", "Please choose a date not before today and within operation hours.")
                return
        except ValueError:
            messagebox.showerror("Date Time Error", "Please enter date and time in correct format (date: YYYY-MM-DD, time: HH:MM)")
            return


    def getInUseTable(self, peopleNum : int, date : str, startTime : str, endTime : str) -> list[int]:
        if int(peopleNum) <= 6:
            tableCapacity = 6
        elif int(peopleNum) > 6 and int(peopleNum) <= 12:
            tableCapacity = 12

        self.cur.execute(
            """
            SELECT table_id from table_inUse_view 
            WHERE date = ? AND
                  time <= ? AND
                  end_time >= ? AND
                  time <= ? AND
                  end_time >= ? AND
                  table_capacity >= ? 
            """, (date, startTime, startTime, endTime, endTime, tableCapacity)
        )
        result = self.cur.fetchall()
        inUse_table = [int(item) for inner_list in result for item in inner_list]
        
        return inUse_table
        
    def checkTableUI (self) -> None:

        # ui for check table

        self.clearBody()
        self.resetMenu()
                
        # hint text for entry field

        self.text_reserveDate = tk.Text(self.body)
        self.text_reserveDate.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Reserve Date:'
        self.text_reserveDate.configure(state="normal")
        self.text_reserveDate.insert("0.0", _text_)
        self.text_reserveDate.configure(state="disabled")
        self.text_reserveDate.grid(column=0, padx="370 5", pady="95 5", row=1)
        
        self.text_reserveTime = tk.Text(self.body)
        self.text_reserveTime.configure(background="#c0c0c0",
                                        font="{Arial} 12 {}",
                                        height=1,
                                        state="disabled",
                                        width=18)
        _text_ = 'Reserve Time:'
        self.text_reserveTime.configure(state="normal")
        self.text_reserveTime.insert("0.0", _text_)
        self.text_reserveTime.configure(state="disabled")
        self.text_reserveTime.grid(column=0, padx="370 5", pady=5, row=2)
        
        self.text_peopleNum = tk.Text(self.body)
        self.text_peopleNum.configure(background="#c0c0c0",
                                      font="{Arial} 12 {}",
                                      height=1,
                                      state="disabled",
                                      width=18)
        _text_ = 'Number of people:'
        self.text_peopleNum.configure(state="normal")
        self.text_peopleNum.insert("0.0", _text_)
        self.text_peopleNum.configure(state="disabled")
        self.text_peopleNum.grid(column=0, padx="370 5", pady=5, row=3)
        
        # styling for entry field
        
        self.reserveDate = StringVar()
        self.reserveDate.set("")
        self.entry_reserveDate = ttk.Entry(self.body, textvariable = self.reserveDate)
        self.entry_reserveDate.configure(font="{Arial} 12 {}", width=26)
        self.entry_reserveDate.grid(column=1, padx="5 370", pady="94 5", row=1)
        
        self.reserveTime = StringVar()
        self.reserveTime.set("")
        self.entry_reserveTime = ttk.Entry(self.body, textvariable = self.reserveTime)
        self.entry_reserveTime.configure(font="{Arial} 12 {}", width=26)
        self.entry_reserveTime.grid(column=1, padx="5 370", pady=5, row=2)
        
        self.peopleNum = StringVar()
        self.peopleNum.set("")
        self.entry_peopleNum = ttk.Entry(self.body, textvariable = self.peopleNum)
        self.entry_peopleNum.configure(font="{Arial} 12 {}", width=26)
        self.entry_peopleNum.grid(column=1, padx="5 370", pady=5, row=3)
        
        self.button_check = ttk.Button(self.body, command=self.checkTable)
        self.button_check.configure(text='Check')
        self.button_check.grid(column=0, row=5, sticky="e")
        
        self.button_back = ttk.Button(self.body, command=self.reserve)
        self.button_back.configure(text='Back')
        self.button_back.grid(column=1,
                              padx="0 480",
                              pady=20,
                              row=5,
                              sticky="e")
        self.body.grid(column=0, ipady=219, row=2, sticky="n")
    
    def checkTable (self) -> None: 
        
        # check table available at the moment
        
        reserveDate = self.reserveDate.get()
        reserveTime = self.reserveTime.get()
        peopleNum = self.peopleNum.get()
        if not reserveDate or not reserveTime or not peopleNum:
            messagebox.showerror("Error", "Please fill in the required information")
            return
        else:
            reserveDateTime = self.validateTime(reserveDate, reserveTime)
            endDateTime = reserveDateTime + timedelta(hours = 1)
            endTime = endDateTime.time().strftime('%H:%M') + ":00"
            
            reserveDate = reserveDateTime.strftime("%Y-%m-%d")
            reserveTime += ":00"
        
        try:
            peopleNum = int(peopleNum)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number of people.")
            return

        table_inUse = self.getInUseTable(peopleNum, reserveDate, reserveTime, endTime)

        if len(table_inUse) >= 10:
            messagebox.showerror("Full Slot", "No more empty table left at given time frame.")
            return
        else:
            tableidALL = list(range(1, 11))
            available_tables = []
            for table_id in tableidALL:
                if table_id not in table_inUse:
                    available_tables.append(table_id)
            
            messagebox.showinfo("Slot Available", f"Table available: {available_tables}.")

    def generateReserveReceipt (self, foodReserve_bool = 1) -> None:
        
        # generate receipt for reservation

        reserve_id = self.reserve_id
        if foodReserve_bool == 1:
            self.cur.execute(
                """
                    SELECT r.id, 
                           r.datetime, 
                           r.reserve_date, 
                           r.reserve_time, 
                           r.table_id, 
                           dish.dish_name, 
                           rd.dish_unit_price, 
                           rd.dish_amount
                    FROM reservation r
                    JOIN reserve_dish rd ON r.id = rd.reserve_id
                    JOIN dish_list dish ON rd.dish_id = dish.dish_id
                    WHERE r.id = ?
                """, (reserve_id,)
            )

            result = self.cur.fetchall()
            reserve_datetime = result[0][1]
            reserve_date = result[0][2]
            reserve_time = result[0][3]
            reserve_tableID = result[0][4]

            reserve_dish = []
            reserve_dish_price = []
            reserve_dish_amount = []

            for index in range(len(result)):
                reserve_dish.append(result[index][5])
                reserve_dish_price.append(result[index][6])
                reserve_dish_amount.append(result[index][7])
            
            receipt_text = f"Reserve ID: {reserve_id}\nDatetime: {reserve_datetime}\nTable ID: {reserve_tableID}\nReserve Date: {reserve_date}\nReserve_time: {reserve_time}\n\nDishes:\n"
            total_cost = 0

            for dish, price, amount in zip(reserve_dish, reserve_dish_price, reserve_dish_amount):
                total_cost += price * amount
                receipt_text += f"{dish}: {amount} x RM{price:.2f} = RM{price * amount:.2f}\n"

            receipt_text += f"\nTotal: RM{total_cost:.2f}"

        elif foodReserve_bool == 0:
            self.cur.execute(
                """
                    SELECT id, datetime, reserve_date, reserve_time, table_id FROM reservation 
                    WHERE id = ?
                """, (reserve_id,)
            )
            result = self.cur.fetchall()
            reserve_datetime = result[0][1]
            reserve_date = result[0][2]
            reserve_time = result[0][3]
            reserve_tableID = result[0][4]

            receipt_text = f"Reserve ID: {reserve_id}\nDatetime: {reserve_datetime}\nTable ID: {reserve_tableID}\nReserve Date: {reserve_date}\nReserve_time: {reserve_time}"

        receiptRelativePath = "reserve_receipt"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fileName = os.path.join(script_dir, receiptRelativePath, f"reserve-{reserve_id}.txt")

        with open(fileName, "w") as file:
            file.write(receipt_text)

        messagebox.showinfo("Receipt Generated", f"Receipt is located at {fileName}")


    def foodReserveUI (self) -> None: 

        # interface for food reservation for food_bool = 1

        self.clearBody()
        self.resetMenu()

        self.frame_foodList = ttk.Frame(self.body)
        self.frame_foodList.configure(height=200, width=200)

        self.foodList_yscroll = ttk.Scrollbar(self.frame_foodList)
        self.foodList_yscroll.configure(orient="vertical")
        self.foodList_yscroll.grid(column=1, row=0, sticky="ns")
        self.table_foodList = ttk.Treeview(self.frame_foodList, yscrollcommand=self.foodList_yscroll.set)
        self.table_foodList.bind("<<TreeviewSelect>>", self.onClick_reserveFoodListTable)
        self.table_foodList.bind("<MouseWheel>", self.table_foodList_mouseWheelscroll)
        self.table_foodList.configure(height=15,
                                      selectmode="browse",
                                      show="headings",
                                      takefocus=True)
        self.table_foodList_cols = ['col_foodID', 'col_foodName', 'col_foodPrice']
        self.table_foodList_dcols = ['col_foodID', 'col_foodName', 'col_foodPrice']
        self.table_foodList.configure(columns=self.table_foodList_cols,
                                      displaycolumns=self.table_foodList_dcols)
        self.table_foodList.column("#0",
                                   width=0,
                                   stretch=tk.NO)
        self.table_foodList.column("col_foodID",
                                   anchor="w",
                                   stretch=True,
                                   width=50,
                                   minwidth=20)
        self.table_foodList.column("col_foodName",
                                   anchor="w",
                                   stretch=True,
                                   width=300,
                                   minwidth=20)
        self.table_foodList.column("col_foodPrice",
                                   anchor="center",
                                   stretch=True,
                                   width=100,
                                   minwidth=20)
        self.table_foodList.heading("col_foodID", anchor="center", text='Food ID')
        self.table_foodList.heading("col_foodName", anchor="center", text='Food Name')
        self.table_foodList.heading("col_foodPrice", anchor="w", text='Food Price (RM)')
        self.table_foodList.grid(column=0, row=0)
        self.frame_foodList.grid(column=1, padx="0 97", pady="20 50", row=0)


        self.frame_orderList = ttk.Frame(self.body)
        self.frame_orderList.configure(height=200, width=200)

        self.orderlist_yscroll = ttk.Scrollbar(self.frame_orderList)
        self.orderlist_yscroll.configure(orient="vertical")
        self.orderlist_yscroll.grid(column=1, row=0, sticky="ns")
        self.table_itemOrdered = ttk.Treeview(self.frame_orderList, yscrollcommand=self.orderlist_yscroll.set)
        self.table_itemOrdered.bind("<MouseWheel>", self.table_itemOrdered_mouseWheelScroll)
        self.table_itemOrdered.configure(selectmode="browse")
        self.table_itemOrdered_cols = ['orderedcol_foodID','orderedcol_foodPrice','orderedcol_amount']
        self.table_itemOrdered_dcols = ['orderedcol_foodID','orderedcol_foodPrice','orderedcol_amount']
        self.table_itemOrdered.configure(columns=self.table_itemOrdered_cols,
                                         displaycolumns=self.table_itemOrdered_dcols)
        self.table_itemOrdered.column("#0", 
                                      width=0,
                                      stretch=tk.NO)
        self.table_itemOrdered.column("orderedcol_foodID", 
                                      anchor="w", 
                                      stretch=True, 
                                      width=100, 
                                      minwidth=20)
        self.table_itemOrdered.column("orderedcol_foodPrice", 
                                      anchor = "center", 
                                      stretch=True, 
                                      width=100, 
                                      minwidth=20)
        self.table_itemOrdered.column("orderedcol_amount",
                                      anchor="w",
                                      stretch=True,
                                      width=200,
                                      minwidth=20)
        self.table_itemOrdered.heading("orderedcol_foodID", anchor="center", text='Food ID')
        self.table_itemOrdered.heading("orderedcol_foodPrice", anchor="center", text='Food Price')
        self.table_itemOrdered.heading("orderedcol_amount", anchor="center", text='Amount')
        self.table_itemOrdered.grid(column=0, row=0)
        self.frame_orderList.grid(column=1, row=1)


        self.frame_addorder = ttk.Frame(self.body)
        self.frame_addorder.configure(height=200, width=200)

        self.text_foodID = tk.Text(self.frame_addorder)
        self.text_foodID.configure(background="#c0c0c0",
                                   font="{Arial} 12 {bold}",
                                   height=1,
                                   state="disabled",
                                   width=18)
        _text_ = 'Food ID:'
        self.text_foodID.configure(state="normal")
        self.text_foodID.insert("0.0", _text_)
        self.text_foodID.configure(state="disabled")
        self.text_foodID.grid(column=0, padx="80 5", pady="0 10", row=0)

        self.text_foodName = tk.Text(self.frame_addorder)
        self.text_foodName.configure(background="#c0c0c0",
                                     font="{Arial} 12 {bold}",
                                     height=1,
                                     state="disabled",
                                     width=18)
        _text_ = 'Food Name'
        self.text_foodName.configure(state="normal")
        self.text_foodName.insert("0.0", _text_)
        self.text_foodName.configure(state="disabled")
        self.text_foodName.grid(column=0, padx="80 5", pady="0 10", row=1)

        self.text_unitPrice = tk.Text(self.frame_addorder)
        self.text_unitPrice.configure(background="#c0c0c0",
                                      font="{Arial} 12 {bold}",
                                      height=1,
                                      state="disabled",
                                      width=18)
        _text_ = 'Unit Price (RM):'
        self.text_unitPrice.configure(state="normal")
        self.text_unitPrice.insert("0.0", _text_)
        self.text_unitPrice.configure(state="disabled")
        self.text_unitPrice.grid(column=0, padx="80 5", pady="0 10", row=2)

        self.text_amount = tk.Text(self.frame_addorder)
        self.text_amount.configure(background="#c0c0c0",
                                   font="{Arial} 12 {bold}",
                                   height=1,
                                   state="disabled",
                                   width=18)
        _text_ = 'Amount:'
        self.text_amount.configure(state="normal")
        self.text_amount.insert("0.0", _text_)
        self.text_amount.configure(state="disabled")
        self.text_amount.grid(column=0, padx="80 5", pady="0 10", row=3)

        self.foodID = StringVar()
        self.foodID.set("")
        self.entry_foodID = ttk.Entry(self.frame_addorder, textvariable = self.foodID)
        self.entry_foodID.configure(font="{Arial} 12 {}", width=26)
        self.entry_foodID.grid(column=1, padx="0 20", pady="0 10", row=0)

        self.foodName = StringVar()
        self.foodName.set("")
        self.entry_foodName = ttk.Entry(self.frame_addorder, textvariable = self.foodName)
        self.entry_foodName.configure(font="{Arial} 12 {}", width=26)
        self.entry_foodName.grid(column=1, padx="0 20", pady="0 10", row=1)

        self.unitPrice = StringVar()
        self.unitPrice.set("")
        self.entry_unitPrice = ttk.Entry(self.frame_addorder, textvariable = self.unitPrice)
        self.entry_unitPrice.configure(font="{Arial} 12 {}", width=26)
        self.entry_unitPrice.grid(column=1, padx="0 20", pady="0 10", row=2)

        self.amount = StringVar()
        self.amount.set("")
        self.entry_amount = ttk.Entry(self.frame_addorder, textvariable = self.amount)
        self.entry_amount.configure(font="{Arial} 12 {}", width=26)
        self.entry_amount.grid(column=1, padx="0 20", pady="0 10", row=3)


        self.button_addOrder = ttk.Button(self.frame_addorder, command = self.appendFoodReserve)
        self.button_addOrder.configure(text='Add Order')
        self.button_addOrder.grid(column=0, columnspan=2, pady="30 0", row=4)
        self.frame_addorder.grid(column=0, padx="0 80", row=0, rowspan=2)

        self.button_refresh = ttk.Button(self.body, command = self.foodReserveUI)
        self.button_refresh.configure(text='Refresh')
        self.button_refresh.grid(column=0, pady="20 30", row=2)

        self.button_confirm = ttk.Button(self.body)
        self.button_confirm.configure(text='Confirm', command = self.addFoodReserve)
        self.button_confirm.grid(column=1, pady="20 30", row=2)
        self.body.grid(column=0, row=2)

        self.buildReserveFoodMenu()

    def table_foodList_mouseWheelscroll (self, event) -> None:
        self.table_foodList.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def table_itemOrdered_mouseWheelScroll (self, event):
        self.table_itemOrdered.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def onClick_reserveFoodListTable (self, event) -> None:
        cur = self.table_foodList.selection()
        cur = self.table_foodList.item(cur)
        list = cur['values']
        if(len(list) == 3):
            self.foodID.set(list[0])
            self.foodName.set(list[1])
            self.unitPrice.set(list[2])
            self.amount.set("1")

    def appendFoodReserve (self) -> None:

        # insert reserved food into tkinter treeview

        foodID = self.foodID.get()
        unitPrice = self.unitPrice.get()
        amount = self.amount.get()

        if not (foodID or unitPrice or amount):
            messagebox.showerror("Error", "Please filled in all the required information")
            return
        else:   
            pass

        orderedFood = []
        for food_id in self.table_itemOrdered.get_children():
            food = self.table_itemOrdered.item(food_id)['values'][0]
            orderedFood.append(str(food))

        if foodID in orderedFood:
            messagebox.showerror("Food Order Repeated", "Please try again and place order of different food each time.")
            return
        else:
            pass

        orderList = [foodID, unitPrice, amount]
        self.table_itemOrdered.insert("", tk.END, values=orderList)

    def buildReserveFoodMenu (self) -> None:

        # query from dish_list table and insert into tkinter treeview

        self.cur.execute(
            """
                SELECT dish_id, dish_name, dish_price FROM dish_list
                ORDER BY dish_id
            """
        )
        foodMenu = self.cur.fetchall()

        for item in foodMenu:
            self.table_foodList.insert("", tk.END, values=item)

    def addFoodReserve (self) -> None:

        # get the list of ordered dish and insert into reserve_dish table

        ordered_items = []
        reserve_id = self.reserve_id

        for child in self.table_itemOrdered.get_children():
            item_values = self.table_itemOrdered.item(child)['values']
            ordered_items.append(item_values)

        if not ordered_items:
            messagebox.showerror("Error", "No items to reserve.")
            return  # Exit the function if there are no items to reserve
        else:
            pass

        for index in range(len(ordered_items)):
            self.cur.execute(
                """
                    INSERT INTO reserve_dish (reserve_id, dish_id, dish_unit_price, dish_amount) VALUES
                    (?, ?, ?, ?)
                """, (reserve_id, ordered_items[index][0], ordered_items[index][1], ordered_items[index][2])
            )
            
        self.conn.commit()
        messagebox.showinfo("Food Reserve Sucess", "Food reservation sucessfully saved")
        self.generateReserveReceipt() # generate receipt when the food reserved is stored into the database
        self.reserve() # reload the reservation ui

    
    # dinein body

    def dineIn (self) -> None:
        self.clearBody()
        self.resetMenu()
        self.menu_dineIn.configure(state = "disable")

        self.frame_foodList = ttk.Frame(self.body)
        self.frame_foodList.configure(height=200, width=200)

        self.foodList_yscroll = ttk.Scrollbar(self.frame_foodList)
        self.foodList_yscroll.configure(orient="vertical")
        self.foodList_yscroll.grid(column=1, row=0, sticky="ns")
        self.table_foodList = ttk.Treeview(self.frame_foodList, yscrollcommand=self.foodList_yscroll.set)
        self.table_foodList.bind("<<TreeviewSelect>>", self.onClick_dineInFoodListTable)
        self.table_foodList.bind("<MouseWheel>", self.table_foodList_mouseWheelscroll)
        self.table_foodList.configure(height=15,
                                      selectmode="browse",
                                      show="headings",
                                      takefocus=True)
        self.table_foodList_cols = ['col_foodID', 'col_foodName', 'col_foodPrice']
        self.table_foodList_dcols = ['col_foodID', 'col_foodName', 'col_foodPrice']
        self.table_foodList.configure(columns=self.table_foodList_cols,
                                      displaycolumns=self.table_foodList_dcols)
        self.table_foodList.column("#0",
                                   width=0,
                                   stretch=tk.NO)
        self.table_foodList.column("col_foodID",
                                   anchor="w",
                                   stretch=True,
                                   width=50,
                                   minwidth=20)
        self.table_foodList.column("col_foodName",
                                   anchor="w",
                                   stretch=True,
                                   width=300,
                                   minwidth=20)
        self.table_foodList.column("col_foodPrice",
                                   anchor="center",
                                   stretch=True,
                                   width=100,
                                   minwidth=20)
        self.table_foodList.heading("col_foodID", anchor="center", text='Food id')
        self.table_foodList.heading("col_foodName", anchor="center", text='Food Name')
        self.table_foodList.heading("col_foodPrice", anchor="w", text='Food Price (RM)')
        self.table_foodList.grid(column=0, row=0)
        self.frame_foodList.grid(column=1, padx="0 97", pady="20 50", row=0)


        self.frame_orderList = ttk.Frame(self.body)
        self.frame_orderList.configure(height=200, width=200)

        self.orderlist_yscroll = ttk.Scrollbar(self.frame_orderList)
        self.orderlist_yscroll.configure(orient="vertical")
        self.orderlist_yscroll.grid(column=1, row=0, sticky="ns")
        self.table_itemOrdered = ttk.Treeview(self.frame_orderList, yscrollcommand=self.orderlist_yscroll.set)
        self.table_itemOrdered.bind("<MouseWheel>", self.table_itemOrdered_mouseWheelScroll)
        self.table_itemOrdered.configure(selectmode="browse")
        self.table_itemOrdered_cols = ['orderedcol_foodID','orderedcol_foodPrice','orderedcol_amount']
        self.table_itemOrdered_dcols = ['orderedcol_foodID','orderedcol_foodPrice','orderedcol_amount']
        self.table_itemOrdered.configure(columns=self.table_itemOrdered_cols,
                                         displaycolumns=self.table_itemOrdered_dcols)
        self.table_itemOrdered.column("#0", 
                                      width=0,
                                      stretch=tk.NO)
        self.table_itemOrdered.column("orderedcol_foodID", 
                                      anchor="center", 
                                      stretch=True, 
                                      width=100, 
                                      minwidth=20)
        self.table_itemOrdered.column("orderedcol_foodPrice", 
                                      anchor = "center", 
                                      stretch=True, 
                                      width=100, 
                                      minwidth=20)
        self.table_itemOrdered.column("orderedcol_amount",
                                      anchor="center",
                                      stretch=True,
                                      width=200,
                                      minwidth=20)
        self.table_itemOrdered.heading("orderedcol_foodID", anchor="center", text='Food ID')
        self.table_itemOrdered.heading("orderedcol_foodPrice", anchor="center", text='Food Price')
        self.table_itemOrdered.heading("orderedcol_amount", anchor="center", text='Amount')
        self.table_itemOrdered.grid(column=0, row=0)
        self.frame_orderList.grid(column=1, row=1)


        self.frame_addorder = ttk.Frame(self.body)
        self.frame_addorder.configure(height=200, width=200)

        self.text_foodID = tk.Text(self.frame_addorder)
        self.text_foodID.configure(background="#c0c0c0",
                                   font="{Arial} 12 {bold}",
                                   height=1,
                                   state="disabled",
                                   width=18)
        _text_ = 'Food ID:'
        self.text_foodID.configure(state="normal")
        self.text_foodID.insert("0.0", _text_)
        self.text_foodID.configure(state="disabled")
        self.text_foodID.grid(column=0, padx="80 5", pady="0 10", row=0)

        self.text_tableID = tk.Text(self.frame_addorder)
        self.text_tableID.configure(background="#c0c0c0",
                                    font="{Arial} 12 {bold}",
                                    height=1,
                                    state="disabled",
                                    width=18)
        _text_ = 'Table ID:'
        self.text_tableID.configure(state="normal")
        self.text_tableID.insert("0.0", _text_)
        self.text_tableID.configure(state="disabled")
        self.text_tableID.grid(column=0, padx="80 5", pady="0 10", row=1)

        self.text_unitPrice = tk.Text(self.frame_addorder)
        self.text_unitPrice.configure(background="#c0c0c0",
                                      font="{Arial} 12 {bold}",
                                      height=1,
                                      state="disabled",
                                      width=18)
        _text_ = 'Unit Price (RM):'
        self.text_unitPrice.configure(state="normal")
        self.text_unitPrice.insert("0.0", _text_)
        self.text_unitPrice.configure(state="disabled")
        self.text_unitPrice.grid(column=0, padx="80 5", pady="0 10", row=2)

        self.text_amount = tk.Text(self.frame_addorder)
        self.text_amount.configure(background="#c0c0c0",
                                   font="{Arial} 12 {bold}",
                                   height=1,
                                   state="disabled",
                                   width=18)
        _text_ = 'Amount:'
        self.text_amount.configure(state="normal")
        self.text_amount.insert("0.0", _text_)
        self.text_amount.configure(state="disabled")
        self.text_amount.grid(column=0, padx="80 5", pady="0 10", row=3)

        self.foodID = StringVar()
        self.foodID.set("")
        self.entry_foodID = ttk.Entry(self.frame_addorder, textvariable = self.foodID)
        self.entry_foodID.configure(font="{Arial} 12 {}", width=26)
        self.entry_foodID.grid(column=1, padx="0 20", pady="0 10", row=0)

        self.tableID = StringVar()
        self.tableID.set("")
        self.entry_tableID = ttk.Entry(self.frame_addorder, textvariable = self.tableID)
        self.entry_tableID.configure(font="{Arial} 12 {}", width=26)
        self.entry_tableID.grid(column=1, padx="0 20", pady="0 10", row=1)

        self.unitPrice = StringVar()
        self.unitPrice.set("")
        self.entry_unitPrice = ttk.Entry(self.frame_addorder, textvariable = self.unitPrice)
        self.entry_unitPrice.configure(font="{Arial} 12 {}", width=26)
        self.entry_unitPrice.grid(column=1, padx="0 20", pady="0 10", row=2)

        self.amount = StringVar()
        self.amount.set("")
        self.entry_amount = ttk.Entry(self.frame_addorder, textvariable = self.amount)
        self.entry_amount.configure(font="{Arial} 12 {}", width=26)
        self.entry_amount.grid(column=1, padx="0 20", pady="0 10", row=3)


        self.button_addOrder = ttk.Button(self.frame_addorder, command = self.appendFoodOrder)
        self.button_addOrder.configure(text='Add Order')
        self.button_addOrder.grid(column=0, columnspan=2, pady="30 0", row=4)
        self.frame_addorder.grid(column=0, padx="0 80", row=0, rowspan=2)

        self.button_refresh = ttk.Button(self.body, command = self.dineIn)
        self.button_refresh.configure(text='Refresh')
        self.button_refresh.grid(column=0, pady="20 30", row=2)

        self.button_confirm = ttk.Button(self.body)
        self.button_confirm.configure(text='Confirm', command = self.addFoodOrder)
        self.button_confirm.grid(column=1, pady="20 30", row=2)
        self.body.grid(column=0, row=2)

        self.buildDineInFoodMenu()

    # dinein functions

    def onClick_dineInFoodListTable (self, event) -> None:
        cur = self.table_foodList.selection()
        cur = self.table_foodList.item(cur)
        list = cur['values']
        if(len(list) == 3):
            self.foodID.set(list[0])
            self.unitPrice.set(list[2])
            self.amount.set("1")

    def appendFoodOrder (self) -> None:

        # insert ordered food into tkinter treeview

        foodID = self.foodID.get()
        unitPrice = self.unitPrice.get()
        amount = self.amount.get()

        if not (foodID or unitPrice or amount):
            messagebox.showerror("Error", "Please filled in all the required information")
            return
        else:   
            pass

        orderedFood = []
        for food_id in self.table_itemOrdered.get_children():
            food = self.table_itemOrdered.item(food_id)['values'][0]
            orderedFood.append(str(food))

        if foodID in orderedFood:
            messagebox.showerror("Food Order Repeated", "Please try again and place order of different food each time.")
            return
        else:
            pass

        orderList = [foodID, unitPrice, amount]
        self.table_itemOrdered.insert("", tk.END, values=orderList)

    def buildDineInFoodMenu (self) -> None:

        # query and insert data from dish_list table into tkinter treeview

        self.cur.execute(
            """
                SELECT dish_id, dish_name, dish_price FROM dish_list
                ORDER BY dish_id
            """
        )

        foodMenu = self.cur.fetchall()

        for item in foodMenu:
            self.table_foodList.insert("", tk.END, values=item)

    def addFoodOrder (self) -> None:

        # get table ID, food ordered from tkinter treeview, insert everything into dineIn_cashier table

        ordered_items = []
        tableID = self.tableID.get()
        
        # check is the user entered table ID or not

        if not tableID:
            messagebox.showerror("Error", "Please enter the table ID to complete the order.")
            return
        else:
            pass
        
        # check is the entered table ID is in use at the time or not 

        today = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')
        
        self.cur.execute(
            """
                SELECT table_id FROM table_in_use 
                WHERE date = ? AND
                      start_time <= ? AND
                      end_time >= ?
            """, (today, current_time, current_time)
        )

        result = self.cur.fetchall()
        table_inUse = [row[0] for row in result]

        if int(tableID) in table_inUse:
            messagebox.showerror("Table not available", f"The table with id {tableID} is occupied at the moment")
            return
        else:
            pass

        for child in self.table_itemOrdered.get_children():
            item_values = self.table_itemOrdered.item(child)['values']
            ordered_items.append(item_values)
        
        if not ordered_items:
            messagebox.showerror("Error", "No items to reserve.")
            return  # exit the function if there is no item to reserve
        else:
            pass

        # check the last order_id in the dineIn_cashier table to make increment of order_id

        self.cur.execute(
            """
                SELECT order_id FROM dineIn_cashier 
                ORDER BY order_id DESC
            """
        )

        result = self.cur.fetchone()
        if result:
            self.order_id = str(int(result[0]) + 1)
        else: 
            self.order_id = str(1)

        # insert the ordered food into dineIn_kitchen with the order_id

        for index in range(len(ordered_items)):
            self.cur.execute(
                """
                    INSERT INTO dineIn_cashier (order_id, table_id, dish_id, dish_price, dish_amount) VALUES
                    (?, ?, ?, ?, ?)
                """, (self.order_id, tableID, ordered_items[index][0], ordered_items[index][1], ordered_items[index][2])
            )

        self.conn.commit()

        currentDate = datetime.now().strftime("%Y-%m-%d")
        currentTime = datetime.now().strftime("%H:%M:%S")
        endTime = (datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")

        self.cur.execute(
            """
                INSERT INTO table_in_use (table_id, date, start_time, end_time) VALUES
                (?,?,?,?)
            """,(tableID, currentDate, currentTime, endTime)
        )


        self.cur.execute(
            """
                SELECT order_id, datetime, dish_id, dish_amount FROM dineIn_cashier
                WHERE order_id = ?
            """, (self.order_id)
        )

        result = self.cur.fetchall()

        for row in result:
            datetime_str = row[1]
            datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            time_only = datetime_obj.strftime('%H:%M')
            
            row_in_list = list(row)
            row_in_list[1] = time_only

            self.cur.execute(
                """
                    INSERT INTO dineIn_kitchen (order_id, time, dish_id, dish_amount) VALUES    
                    (?, ?, ?, ?)
                """, (row_in_list[0], time_only, row_in_list[2], row_in_list[3])
            )
            
        self.conn.commit()

        messagebox.showinfo("Food Order Sucess", "Food Order sucessfully saved")
        self.generateOrderReceipt()
        self.dineIn()
        

    def generateOrderReceipt (self) -> None:

        # generate receipt for food order

        order_id = self.order_id

        self.cur.execute(
            """
                SELECT dine.order_id, 
                       dine.datetime,
                       dine.table_id, 
                       dish.dish_name, 
                       dine.dish_price,
                       dine.dish_amount
                FROM dineIn_cashier dine
                    JOIN dish_list dish ON dine.dish_id = dish.dish_id
                WHERE dine.order_id = ?
            """, (order_id,)
        )

        result = self.cur.fetchall()
        order_datetime = result[0][1]
        order_tableID = result[0][2]
        order_dish = []
        order_dish_price = []
        order_dish_amount = []

        for index in range(len(result)):
            order_dish.append(result[index][3])
            order_dish_price.append(result[index][4])
            order_dish_amount.append(result[index][5])
        
        receipt_text = f"Order ID: {order_id}\nDatetime: {order_datetime}\nTable ID: {order_tableID}\n\nDishes:\n"
        total_cost = 0

        for dish, price, amount in zip(order_dish, order_dish_price, order_dish_amount):
            total_cost += price * amount
            receipt_text += f"{dish}: {amount} x RM{price:.2f} = RM{price * amount:.2f}\n"

        receipt_text += f"\nTotal: RM{total_cost:.2f}"

        receiptRelativePath = "dineIn_receipt"
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fileName = os.path.join(script_dir, receiptRelativePath, f"order-{order_id}.txt")

        with open(fileName, "w") as file:
            file.write(receipt_text)

        messagebox.showinfo("Receipt Generated", f"Receipt is located at {fileName}")

    # financial body

    def financial (self) -> None:
        self.clearBody()
        self.resetMenu()
        self.menu_financial.configure(state = "disable")

        self.frame_generateButtons = ttk.Frame(self.body)
        self.frame_generateButtons.configure(height=200, width=200)


        self.button_allTime = ttk.Button(self.frame_generateButtons, command=self.generateAllTime)
        self.button_allTime.configure(text='Generate All Time')
        self.button_allTime.grid(
            column=0, pady="20 5", row=0, sticky="ew")
        
        self.button_OneYear = ttk.Button(self.frame_generateButtons, command=self.generateOneYear)
        self.button_OneYear.configure(text='Generate One Year')
        self.button_OneYear.grid(column=0, pady=5, row=1, sticky="ew")
        
        self.button_OneMonth = ttk.Button(self.frame_generateButtons, command=self.generateOneMonth)
        self.button_OneMonth.configure(text='Generate One Month')
        self.button_OneMonth.grid(
            column=0, pady=5, row=2, sticky="ew")
        
        self.button_OneWeek = ttk.Button(self.frame_generateButtons, command=self.generateOneWeek)
        self.button_OneWeek.configure(text='Generate One Week')
        self.button_OneWeek.grid(
            column=0, pady="5 20", row=3, sticky="ew")
        
        self.frame_generateButtons.grid(column=0, padx=516, row=4)
        self.body.grid(column=0, ipady=255, row=2)
    
    # financial functions

    def generateAllTime (self) -> None:
        self.cur.execute(
            """
                SELECT date, 
                       SUM(dish_amount * dish_price) AS total_sales, 
                       SUM(dish_amount * dish_cost) AS total_cost,
                       SUM(dish_amount * (dish_price - dish_cost)) AS gross_profit  
                FROM kitchen_view
                WHERE 
                serving_stat == "PAID"
                GROUP BY date
                ORDER BY date
            """
        )

        try:
            result = self.cur.fetchall()
            dates, total_sales, total_cost, gross_profit = zip(*result)
        except ValueError:
            messagebox.showerror("Error", "The sales data is insufficient to generate graphs")
            return
        
        graph = tk.Tk()
        graph.title("Financial Report (All Time)")
        graph.geometry("1400x800")

        frame_graph = tk.Frame(graph)
        frame_graph.pack(fill=tk.BOTH, expand=True)

        plt.style.use('ggplot') # change the theme of the graph generated, the theme is available after matplotlib installation

        fig, axs = plt.subplots(3, 1, figsize=(25, 50), constrained_layout=True, sharex=True)
        
        # sales graph
        axs[0].plot(mdates.date2num(dates), total_sales, color='blue')
        axs[0].fill_between(mdates.date2num(dates), 0, total_sales, color='blue', alpha=0.3)
        axs[0].set_title("Total Sales Over Time (All Time)")
        axs[0].set_ylabel("Total Sales")
        axs[0].xaxis.set_major_locator(mdates.YearLocator())
        axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m")) 
        plt.setp(axs[0].get_xticklabels(), rotation=45)

        # cost graph
        axs[1].plot(mdates.date2num(dates), total_cost, color='green')
        axs[1].fill_between(mdates.date2num(dates), 0, total_cost, color='green', alpha=0.3)
        axs[1].set_title("Total Cost Over Time (All Time)")
        axs[1].set_ylabel("Total Cost")
        axs[1].xaxis.set_major_locator(mdates.YearLocator())
        axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.setp(axs[1].get_xticklabels(), rotation=45)

        # gross profit graph
        axs[2].plot(mdates.date2num(dates), gross_profit, color='orange')
        axs[2].fill_between(mdates.date2num(dates), 0, gross_profit, color='orange', alpha=0.3)
        axs[2].set_title("Gross Profit Over Time (All Time)")
        axs[2].set_xlabel("Date")
        axs[2].set_ylabel("Gross Profit")
        axs[2].xaxis.set_major_locator(mdates.YearLocator())
        axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.setp(axs[2].get_xticklabels(), rotation=45)

        graph_canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        graph_canvas.get_tk_widget().pack()

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        graph.mainloop()

    def generateOneYear (self) -> None:
        one_year_ago = datetime.now() - timedelta(days=365)
        one_year_ago = one_year_ago.strftime("%Y-%m-%d")

        self.cur.execute(
            """
                SELECT date, 
                       SUM(dish_amount * dish_price) AS total_sales, 
                       SUM(dish_amount * dish_cost) AS total_cost,
                       SUM(dish_amount * (dish_price - dish_cost)) AS gross_profit  
                FROM kitchen_view
                WHERE 
                date >= ? AND
                serving_stat == "PAID"
                GROUP BY date
                ORDER BY date
            """,(one_year_ago,)
        )

        try:
            result = self.cur.fetchall()
            dates, total_sales, total_cost, gross_profit = zip(*result)
        except ValueError:
            messagebox.showerror("Error", "The sales data is insufficient to generate graphs")
            return
        
        graph = tk.Tk()
        graph.title("Financial Report (Lastest One Year)")
        graph.geometry("1400x800")

        frame_graph = tk.Frame(graph)
        frame_graph.pack(fill=tk.BOTH, expand=True)

        plt.style.use('ggplot') # change the theme of the graph generated, the theme is available after matplotlib installation

        fig, axs = plt.subplots(3, 1, figsize=(25, 50), constrained_layout=True, sharex=True)

        # sales graph
        axs[0].plot(mdates.date2num(dates), total_sales,color='blue')
        axs[0].fill_between(mdates.date2num(dates), 0, total_sales, color='blue', alpha=0.3)
        axs[0].set_title("Total Sales Over Time (Lastest One Year)")
        axs[0].set_ylabel("Total Sales")
        axs[0].xaxis.set_major_locator(mdates.MonthLocator())
        axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m")) 
        plt.setp(axs[0].get_xticklabels(), rotation=45)

        # cost graph
        axs[1].plot(mdates.date2num(dates), total_cost, color='green')
        axs[1].fill_between(mdates.date2num(dates), 0, total_cost, color='green', alpha=0.3)
        axs[1].set_title("Total Cost Over Time (Lastest One Year)")
        axs[1].set_ylabel("Total Cost")
        axs[1].xaxis.set_major_locator(mdates.MonthLocator())
        axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.setp(axs[1].get_xticklabels(), rotation=45)

        # gross profit graph
        axs[2].plot(mdates.date2num(dates), gross_profit, color='orange')
        axs[2].fill_between(mdates.date2num(dates), 0, gross_profit, color='orange', alpha=0.3)
        axs[2].set_title("Gross Profit Over Time (Lastest One Year)")
        axs[2].set_xlabel("Date")
        axs[2].set_ylabel("Gross Profit")
        axs[2].xaxis.set_major_locator(mdates.MonthLocator())
        axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        plt.setp(axs[2].get_xticklabels(), rotation=45)

        graph_canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        graph_canvas.get_tk_widget().pack()

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        graph.mainloop()
    
    def generateOneMonth (self) -> None:
        one_month_ago = datetime.now() - timedelta(days=30)
        one_month_ago = one_month_ago.strftime("%Y-%m-%d")

        self.cur.execute(
            """
                SELECT date, 
                       SUM(dish_amount * dish_price) AS total_sales, 
                       SUM(dish_amount * dish_cost) AS total_cost,
                       SUM(dish_amount * (dish_price - dish_cost)) AS gross_profit  
                FROM kitchen_view
                WHERE 
                date >= ? AND
                serving_stat == "PAID"
                GROUP BY date
                ORDER BY date
            """,(one_month_ago,)
        )

        try:
            result = self.cur.fetchall()
            dates, total_sales, total_cost, gross_profit = zip(*result)
        except ValueError:
            messagebox.showerror("Error", "The sales data is insufficient to generate graphs")
            return
        
        graph = tk.Tk()
        graph.title("Financial Report (Lastest One Month)")
        graph.geometry("1400x800")

        frame_graph = tk.Frame(graph)
        frame_graph.pack(fill=tk.BOTH, expand=True)

        plt.style.use('ggplot') # change the theme of the graph generated, the theme is available after matplotlib installation

        fig, axs = plt.subplots(3, 1, figsize=(25, 50), constrained_layout=True, sharex=True)

        # sales graph
        axs[0].plot(mdates.date2num(dates), total_sales, color='blue')
        axs[0].fill_between(mdates.date2num(dates), total_sales, color='blue', alpha=0.3)
        axs[0].set_title("Total Sales Over Time (Lastest One Month)")
        axs[0].set_ylabel("Total Sales")
        axs[0].xaxis.set_major_locator(mdates.DayLocator())
        axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(axs[0].get_xticklabels(), rotation=45)

        # cost graph
        axs[1].plot(mdates.date2num(dates), total_cost, color='green')
        axs[1].fill_between(mdates.date2num(dates), 0, total_cost, color='green', alpha=0.3)
        axs[1].set_title("Total Cost Over Time (Lastest One Month)")
        axs[1].set_ylabel("Total Cost")
        axs[1].xaxis.set_major_locator(mdates.DayLocator())
        axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(axs[1].get_xticklabels(), rotation=45)

        # gross profit graph
        axs[2].plot(mdates.date2num(dates), gross_profit, color='orange')
        axs[2].fill_between(mdates.date2num(dates), 0, gross_profit, color='orange', alpha=0.3)
        axs[2].set_title("Gross Profit Over Time (Lastest One Month)")
        axs[2].set_xlabel("Date")
        axs[2].set_ylabel("Gross Profit")
        axs[2].xaxis.set_major_locator(mdates.DayLocator())
        axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(axs[2].get_xticklabels(), rotation=45)

        graph_canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        graph_canvas.get_tk_widget().pack()

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        graph.mainloop()

    def generateOneWeek (self) -> None:
        one_week_ago = datetime.now() - timedelta(days=7)
        one_week_ago = one_week_ago.strftime("%Y-%m-%d")

        self.cur.execute(
            """
                SELECT date, 
                       SUM(dish_amount * dish_price) AS total_sales, 
                       SUM(dish_amount * dish_cost) AS total_cost,
                       SUM(dish_amount * (dish_price - dish_cost)) AS gross_profit  
                FROM kitchen_view
                WHERE 
                date >= ? AND
                serving_stat == "PAID"
                GROUP BY date
                ORDER BY date
            """,(one_week_ago,)
        )

        try:
            result = self.cur.fetchall()
            dates, total_sales, total_cost, gross_profit = zip(*result)
        except ValueError:
            messagebox.showerror("Error", "The sales data is insufficient to generate graphs")
            return
        
        graph = tk.Tk()
        graph.title("Financial Report (Lasted One Week)")
        graph.geometry("1200x800")

        frame_graph = tk.Frame(graph)
        frame_graph.pack(fill=tk.BOTH, expand=True)

        plt.style.use('ggplot') # change the theme of the graph generated, the theme is available after matplotlib installation

        fig, axs = plt.subplots(3, 1, figsize=(25, 50), constrained_layout=True, sharex=True)

        # sales graph
        axs[0].plot(mdates.date2num(dates), total_sales, color='blue')
        axs[0].fill_between(mdates.date2num(dates), 0, total_sales, color='blue', alpha=0.3)
        axs[0].set_title("Total Sales Over Time (Lasted One Week)")
        axs[0].set_ylabel("Total Sales")
        axs[0].xaxis.set_major_locator(mdates.DayLocator())
        axs[0].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(axs[0].get_xticklabels(), rotation=45)

        # cost graph
        axs[1].plot(mdates.date2num(dates), total_cost, color='green')
        axs[1].fill_between(mdates.date2num(dates), 0, total_cost, color='green', alpha=0.3)
        axs[1].set_title("Total Cost Over Time (Lasted One Week)")
        axs[1].set_ylabel("Total Cost")
        axs[1].xaxis.set_major_locator(mdates.DayLocator())
        axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(axs[1].get_xticklabels(), rotation=45)

        # gross profit graph
        axs[2].plot(mdates.date2num(dates), gross_profit, color='orange')
        axs[2].fill_between(mdates.date2num(dates), 0, gross_profit, color='orange', alpha=0.3)
        axs[2].set_title("Gross Profit Over Time (Lasted One Week)")
        axs[2].set_xlabel("Date")
        axs[2].set_ylabel("Gross Profit")
        axs[2].xaxis.set_major_locator(mdates.DayLocator())
        axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        plt.setp(axs[2].get_xticklabels(), rotation=45)

        graph_canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        graph_canvas.get_tk_widget().pack()

        canvas = FigureCanvasTkAgg(fig, master=frame_graph)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        graph.mainloop()


    # kitchen interface

    def kitchen (self) -> None:
        self.clearBody()
        self.resetMenu()
        self.menu_kitchen.configure(state = "disable")


        self.tableFrame_pendingOrder = ttk.Labelframe(self.body)
        self.tableFrame_pendingOrder.configure(height=200, labelanchor="n", text='Pending Order:', width=200)
        
        self.pendingOrder_yscroll = ttk.Scrollbar(self.tableFrame_pendingOrder)
        self.pendingOrder_yscroll.configure(orient="vertical")
        self.pendingOrder_yscroll.grid(column=1, row=0, sticky="ns")

        self.table_pendingOrder = ttk.Treeview(self.tableFrame_pendingOrder, yscrollcommand=self.pendingOrder_yscroll.set)
        self.table_pendingOrder.configure(selectmode="browse")
        self.table_pendingOrder.bind('<<TreeviewSelect>>', self.onClick_kitchenPendingTable)
        self.table_pendingOrder.bind('<MouseWheel>', self.table_pendingOrder_mouseWheelScroll)
        self.table_pendingOrder_cols = ['pendingCol_time', 'pendingCol_category', 'pendingCol_ID', 'pendingCol_dishName', 'pendingCol_amount']
        self.table_pendingOrder_dcols = ['pendingCol_time', 'pendingCol_category', 'pendingCol_ID', 'pendingCol_dishName', 'pendingCol_amount']
        self.table_pendingOrder.configure(columns=self.table_pendingOrder_cols,
                                          displaycolumns=self.table_pendingOrder_dcols)
        
        self.table_pendingOrder.column("#0", 
                                       width=0, 
                                       stretch=tk.NO)
        self.table_pendingOrder.column("pendingCol_time", 
                                       anchor="w", 
                                       stretch=True, 
                                       width=80, 
                                       minwidth=20)
        self.table_pendingOrder.column("pendingCol_category",
                                       anchor="w",
                                       stretch=True,
                                       width=100,
                                       minwidth=20)
        self.table_pendingOrder.column("pendingCol_ID",
                                       anchor="w",
                                       stretch=True,
                                       width=30,
                                       minwidth=20)
        self.table_pendingOrder.column("pendingCol_dishName",
                                       anchor="w",
                                       stretch=True,
                                       width=300,
                                       minwidth=20)
        self.table_pendingOrder.column("pendingCol_amount", 
                                       anchor="w", 
                                       stretch=True, 
                                       width=52, 
                                       minwidth=20)
        
        self.table_pendingOrder.heading("pendingCol_time", anchor="center", text='Time')
        self.table_pendingOrder.heading("pendingCol_category", anchor="center", text='Category')
        self.table_pendingOrder.heading("pendingCol_ID", anchor="center", text='ID')
        self.table_pendingOrder.heading("pendingCol_dishName", anchor="center", text='Dish Name')
        self.table_pendingOrder.heading("pendingCol_amount", anchor="w", text='Amount')
        self.table_pendingOrder.grid(column=0, row=0)
        self.tableFrame_pendingOrder.grid(column=1, padx=32, pady="20 30", row=0)
        

        self.tableFrame_readytoserve = ttk.Labelframe(self.body)
        self.tableFrame_readytoserve.configure(height=200, labelanchor="n", text='Ready to Serve:', width=200)
        
        self.readyToServe_yscroll = ttk.Scrollbar(self.tableFrame_readytoserve)
        self.readyToServe_yscroll.configure(orient="vertical")
        self.readyToServe_yscroll.grid(column=1, row=0, sticky="ns")

        self.table_readyToServe = ttk.Treeview(self.tableFrame_readytoserve, yscrollcommand=self.readyToServe_yscroll.set)
        self.table_readyToServe.bind("<<TreeviewSelect>>", self.onClick_kitchenReadyToServeTable)
        self.table_readyToServe.bind('<MouseWheel>', self.table_readyToServe_mouseWheelScroll)
        self.table_readyToServe.configure(selectmode="browse")
        self.table_readyToServe_cols = ['readyCol_time', 'readyCol_category', 'readyCol_ID', 'readycol_dishName', 'readyCol_Amount']
        self.table_readyToServe_dcols = ['readyCol_time', 'readyCol_category', 'readyCol_ID', 'readycol_dishName', 'readyCol_Amount']
        self.table_readyToServe.configure(columns=self.table_readyToServe_cols,
                                          displaycolumns=self.table_readyToServe_dcols)
        
        self.table_readyToServe.column("#0",
                                       width=0,
                                       stretch=tk.NO)
        self.table_readyToServe.column("readyCol_time", 
                                       anchor="w", 
                                       stretch=True, 
                                       width=80, 
                                       minwidth=20)
        self.table_readyToServe.column("readyCol_category",
                                       anchor="w",
                                       stretch=True,
                                       width=100,
                                       minwidth=20)
        self.table_readyToServe.column("readyCol_ID",
                                       anchor="w",
                                       stretch=True,
                                       width=30,
                                       minwidth=20)
        self.table_readyToServe.column("readycol_dishName",
                                       anchor="w",
                                       stretch=True,
                                       width=300,
                                       minwidth=20)
        self.table_readyToServe.column("readyCol_Amount",
                                       anchor="w",
                                       stretch=True,
                                       width=52,
                                       minwidth=20)
        
        self.table_readyToServe.heading("readyCol_time", anchor="center", text='Time')
        self.table_readyToServe.heading("readyCol_category", anchor="center", text='Category')
        self.table_readyToServe.heading("readyCol_ID", anchor="center", text='ID')
        self.table_readyToServe.heading("readycol_dishName", anchor="center", text='Dish Name')
        self.table_readyToServe.heading("readyCol_Amount", anchor="w", text='Amount')
        self.table_readyToServe.grid(column=0, row=0)
        self.tableFrame_readytoserve.grid(column=1, row=1)


        self.frame_statusRelay = ttk.Frame(self.body)
        self.frame_statusRelay.configure(height=200, width=200)

        self.text_time = tk.Text(self.frame_statusRelay)
        self.text_time.configure(background="#c0c0c0", 
                                 font="{Arial} 12 {bold}",
                                 height=1,
                                 state="disabled",
                                 width=18)
        _text_ = 'Time:'
        self.text_time.configure(state="normal")
        self.text_time.insert("0.0", _text_)
        self.text_time.configure(state="disabled")
        self.text_time.grid(column=0, padx="80 5", pady="0 10", row=0)

        self.text_category = tk.Text(self.frame_statusRelay)
        self.text_category.configure(background="#c0c0c0",
                                     font="{Arial} 12 {bold}",
                                     height=1,
                                     state="disabled",
                                     width=18)
        _text_ = 'Category:'
        self.text_category.configure(state="normal")
        self.text_category.insert("0.0", _text_)
        self.text_category.configure(state="disabled")
        self.text_category.grid(column=0, padx="80 5", pady="0 10", row=1)

        self.text_id = tk.Text(self.frame_statusRelay)
        self.text_id.configure(background="#c0c0c0",
                               font="{Arial} 12 {bold}",
                               height=1,
                               state="disabled",
                               width=18)
        _text_ = 'ID:'
        self.text_id.configure(state="normal")
        self.text_id.insert("0.0", _text_)
        self.text_id.configure(state="disabled")
        self.text_id.grid(column=0, padx="80 5", pady="0 10", row=2)

        self.text_dishName = tk.Text(self.frame_statusRelay)
        self.text_dishName.configure(background="#c0c0c0",
                                     font="{Arial} 12 {bold}",
                                     height=1,
                                     state="disabled",
                                     width=18)
        _text_ = 'Dish Name:'
        self.text_dishName.configure(state="normal")
        self.text_dishName.insert("0.0", _text_)
        self.text_dishName.configure(state="disabled")
        self.text_dishName.grid(column=0, padx="80 5", pady="0 10", row=3)

        self.text_amount = tk.Text(self.frame_statusRelay)
        self.text_amount.configure(background="#c0c0c0",
                                   font="{Arial} 12 {bold}",
                                   height=1,
                                   state="disabled",
                                   width=18)
        _text_ = 'Amount:'
        self.text_amount.configure(state="normal")
        self.text_amount.insert("0.0", _text_)
        self.text_amount.configure(state="disabled")
        self.text_amount.grid(column=0, padx="80 5", pady="0 10", row=4)
        
        self.text_changeStatus = tk.Text(self.frame_statusRelay)
        self.text_changeStatus.configure(background="#c0c0c0",
                                         font="{Arial} 12 {bold}",
                                         height=1,
                                         state="disabled",
                                         width=18)
        _text_ = 'Change Status:'
        self.text_changeStatus.configure(state="normal")
        self.text_changeStatus.insert("0.0", _text_)
        self.text_changeStatus.configure(state="disabled")
        self.text_changeStatus.grid(column=0, padx="80 5", pady="10 10", row=5)

        self.time = StringVar()
        self.time.set("")
        self.entry_time = ttk.Entry(self.frame_statusRelay, textvariable=self.time)
        self.entry_time.configure(font="{Arial} 12 {}", width=26)
        self.entry_time.grid(column=1, padx="0 20", pady="0 10", row=0)
        
        self.category = StringVar()
        self.category.set("")
        self.entry_category = ttk.Entry(self.frame_statusRelay, textvariable=self.category)
        self.entry_category.configure(font="{Arial} 12 {}", width=26)
        self.entry_category.grid(column=1, padx="0 20", pady="0 10", row=1)

        self.ID = StringVar()
        self.category.set("")
        self.entry_ID = ttk.Entry(self.frame_statusRelay, textvariable=self.ID)
        self.entry_ID.configure(font="{Arial} 12 {}", width=26)
        self.entry_ID.grid(column=1, padx="0 20", pady="0 10", row=2)
        
        self.dishName = StringVar()
        self.category.set("")
        self.entry_dishName = ttk.Entry(self.frame_statusRelay, textvariable=self.dishName)
        self.entry_dishName.configure(font="{Arial} 12 {}", width=26)
        self.entry_dishName.grid(column=1, padx="0 20", pady="0 10", row=3)
        
        self.amount = StringVar()
        self.category.set("")
        self.entry_amount = ttk.Entry(self.frame_statusRelay, textvariable=self.amount)
        self.entry_amount.configure(font="{Arial} 12 {}", width=26)
        self.entry_amount.grid(column=1, padx="0 20", pady="0 10", row=4)

        self.changeStatus = StringVar(value="Ready to serve")
        __values = ['Ready to serve', 'Pending', 'Served']
        self.status_option = ttk.OptionMenu(self.frame_statusRelay,
                                            self.changeStatus,
                                            "Ready to serve",
                                            *__values,
                                            command=None)
        self.status_option.grid(column=1, row=5, sticky="ew")


        self.button_confirm = ttk.Button(self.frame_statusRelay, command=self.confirmChanges)
        self.button_confirm.configure(text='Confirm')
        self.button_confirm.grid(column=0, columnspan=2, pady="40 0", row=6)

        self.frame_statusRelay.grid(column=0, row=0, rowspan=2)
        self.button_refresh = ttk.Button(self.body, command=self.kitchen)
        self.button_refresh.configure(text='Refresh')
        self.button_refresh.grid(column=1, pady="20 30", row=2)
        self.body.grid(column=0, ipady=41, row=2, sticky="n")

        self.updateReserveKitchenSQL()
        self.buildKitchenPendingTable()
        self.buildKitchenReadyToServeTable()

    # kitchen body

    def table_pendingOrder_mouseWheelScroll (self, event) -> None:
        self.table_pendingOrder.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def table_readyToServe_mouseWheelScroll (self, event) -> None:
        self.table_readyToServe.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def onClick_kitchenPendingTable (self, event) -> None:
        cur = self.table_pendingOrder.selection()
        cur = self.table_pendingOrder.item(cur)
        list = cur['values']
        if (len(list) == 5):
            self.time.set(list[0])
            self.category.set(list[1])
            self.ID.set(list[2])
            self.dishName.set(list[3])
            self.amount.set(list[4])

    def onClick_kitchenReadyToServeTable (self, event) -> None:
        cur = self.table_readyToServe.selection()
        cur = self.table_readyToServe.item(cur)
        list = cur['values']
        if (len(list) == 5):
            self.time.set(list[0])
            self.category.set(list[1])
            self.ID.set(list[2])
            self.dishName.set(list[3])
            self.amount.set(list[4])

    def updateReserveKitchenSQL (self) -> None:

        # query food reservation 30 minutes ago and insert into reserve_kitchen table

        today = datetime.now().strftime('%Y-%m-%d')
        current_datetime = datetime.now()
        time_30_minutes_ago = current_datetime - timedelta(minutes=30)
        time_30_minutes_ago = time_30_minutes_ago.strftime('%H:%M')

        self.cur.execute(
            """
                SELECT r.id, 
                       r.reserve_time, 
                       rd.dish_id, 
                       rd.dish_amount
                FROM reservation r 
                JOIN reserve_dish rd ON r.id = rd.reserve_id
                WHERE r.reserve_date = ? AND
                      r.reserve_time >= ?
            """, (today, time_30_minutes_ago)
        )
        
        result = self.cur.fetchall()
        
        # verify existance of obtained reserve_id in reserve_kitchen table
        # to prevent duplicated insertion, and infinite duplication upon refresh 

        reserve_id = list(zip(*result))

        try:
            reserve_id = list(reserve_id[0])
        except IndexError:
            messagebox.showinfo("No order", "No order available")
            return

        reserve_id = list(set(reserve_id))

        check_reserve_id = []
        for id in reserve_id:
            self.cur.execute(
                """
                    SELECT reserve_id FROM reserve_kitchen 
                    WHERE reserve_id = ?
                """, (id,)
            )
            check_reserve_id.append(list(set(self.cur.fetchall())))

        # to get the first reserve_id only (among the duplicated id)
        check_reserve_id = [item[0] for sublist in check_reserve_id for item in sublist]
        
        # make the checking compatible for both single and multiple food reserve order
        try: 
            check_reserve_id = check_reserve_id[0][0]
        except IndexError:
            try: 
                check_reserve_id = check_reserve_id[0]
            except IndexError:
                pass
        except TypeError:
            pass

        if (reserve_id == check_reserve_id) :
            return
        else:
            pass

        for row in result:
            self.cur.execute(
                """
                    INSERT INTO reserve_kitchen (reserve_id, time, dish_id, dish_amount) VALUES
                    (?,?,?,?)
                """, (row[0], row[1], row[2], row[3])
            )
        self.conn.commit()


    def buildKitchenPendingTable (self) -> None:
        self.cur.execute(
            """
                SELECT SUBSTR(time, 1, 5), 
                       serve_type, 
                       ID, 
                       dish_name, 
                       dish_amount
                FROM kitchen_view
                WHERE serving_stat = 'PENDING'
            """
        )
        result = self.cur.fetchall()

        for row in result:
            self.table_pendingOrder.insert("", tk.END, values=row)

    def buildKitchenReadyToServeTable (self) -> None:
        self.cur.execute(
            """
                SELECT time, serve_type, ID, dish_name, dish_amount FROM kitchen_view
                WHERE serving_stat = 'READY TO SERVE'
            """
        )
        result = self.cur.fetchall()

        for row in result:
            self.table_readyToServe.insert("", tk.END, values=row)

    def confirmChanges (self) -> None:
        time = self.time.get()
        category = self.category.get()
        id = self.ID.get()
        dishName = self.dishName.get()
        amount = self.amount.get()

        if not time or not category or not id or not dishName or not amount:
            messagebox.showerror("Error", "Please fill in the required information")
            return
        else:
            self.changeServingStatus()
            messagebox.showinfo("Status Changed Successfully", "The change on the serving status is complete")
            self.kitchen()

    def changeServingStatus (self) -> None:
        time = self.time.get()
        category = self.category.get()
        id = self.ID.get()
        dishName = self.dishName.get()
        amount = self.amount.get()
        status = self.changeStatus.get().upper()

        if category == 'RESERVE':
            self.cur.execute(
                """
                    UPDATE reserve_kitchen SET serving_stat = ?
                    WHERE time = ? AND
                          reserve_id = ? AND
                          dish_id = (SELECT dish_id from dish_list WHERE dish_name = ?) AND
                          dish_amount = ? 
                """, (status, time, id, dishName, amount)
            )
            if status == "SERVED": # assume the customer has made the payment after the dish is served
                self.cur.execute(
                    """
                        UPDATE reserve_dish SET payment_status = 'PAID'
                        WHERE reserve_id = ? AND
                              dish_id = (SELECT dish_id from dish_list WHERE dish_name = ?)
                    """, (id, dishName)
                )
        elif category == 'DINE IN':
            self.cur.execute(
                """
                    UPDATE dineIn_kitchen SET serving_stat = ?
                    WHERE time = ? AND
                          order_id = ? AND
                          dish_id = (SELECT dish_id from dish_list WHERE dish_name = ?) AND
                          dish_amount = ? 
                """, (status, time, id, dishName, amount)
            )
            if status == "SERVED": # assume the customer has made the payment after the dish is served
                self.cur.execute(
                    """
                        UPDATE dineIn_cashier SET payment_status = 'PAID'
                        WHERE order_id = ? AND
                              dish_id = (SELECT dish_id from dish_list WHERE dish_name = ?) AND
                              dish_amount = ?
                    """, (id, dishName, amount)
                )
        
        self.conn.commit()


    # table management body

    def table_management (self) -> None:
        self.clearBody()
        self.resetMenu()
        self.menu_tables.configure(state = "disable")
        

        self.tableFrame_tableAvail = ttk.Labelframe(self.body)
        self.tableFrame_tableAvail.configure(height=200, labelanchor="n", text='Table Available', width=200)

        self.tableAvail_yscroll = ttk.Scrollbar(self.tableFrame_tableAvail)
        self.tableAvail_yscroll.configure(orient="vertical")
        self.tableAvail_yscroll.grid(column=1, row=0, sticky="ns")

        self.table_tableAvail = ttk.Treeview(self.tableFrame_tableAvail, yscrollcommand=self.tableAvail_yscroll.set)
        self.table_tableAvail.configure(selectmode="browse")
        self.table_tableAvail_cols = ["tableAvailCol_ID",'tableAvailCol_capacity']
        self.table_tableAvail_dcols = ["tableAvailCol_ID",'tableAvailCol_capacity']
        self.table_tableAvail.configure(columns=self.table_tableAvail_cols,
                                        displaycolumns=self.table_tableAvail_dcols)
        self.table_tableAvail.column("#0",
                                     width=0,
                                     stretch=tk.NO)
        self.table_tableAvail.column("tableAvailCol_ID",
                                     anchor="center",
                                     stretch=True,
                                     width=20,
                                     minwidth=20)
        self.table_tableAvail.column("tableAvailCol_capacity",
                                     anchor="center",
                                     stretch=True,
                                     width=200,
                                     minwidth=20)
        
        self.table_tableAvail.heading("tableAvailCol_ID", anchor="center", text='ID')
        self.table_tableAvail.heading("tableAvailCol_capacity", anchor="center", text='Capacity')
        self.table_tableAvail.grid(column=0, row=0)
        self.tableFrame_tableAvail.grid(column=0, padx="286 50", pady="20 30", row=0)
        

        self.tableFrame_tableInUse = ttk.Labelframe(self.body)
        self.tableFrame_tableInUse.configure(height=200, labelanchor="n", text='Table In Use', width=200)
        
        self.tableInUse_yscroll = ttk.Scrollbar(self.tableFrame_tableInUse)
        self.tableInUse_yscroll.configure(orient="vertical")
        self.tableInUse_yscroll.grid(column=1, row=0, sticky="ns")

        self.table_tableInUse = ttk.Treeview(self.tableFrame_tableInUse, yscrollcommand=self.tableInUse_yscroll.set)
        self.table_tableInUse.configure(selectmode="browse")
        self.table_tableInUse_cols = ['tableInUseCol_ID','tableInUseCol_capacity']
        self.table_tableInUse_dcols = ['tableInUseCol_ID','tableInUseCol_capacity']
        self.table_tableInUse.configure(columns=self.table_tableInUse_cols, 
                                        displaycolumns=self.table_tableInUse_dcols)
        self.table_tableInUse.column("#0", 
                                     width=0,
                                     stretch=tk.NO)
        self.table_tableInUse.column("tableInUseCol_ID", 
                                     anchor="center",
                                     stretch=True,
                                     width=20,
                                     minwidth=20)
        self.table_tableInUse.column("tableInUseCol_capacity",
                                     anchor="center",
                                     stretch=True,
                                     width=200,
                                     minwidth=20)
        
        self.table_tableInUse.heading("tableInUseCol_ID", anchor="center", text='ID')
        self.table_tableInUse.heading("tableInUseCol_capacity", anchor="center", text='Capacity')
        self.table_tableInUse.grid(column=0, row=0)
        self.tableFrame_tableInUse.grid(column=1, padx="50 286", pady="20 30", row=0)
        

        self.button_refresh = ttk.Button(self.body, command=self.table_management)
        self.button_refresh.configure(text='Refresh')
        self.button_refresh.grid(column=0, columnspan=2, pady="0 20", row=2)
        self.body.grid(column=0, ipady=175, row=2, sticky="n")

        self.buildTableAvailableTable()
        self.buildTableInUseTable()

    # table management functions

    def buildTableAvailableTable (self) -> None:
        today = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')
        
        self.cur.execute(
            """
                SELECT table_id FROM table_inUse_view
                WHERE date = ? AND
                      time <= ? AND
                      end_time >= ?
            """, (today, current_time, current_time)
        )

        result = self.cur.fetchall()
        table_inUse = [row[0] for row in result]

        tableidALL = list(range(1, 11))
        available_tables = []

        for table_id in tableidALL:
            if table_id not in table_inUse:
                available_tables.append(table_id)
        
        result = []
        for table_id in available_tables:
            self.cur.execute(
                """
                SELECT table_id, table_capacity FROM table_list
                WHERE table_id = ?
                """, (table_id,)
            )
            result.append(self.cur.fetchall())
        
        result = [item for inner_list in result for item in inner_list] # remove inner list, original nested

        for row in result:
            self.table_tableAvail.insert("", tk.END, values=row)
    
    def buildTableInUseTable (self) -> None:
        today = datetime.now().strftime('%Y-%m-%d')
        current_time = datetime.now().strftime('%H:%M:%S')
        
        self.cur.execute(
            """
                SELECT table_id FROM table_in_use 
                WHERE date = ? AND
                      start_time <= ? AND
                      end_time >= ?
            """, (today, current_time, current_time)
        )

        result = self.cur.fetchall()
        table_inUse = [row[0] for row in result]

        result = []
        for table_id in table_inUse:
            self.cur.execute(
                """
                SELECT table_id, table_capacity FROM table_list
                WHERE table_id = ?
                """, (table_id,)
            )
            result.append(self.cur.fetchone())

        for row in result:
            self.table_tableInUse.insert("", tk.END, values=row)

# for individual module testing
if __name__ == "__main__":
    app = adminInterface()
    app.run()