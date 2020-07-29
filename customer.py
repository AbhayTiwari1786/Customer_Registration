from tkinter import *
from tkinter import ttk
import pymysql
import sys


class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title("NIRMAL HOMESTAY KAINCHI DHAM (BHOWALI) DISTRICT NAINITAL UTTRAKHAND -263132",)
        self.root.geometry("2000x1500+0+0")

        title = Label(self.root, text="Electronic Register", bd=10, relief="sunken",
                      font=("times new roman", 20, "bold"), bg="grey", fg="white")
        title.pack(side=TOP, fill="x")

        # ================ALL Variables=========================================
        self.Customer_Id_var = StringVar()
        self.Id_Type_var = StringVar()
        self.Arrival_Date_var = StringVar()
        self.Customer_Name_var = StringVar()
        self.Customer_Address_var = StringVar()
        self.Phone_No_var = StringVar()
        self.Nationality_var = StringVar()
        self.Coming_From_var = StringVar()
        self.Back_To_var = StringVar()
        self.No_Of_Occupants_var = StringVar()
        self.Date_Of_Departure_var = StringVar()
        self.Vehicle_No_var = StringVar()
        self.Room_No_var = StringVar()
        self.Room_Rent_var = StringVar()
        self.Advance_var = StringVar()
        self.Remarks_var = StringVar()
        self.searchBy_var = StringVar()
        self.searchtxt_var = StringVar()
        # ===========================================================================================================

        Details_Frame = Frame(self.root, bd=4, relief="sunken", bg="grey")
        Details_Frame.place(x=20, y=70, width=500, height=600)
        D_title = Label(Details_Frame, text="Customer Registration", font=("times new roman", 20, "bold"), fg="White",
                        bg="grey")
        D_title.grid(row=0, columnspan=2, pady=20)

        Customer_ID = Label(Details_Frame, text="Customer_Id :-", font=("times new roman", 15, "bold"), fg="white",
                            bg="grey")
        Customer_ID.grid(row=1, column=0, sticky="w")
        txt_ID = Entry(Details_Frame, textvariable=self.Customer_Id_var, font=("times new roman", 10, "bold"),
                       bd=3, relief="sunken")
        txt_ID.grid(row=1, column=1)

        Id_type = Label(Details_Frame, text="Id_Type :-", font=("times new roman", 15, "bold"), fg="white",
                            bg="grey")
        Id_type.grid(row=2, column=0, sticky="w")
       
        Id_type = ttk.Combobox(Details_Frame,textvariable=self.Id_Type_var ,text="Id_Type :-", font=("times new roman", 10, "bold"),
                                    state='readonly')
        Id_type['values'] = ("AdhaarCard", "Election Id", "Driving License","Pan Card")
        Id_type.grid(row=2, column=1, padx=20, pady=10)


        Arrival_Date = Label(Details_Frame, text="Arrival_Date :-", font=("times new roman", 15, "bold"), fg="white",
                             bg="grey")
        Arrival_Date.grid(row=3, column=0, sticky="w")
        txt_Arrival = Entry(Details_Frame, textvariable=self.Arrival_Date_var, font=("times new roman", 10, "bold"),
                            bd=3, relief="sunken")
        txt_Arrival.grid(row=3, column=1)

        Customer_Name = Label(Details_Frame, text="Customer_Name :-", font=("times new roman", 15, "bold"), fg="white",
                              bg="grey")
        Customer_Name.grid(row=4, column=0, sticky="w")
        txt_Name = Entry(Details_Frame, textvariable=self.Customer_Name_var, font=("times new roman", 10, "bold"), bd=3,
                         relief="sunken")
        txt_Name.grid(row=4, column=1)

        Customer_Address = Label(Details_Frame, text="Customer_Address :-", font=("times new roman", 15, "bold"),
                                 fg="white", bg="grey")
        Customer_Address.grid(row=5, column=0, sticky="w")
        txt_Address = Entry(Details_Frame, textvariable=self.Customer_Address_var, font=("times new roman", 10, "bold"),
                            bd=3, relief="sunken")
        txt_Address.grid(row=5, column=1)

        Phone_No = Label(Details_Frame, text="Phone_No :-", font=("times new roman", 15, "bold"),
                         fg="white", bg="grey")
        Phone_No.grid(row=6, column=0, sticky="w")
        txt_Phone = Entry(Details_Frame, textvariable=self.Phone_No_var, font=("times new roman", 10, "bold"), bd=3,
                          relief="sunken")
        txt_Phone.grid(row=6, column=1)

        Nationality = Label(Details_Frame, text="Nationality :-", font=("times new roman", 15, "bold"), fg="white",
                            bg="grey")
        Nationality.grid(row=7, column=0, sticky="w")
        txt_Nationality = Entry(Details_Frame, textvariable=self.Nationality_var, font=("times new roman", 10, "bold"),
                                bd=3, relief="sunken")
        txt_Nationality.grid(row=7, column=1)

        Coming_From = Label(Details_Frame, text="Coming_From :-", font=("times new roman", 15, "bold"),
                            fg="white", bg="grey")
        Coming_From.grid(row=8, column=0, sticky="w")
        txt_Coming = Entry(Details_Frame, textvariable=self.Coming_From_var, font=("times new roman", 10, "bold"), bd=3,
                           relief="sunken")
        txt_Coming.grid(row=8, column=1)

        Back_To = Label(Details_Frame, text="Back_To :-", font=("times new roman", 15, "bold"),
                        fg="white", bg="grey")
        Back_To.grid(row=9, column=0, sticky="w")
        txt_Return = Entry(Details_Frame, textvariable=self.Back_To_var, font=("times new roman", 10, "bold"), bd=3,
                           relief="sunken")
        txt_Return.grid(row=9, column=1)

        No_Of_Occupants = Label(Details_Frame, text="No_Of_Occupants :-", font=("times new roman", 15, "bold"),
                                fg="white", bg="grey")
        No_Of_Occupants.grid(row=10, column=0, sticky="w")
        txt_Occupants = Entry(Details_Frame, textvariable=self.No_Of_Occupants_var,
                              font=("times new roman", 10, "bold"), bd=3, relief="sunken")
        txt_Occupants.grid(row=10, column=1)

        Departure_Date = Label(Details_Frame, text="Departure_Date :-", font=("times new roman", 15, "bold"),
                               fg="white", bg="grey")
        Departure_Date.grid(row=11, column=0, sticky="w")
        txt_Departure = Entry(Details_Frame, textvariable=self.Date_Of_Departure_var,
                              font=("times new roman", 10, "bold"), bd=3, relief="sunken")
        txt_Departure.grid(row=11, column=1)

        Vehicle_No = Label(Details_Frame, text="Vechile_No :-", font=("times new roman", 15, "bold"),
                           fg="white", bg="grey")
        Vehicle_No.grid(row=12, column=0, sticky="w")
        txt_Vechile = Entry(Details_Frame, textvariable=self.Vehicle_No_var, font=("times new roman", 10, "bold"), bd=3,
                            relief="sunken")
        txt_Vechile.grid(row=12, column=1)

        Room_No = Label(Details_Frame, text="Room_No :-", font=("times new roman", 15, "bold"),
                        fg="white", bg="grey")
        Room_No.grid(row=13, column=0, sticky="w")
        txt_Room = Entry(Details_Frame, textvariable=self.Room_No_var, font=("times new roman", 10, "bold"), bd=3,
                         relief="sunken")
        txt_Room.grid(row=13, column=1)

        Room_Rent = Label(Details_Frame, text="Room_Rent :-", font=("times new roman", 15, "bold"),
                          fg="white", bg="grey")
        Room_Rent.grid(row=14, column=0, sticky="w")
        txt_Rent = Entry(Details_Frame, textvariable=self.Room_Rent_var, font=("times new roman", 10, "bold"), bd=3,
                         relief="sunken")
        txt_Rent.grid(row=14, column=1)

        Advance = Label(Details_Frame, text="Advance :-", font=("times new roman", 15, "bold"),
                        fg="white", bg="grey")
        Advance.grid(row=15, column=0, sticky="w")
        txt_Advance = Entry(Details_Frame, textvariable=self.Advance_var, font=("times new roman", 10, "bold"), bd=3,
                            relief="sunken")
        txt_Advance.grid(row=15, column=1)

        Remarks = Label(Details_Frame, text="Remarks :-", font=("times new roman", 15, "bold"),
                        fg="white", bg="grey")
        Remarks.grid(row=16, column=0, sticky="w")
        txt_Remarks = Entry(Details_Frame, textvariable=self.Remarks_var, font=("times new roman", 10, "bold"), bd=3,
                            relief="sunken")
        txt_Remarks.grid(row=16, column=1)

        btn_Frame = Frame(Details_Frame, bd=4, relief="sunken", bg="white")
        btn_Frame.place(x=10, y=550, width=470, height=32)

        Addbtn =    Button(btn_Frame, text="Add", width=15, command=self.add_Customer,
                        font=("times new roman", 10, "bold")).grid(row=18, column=1)
        Updatebtn = Button(btn_Frame, text="Update", width=15,command =self.Update_Data,
                           font=("times new roman", 10, "bold")).grid(row=18,
                                                                      column=2)
        Deletebtn = Button(btn_Frame, text="Delete", width=15,command=self.delete_data,font=("times new roman", 10, "bold")).grid(row=18,
                                                                                                          column=3)
        Clearbtn =  Button(btn_Frame, text="Clear", width=15, command=self.clear,
                          font=("times new roman", 10, "bold")).grid(row=18,
                                                                     column=4)

        Record_Frame = Frame(self.root, bd=4, relief="ridge", bg="grey")
        Record_Frame.place(x=600, y=70, width=700, height=560)

        lbl_search = Label(Record_Frame, text="Search By", font=("times new roman", 15, "bold"), bg="grey", fg="white")
        lbl_search.grid(row=0, column=0, sticky="w", pady=20)

        combo_search = ttk.Combobox(Record_Frame,textvariable=self.searchBy_var ,text="Search By", font=("times new roman", 10, "bold"),
                                    state='readonly')
        combo_search['values'] = ("Phone_No", "Name", "City")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Record_Frame,textvariable=self.searchtxt_var,font=("times new roman", 10, "bold"), bd=3, relief="sunken")
        txt_search.grid(row=0, column=2)

        Search_btn = Button(Record_Frame, text="Search",command=self.search_data,width=10, font=("times new roman", 10, "bold")).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=15,
                                                                                                              pady=10)
        ShowAll_btn = Button(Record_Frame, text="Show All",command=self.fetch_data ,width=10,font=("times new roman", 10, "bold")).grid(row=0,
                                                                                                                 column=4,
                                                                                                                 padx=15,
                                                                                                                 pady=10)

        Table_Frame = Frame(Record_Frame, bd=4, relief="ridge", bg="grey")
        Table_Frame.place(x=10, y=70, width=675, height=430, )

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Customer_table = ttk.Treeview(Table_Frame, columns=("Customer_Id","Id_Type",
                                                                 "Arrival_Date", "Customer_Name", "Customer_Address",
                                                                 "Phone_No", "Nationality", "Coming_From", "Back_To",
                                                                 "No_Of_Occupants", "Departure_Date", "Vehicle_No",
                                                                 "Room_No", "Room_Rent", "Advance", "Remarks"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Customer_table.xview)
        scroll_y.config(command=self.Customer_table.yview)

        self.Customer_table.heading("Customer_Id", text="Customer_Id")
        self.Customer_table.heading("Id_Type", text ="Id_Type")

        self.Customer_table.heading("Arrival_Date", text="Arrival_Date")
        self.Customer_table.heading("Customer_Name", text="Customer_Name")
        self.Customer_table.heading("Customer_Address", text="Address")
        self.Customer_table.heading("Phone_No", text="Phone_No")
        self.Customer_table.heading("Nationality", text="Nationality")
        self.Customer_table.heading("Coming_From", text="Coming_From")
        self.Customer_table.heading("Back_To", text="Back_To")
        self.Customer_table.heading("No_Of_Occupants", text="No_Of_Occupants")
        self.Customer_table.heading("Departure_Date", text="Departure_Date")
        self.Customer_table.heading("Vehicle_No", text="Vehicle_No")
        self.Customer_table.heading("Room_No", text="Room_No")
        self.Customer_table.heading("Room_Rent", text="Room_Rent")
        self.Customer_table.heading("Advance", text="Advance")
        self.Customer_table.heading("Remarks", text="Remarks")

        self.Customer_table['show'] = 'headings'

        self.Customer_table.column("Customer_Id", width=130)
        self.Customer_table.column("Id_Type",width=100)
        self.Customer_table.column("Arrival_Date",width=100)
        self.Customer_table.column("Customer_Name", width=150)
        self.Customer_table.column("Customer_Address", width=250)
        self.Customer_table.column("Phone_No", width=100)
        self.Customer_table.column("Nationality", width=100)
        self.Customer_table.column("Coming_From", width=100)
        self.Customer_table.column("Back_To", width=100)
        self.Customer_table.column("No_Of_Occupants", width=100)
        self.Customer_table.column("Departure_Date", width=100)
        self.Customer_table.column("Vehicle_No", width=100)
        self.Customer_table.column("Room_No", width=100)
        self.Customer_table.column("Room_Rent", width=100)
        self.Customer_table.column("Advance", width=100)
        self.Customer_table.column("Remarks", width=100)

        self.Customer_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.Customer_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_Customer(self):
        conn = pymysql.connect(host="localhost", user="root", password="", db="abhay")
        cur = conn.cursor()
        cur.execute(" Insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.Customer_Id_var.get(),
                     self.Id_Type_var.get(),
                     self.Arrival_Date_var.get(),
                     self.Customer_Name_var.get(),
                     self.Customer_Address_var.get(),
                     self.Phone_No_var.get(),

                     self.Nationality_var.get(),
                     self.Coming_From_var.get(),
                     self.Back_To_var.get(),
                     self.No_Of_Occupants_var.get(),
                     self.Date_Of_Departure_var.get(),

                     self.Vehicle_No_var.get(),
                     self.Room_No_var.get(),
                     self.Room_Rent_var.get(),
                     self.Advance_var.get(),
                     self.Remarks_var.get()))

        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", db="abhay")
        cur = conn.cursor()
        cur.execute("select * from register")
        rows = cur.fetchall()

        # if len(rows) != 0:
        # self.Customer_table.delete(self.Customer_table.get_children())
        for row in rows:
            self.Customer_table.insert('', END, values=row)

            conn.commit()
        conn.close()

    def clear(self):
        self.Customer_Id_var.set("")
        self.Id_Type_var.set("")
        self.Arrival_Date_var.set("")
        self.Customer_Name_var.set("")
        self.Customer_Address_var.set("")
        self.Phone_No_var.set("")
        self.Nationality_var.set("")
        self.Coming_From_var.set("")
        self.Back_To_var.set("")
        self.No_Of_Occupants_var.set("")
        self.Date_Of_Departure_var.set("")
        self.Vehicle_No_var.set("")
        self.Room_No_var.set("")
        self.Room_Rent_var.set("")
        self.Advance_var.set("")
        self.Remarks_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.Customer_table.focus()
        content = self.Customer_table.item(cursor_row)
        row = content['values']
        # print(row)

        self.Customer_Id_var.set(row[0])
        self.Id_Type_var.set(row[1])
        self.Arrival_Date_var.set(row[2])
        self.Customer_Name_var.set(row[3])
        self.Customer_Address_var.set(row[4])
        self.Phone_No_var.set(row[5])
        self.Nationality_var.set(row[6])
        self.Coming_From_var.set(row[7])
        self.Back_To_var.set(row[8])
        self.No_Of_Occupants_var.set(row[9])
        self.Date_Of_Departure_var.set(row[10])
        self.Vehicle_No_var.set(row[11])
        self.Room_No_var.set(row[12])
        self.Room_Rent_var.set(row[13])
        self.Advance_var.set(row[14])
        self.Remarks_var.set(row[15])

    def Update_Data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", db="abhay")
        cur = conn.cursor()
        cur.execute("UPDATE register SET  Id_Type=%s ,Date_Of_Arrival=%s,"
                    "Customer_Name=%s,Customer_Address=%s,Phone_No=%s,Nationality=%s,Coming_From=%s,"
                    "Back_To=%s,No_Of_Occupants=%s,Date_Of_Departure=%s,Vehicle_No=%s,Room_No=%s," 
                    "Room_Rent=%s,Advance=%s,Remarks=%s WHERE Customer_Id=%s",
                                                                    ( 
                                                                        
                                                                      self.Arrival_Date_var.get(),
                                                                                                                                                                                                                                                                                    self.Customer_Name_var.get(),
                                                                      self.Customer_Address_var.get(),
                                                                      self.Id_Type_var.get(),
                                                                      self.Phone_No_var.get(),
                                                                      self.Nationality_var.get(),
                                                                      self.Coming_From_var.get(),
                                                                      self.Back_To_var.get(),
                                                                      self.No_Of_Occupants_var.get(),
                                                                      self.Date_Of_Departure_var.get(),
                                                                      self.Vehicle_No_var.get(),
                                                                      self.Room_No_var.get(),
                                                                      self.Room_Rent_var.get(),
                                                                      self.Advance_var.get(),
                                                                      self.Remarks_var.get(),
                                                                      self.Customer_Id_var.get()))

        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

    def delete_data(self):
         conn = pymysql.connect(host="localhost", user="root", password="", db="abhay")
         cur = conn.cursor()
         cur.execute("delete from register where Customer_Id =%s",(self.Customer_Id_var.get()))
         conn.commit()
         conn.close()
         self.fetch_data()
         self.clear()

    def search_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="", db="abhay")
        cur = conn.cursor()
        cur.execute("select * from register where"+str(self.searchBy_var.get())+"like %'"+str(self.searchtxt_var.get()),"%'")
        rows = cur.fetchall()
        
        # if len(rows)!= 0:
            # self.Customer_table.delete(+self.Customer_table.get_children())
        for row in rows:
            self.Customer_table.insert('', END, values=row)

            conn.commit()
        conn.close()
    


root = Tk()
obj = Customer(root)
root.mainloop()
