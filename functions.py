import mysql.connector as tarush
from random import *
import datetime
date_t = datetime.datetime.now()

date_t = datetime.datetime.now()


def login(a, b):
    global phone
    global user_id
    phone = a
    password = b
    p = "@@".join(password)
    if len(str(phone)) == 10 or len(str(password)) >= 8:
        try:
            sql = "SELECT * FROM user_info WHERE phone={} and pass='{}'".format(
                phone, p)
            cursor.execute(sql)
            a = cursor.fetchone()
            user_id = a[0]
            data = cursor.rowcount
            if data == 1:
                main()
            else:
                print("\nIncorrect details\n--------------")
                # login()
        except:
            print("\nError Occured. Your details may be incorrect.\n--------------")
            # log_sign()
    else:
        print("Invalid pnone number login again\n------------")
        # login()
# print("<----------DBMS Project------------>")
# l1 = ['Banglore', 'Delhi', 'Mumbai', 'Banglore']


# def password():
#     password = input("Enter new strong password : ")
#     p = "@@".join(password)
#     if len(password) >= 8:
#         try:
#             sql = "UPDATE user_info set pass=%s WHERE id=%s"
#             values = (p, user_id)
#             cursor.execute(sql, values)
#             conn.commit()
#             print("Password Updated\n------------------")
#         except:
#             print("Error Occured")
#             main()
#     else:
#         print("password less than 8 is not allowed.\n---------------")
#         main()


# def update_phone():
#     updated_phone = int(input("Enter 10 Digit new Phone : "))
#     if len(str(updated_phone)) == 10:
#         try:
#             sql = "UPDATE user_info set phone=%s WHERE id=%s"
#             values = (updated_phone, user_id)
#             cursor.execute(sql, values)
#             conn.commit()
#             print("Phone Number Updated. Please Login Again.\n------------------")
#             login()
#         except mysql.connector.Error as e:
#             print(e)
#             main()
#     else:
#         print("password less than 8 is not allowed.\n")
#         main()


# def book():
#     print("\n", l1)
#     srt_point = input("Enter the starting point from the above list : ")
#     end_point = input("Enter the Ending point from the above list : ")

#     number = int(input("Enter the number of ticket you want to book : "))
#     date = input("Enter date of journer : ")
#     month = input("Enter month of journey: ")
#     j_date = date + "-" + month

#     for i in range(1, number+1):
#         today_date = datetime.datetime.now()
#         name = input("Enter Passanger name  : ")
#         age = int(input("Enter Passanger age : "))
#         try:
#             sql = "INSERT INTO book_ticket (name,age,starting_point,end_point,phone,user_id,book_date,j_date) VALUES ('{}',{},'{}','{}',{},{},'{}','{}')".format(
#                 name, age, srt_point, end_point, phone, user_id, date_t, j_date)
#             cursor.execute(sql)
#             conn.commit()
#             print(i, " *** Ticket has been REGISTERED THANK YOU VIST AGAIN ***\n")
#         except exception as e:
#             print(e)
#     main()


# def cancel():
#     print("Go to view ticket section to know your ticket id.\n--------------------")
#     try:
#         sql = "SELECT * FROM book_ticket WHERE phone={} and user_id={}".format(
#             phone, user_id)
#         cursor.execute(sql)
#         a = cursor.fetchall()
#         for result in a:
#             print(result)
#         if cursor.rowcount >= 1:
#             try:
#                 idd = int(input("How many tickets you want to delete : "))
#                 for i in range(1, idd+1):
#                     ticket_id = int(input("Enter the ticket id : "))
#                     s = "DELETE FROM book_ticket where id={}".format(ticket_id)
#                     cursor.execute(s)
#                     conn.commit()
#                     print("1 ticket canceled")
#                 main()
#             except:
#                 print("Error while canceling the ticket")
#                 main()
#         else:
#             print("No tickets are regestered \n")
#     except:
#         print("Rendering ..")
#         main()


# def update():
#     user_ch_3 = int(
#         input("Enter 1 for phone and 2 for password to change another key to exit: "))

#     if user_ch_3 == 1:
#         update_phone()
#     elif user_ch_3 == 2:
#         password()
#     else:
#         print("Something went wrong...\n-------------")
#         main()


# def enquiry():
#     print("The section still left to design.\n-----------")
#     main()


# def view():
#     try:
#         sql = "SELECT * FROM book_ticket WHERE phone={} and user_id={}".format(
#             phone, user_id)
#         cursor.execute(sql)
#         row = cursor.rowcount
#         while True:
#             a = cursor.fetchone()
#             print("Ticket ID : ", a[0], "\nName : ", a[1], "\nAge : ", a[2], "\nStarting Station : ", a[3],
#                   "\nEnd Station : ", a[4], "\nBooking Date : ", a[7], "\nJourney Date : ", a[8], "\n---------------------")
#         print("IGNORE THE RENDERING MESSAGE")
#     except:
#         print("Rendering the Process ..")
#         main()


# def delete():
#     try:
#         cursor = conn.cursor()
#         sql = "DELETE FROM user_info where id={}".format(user_id)
#         cursor.execute(sql)
#         conn.commit()
#         print("Account Deleted")
#         log_sign()
#     except:
#         print("Rendering to delete your account.")

#     main()


# def generate():
#     print("You can generate one ticket at one time.Please visit this section with your ticket id.\n-------------")
#     no_of_tkt = input("Enter the number of ticket you want to generate : ")
#     for i in range(1, int(no_of_tkt)+1):
#         tkt_id = int(input("Enter the ticket id : "))
#         sql = "SELECT * FROM book_ticket WHERE id={}".format(tkt_id)
#         cursor.execute(sql)
#         a = cursor.fetchone()
#         iid = a[0]
#         name = a[1]
#         age = a[2]
#         st_p = a[3]
#         ed_p = a[4]
#         x = str(iid)
#         j_d = a[8]
#         b_d = a[7]
#         try:
#             file = open("Rail_Ticket_"+x+".txt", "w")
#             file.write("<-----------********----------->\nNOTE:-->Don't try to make a fake ticket. Tc will get to know if the ticket is fake or real.\nTicket id : "+x +
#                        "\nName : "+name+"\nAge : "+str(age)+"\nFrom : "+st_p+"\nTo :"+ed_p+"\nJourney Date :"+j_d+"\nBooking Date :"+b_d+"\n<--------------************------------->")
#             file.close()
#             print(i, " ticket generated as Rail_Ticket_"+x+".txt\n")

#         except:
#             print("Ticket not found")
#             main()
#     main()


# def issue():
#     problem = input("Enter Your Issue : ")
#     try:
#         cursor = conn.cursor()
#         sql = "INSERT INTO report (phone,report) VALUES ({},'{}')".format(
#             str(phone), problem)
#         cursor.execute(sql)
#         conn.commit()
#         print("Report Submitted Successfully\n")
#         main()
#     except:
#         print("Rendering to submit\n")


# def out():
#     user_id = ""
#     print("You are logged out properly\n")
#     log_sign()


# def main():
#     print("\t\t\t\t**************************************************************************************************************")
#     print("\t\t\t\t\t\t\t\tRAILWAY MAINAGEMENT AND RESERVATION SYSTEM PORTAL")
#     print("\t\t\t\t**************************************************************************************************************")

#     print("\t\t\t\t\t\t\t\t\tA Project by Tarush..")
#     print("\t\t\t\t")
#     print("MAIN MENU\n")
#     print("The time is:")
#     print(date_t, "\n")

#     print("------------\n1. Book a ticket\n2. Cancel ticket\n3. Update your profile\n4. Rail Enquiry\n5. View Tickets\n6. Report Issue\n7. Delete Account\n8. Log Out\n9. Generate Your Ticket\n10. Exit the Portal\n---------------")
#     print("")
#     user_ch_2 = input("Enter your choice : ")
#     if user_ch_2 == '1':
#         book()
#     elif user_ch_2 == '2':
#         cancel()
#     elif user_ch_2 == '3':
#         update()
#     elif user_ch_2 == '4':
#         enquiry()
#     elif user_ch_2 == '5':
#         view()
#     elif user_ch_2 == '6':
#         issue()
#     elif user_ch_2 == '7':
#         delete()
#     elif user_ch_2 == '8':
#         out()
#     elif user_ch_2 == '9':
#         generate()

#     elif user_ch_2 == '10':
#         print("\n**** Thank you visit again 🙏 ******\n")
#         out()
#     else:
#         print("Invalid Input")
#         main()


# def mapp():
#     print("************* WELCOME TO THE TARRIF SECTION *************** \n", " Tickets which are available for:", str(l1),
#           "\nBanglore <-> Delhi -- RS 500\nMumbai <-> Delhi -- RS 500\nHyderbad <-> Delhi -- RS 500\nRajasthan <-> Delhi -- RS 500\nTamilnadu <-> Delhi -- RS 500\n")

#     print()
#     log_sign()


# def signup():
#     usename = input("Enter your username : ")
#     password = input("Enter your password : ")
#     c_pass = input("Enter your password again : ")
#     if password == c_pass or len(str(password)) >= 8:
#         p = "@@".join(password)
#         phone = int(input("Enter your Phone number : "))

#         r1 = randrange(100, 200)
#         r2 = randrange(100, 200)
#         print("Prove You are not robot ", r1, "+", r2)
#         user_ans = int(input("Enter your Ans : "))
#         if user_ans == r1+r2:
#             if len(str(phone)) == 10:
#                 try:
#                     cursor = conn.cursor()
#                     sql = "INSERT INTO user_info (username,pass,phone) VALUES ('{}','{}','{}')".format(
#                         usename, p, phone)
#                     cursor.execute(sql)
#                     conn.commit()
#                     print("Account Created succesfully\n---------------")
#                     log_sign()
#                 except:
#                     print("Rendering ... The account may exist.\n-----------")
#             print("Invalid Phone Number signup again\n--------------")
#             signup()
#         else:
#             print("Wrong Ans signup again.\n--------------------")
#             signup()

#     else:
#         print("Password does't matched\n------------- ")
#         log_sign()


# def log_sign():
#     print("\t\t\t\t**************************************************************************************************************")
#     print("\t\t\t\t\t\t\t\tRAILWAY MAINAGEMENT AND RESERVATION SYSTEM PORTAL")
#     print("\t\t\t\t**************************************************************************************************************")

#     print("\t\t\t\t\t\t\t\t\tA Project by Tarush..")
#     print("\t\t\t\t")
#     print("MAIN MENU\n")
#     print("The time is:")
#     print(date_t, "\n")

#     print("1. Sign Up or Create an Account to book your tickets\n2. Login to book your tickets\n3. Tarrif, enquiry and other details\n4. Exit the Portal\n--------------------- ")

#     user_ch_1 = int(input("Enter Choice : "))
#     if user_ch_1 == 1:
#         signup()
#     elif user_ch_1 == 2:
#         login()
#     elif user_ch_1 == 3:
#         mapp()
#     elif user_ch_1 == 4:
#         print("\n**** Thank you visit again 🙏 ******\n")

#     else:
#         print("Wrong input choosen")
#         log_sign()


try:

    global conn
    user_id = ""
    conn = tarush.connect(host="localhost", port="3306", user="root",
                          password="omsairam", database="railway")
    cursor = conn.cursor()

    if user_id == "":
        log_sign()
    if user_id != "":
        main()

except:
    print("The server is probably not runnng....")
