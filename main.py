from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_mysqldb import MySQL
# from functions import *
import datetime

app = Flask(__name__)

# Configure db
# db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "omsairam"
app.config['MYSQL_DB'] = "railway"

today_date = datetime.datetime.now()
mysql = MySQL(app)
try:
    if user_id == "":

        log_sign()
    if user_id != "":
        main()
except:
    print("validating")
user_id = 1
phonenumber = ""
password = ""


@app.route('/', methods=['GET', 'POST'])
def Login():
    global phonenumber
    if request.method == 'POST':

        userDetails = request.form
        phone = userDetails['phone']
        password = userDetails['password']

        phonenumber = phone
        p = "@@".join(password)
        sql = "SELECT * FROM user_info WHERE phone={} and pass='{}'".format(
            int(phone), p)
        cur = mysql.connection.cursor()
        cur.execute(sql)
        a = cur.fetchone()
        user_id = a[0]
        data = cur.rowcount
        print(f"the user id is {user_id}")
        # return redirect('/home', values=user_id, name=a[1], phone=a[3])
        return render_template('Main.html')
    return render_template('Signup.html')


@app.route('/Book', methods=['GET', 'POST'])
def Bookk():
    if request.method == 'POST':

        post_title = request.form['booking_val']
        global ticket
        ticket = post_title
        print("the ticket is ", ticket)

        # returne(post_title)

        return render_template('booking.html', value=int(post_title)), ticket
    else:
        return render_template('ticket.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return render_template('Main.html')
    return render_template('index.html')


def logindata(a, b):

    phone = int(a)
    password = b
    p = "@@".join(password)
    print(p, password, phone)
    if len(str(phone)) == 10 or len(str(password)) >= 8:
        try:
            cur = mysql.connection.cursor()
            sql = "SELECT * FROM user_info WHERE phone={} and pass='{}'".format(
                phone, p)
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            user_id = a[0]
            data = cur.rowcount
            print(data)
            if data == 1:

                print("sucess")

            else:
                print("\nIncorrect details\n--------------")

        except:
            print("\nError Occured. Your details may be incorrect.\n--------------")

    else:
        print("Invalid pnone number login again\n------------")


def cancel(idd1, ticketid1):
    print("Go to view ticket section to know your ticket id.\n--------------------")
    try:
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM book_ticket WHERE phone={} and user_id={}".format(
            # phone, user_id)
              phone, user_id)

        cur.execute(sql)
        a = cur.fetchall()
        for result in a:
            print(result)
        if cur.rowcount >= 1:
            try:
                idd = int(idd1)
                for i in range(1, idd+1):
                    ticket_id = int(ticketid1)
                    s = "DELETE FROM book_ticket where id={}".format(ticket_id)
                    cur.execute(s)
                    mysql.connection.commit()
                    print("1 ticket canceled")
                # main()
            except:
                print("Error while canceling the ticket")
                # main()
        else:
            print("No tickets are regestered \n")
    except:
        print("Rendering ..")
        # main()


def book(name, age, srt_point, end_point, number, date, month, j_date):

    today_date = datetime.datetime.now()
    phone = 7338003303
    cur = mysql.connection.cursor()
    sql = "INSERT INTO book_ticket (name,age,starting_point,end_point,phone,user_id,book_date,j_date) VALUES ('{}',{},'{}','{}',{},{},'{}','{}')".format(
        name, age, srt_point, end_point, phone, user_id, today_date, j_date)
    cur.execute(sql)
    mysql.connection.commit()
    # print(i, " *** Ticket has been REGISTERED THANK YOU VIST AGAIN ***\n")

    print("error")


@app.route("/Cancel", methods=['GET', 'POST'])
def Cancel():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        number = userDetails['numberofticekts']
        idd = userDetails['idoftickets']
        cancel(number, idd)
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM book_ticket WHERE phone={} and user_id={}".format(
            # phone, user_id)
              phone, user_id)

        cur.execute(sql)
        a = cur.fetchall()

        return render_template('cancel.html', res=a)
    else:
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM book_ticket WHERE phone={} and user_id={}".format(
            # phone, user_id)
              phone, user_id)

        cur.execute(sql)
        a = cur.fetchall()

        return render_template('cancel.html', res=a)


def password(password):

    p = "@@".join(password)
    if len(password) >= 8:
        try:
            cur = mysql.connection.cursor()
            sql = "UPDATE user_info set pass=%s WHERE id=%s"
            values = (p, user_id)
            cur.execute(sql, values)
            cur.commit()
            print("Password Updated\n------------------")
        except:
            print("Error Occured")

    else:
        print("password less than 8 is not allowed.\n---------------")


@app.route("/Profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':

        userDetails = request.form
        number = userDetails['password_val']
        password(number)

        return render_template('profile.html')
    else:
        return render_template('profile.html')


@app.route("/view")
def view():

    cur = mysql.connection.cursor()
    sql = "SELECT * FROM book_ticket WHERE phone={} and user_id={}".format(
        # phone, user_id)
        phone, user_id)

    cur.execute(sql)
    a = cur.fetchall()

    return render_template('view.html', res=list(a))


@app.route("/Admin")
def Admin():

    return render_template('enquiry.html')


@app.route("/Enquiry")
def enquiry():
    cur = mysql.connection.cursor()
    sql = "SELECT * FROM enq"

    cur.execute(sql)
    a = cur.fetchall()

    return render_template('enquiry.html', res=a)


def issue(number):

    try:
        cur = mysql.connection.cursor()
        sql = "INSERT INTO report (phone,report) VALUES ({},'{}')".format(
            "7338003303", number)
        cur.execute(sql)
        cur.commit()
        print("Report Submitted Successfully\n")

    except:

        print("Rendering to submit\n")


@app.route("/Report", methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        userDetails = request.form
        number = userDetails['report']
        issue(number)

        cur = mysql.connection.cursor()
        sql = "SELECT * FROM report WHERE phone={}".format(
            # phone, user_id)
            phone)

        cur.execute(sql)
        a = cur.fetchall()
        for result in a:
            print(result)
        return render_template('report.html', res=a)
    else:
        cur = mysql.connection.cursor()
        sql = "SELECT * FROM report WHERE phone={}".format(
            # phone, user_id)
            phone)
        cur.execute(sql)
        a = cur.fetchall()

        for result in a:
            print(result)
        return render_template('report.html', res=a)

    return render_template('report.html')


ticket = None


print("the ticket is ", ticket)


@app.route("/home/<name>", methods=['GET', 'POST'])
def indexx(name):
    print(name)
    if request.method == 'POST':
        post_date = request.form['date_val']
        Booked = request.form['booked']
        post_month = request.form['month_val']
        post_start_point = request.form.get('starting_point')
        # select = request.form.get('comp_select')
        post_end_point = request.form.get('ending_point')
        j_date = post_date + "-" + post_month
        if post_start_point == "Banglore" and post_end_point == "Delhi" or post_start_point == "Delhi" and post_end_point == "Banglore":

            cur = mysql.connection.cursor()
            sql = "SELECT * FROM enq WHERE name='BLR<-->DEL(EXPRESS)'"
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            print(a[9])
            result = a[9]
            present = int(result) - int(Booked)

            cur = mysql.connection.cursor()
            sql = f"UPDATE enq set availability={present} WHERE name='BLR<-->DEL(EXPRESS)'"

            cur.execute(sql)
            mysql.connection.commit()

        elif post_start_point == "Kolkata" and post_end_point == "Delhi" or post_start_point == "Delhi" and post_end_point == "Kolkata":

            cur = mysql.connection.cursor()
            sql = "SELECT * FROM enq WHERE name='DEL<-->KOL(EXPRESS)'"
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            print(a[9])
            result = a[9]
            present = int(result) - int(Booked)

            cur = mysql.connection.cursor()
            sql = f"UPDATE enq set availability={present} WHERE name='raajdhani'"

            cur.execute(sql)
            mysql.connection.commit()

        elif post_start_point == "Mumbai" and post_end_point == "Delhi" or post_start_point == "Delhi" and post_end_point == "Mumbai":

            cur = mysql.connection.cursor()
            sql = "SELECT * FROM enq WHERE name='MUM<-->DEL(EXPRESS)'"
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            print(a[9])
            result = a[9]
            present = int(result) - int(Booked)

            cur = mysql.connection.cursor()
            sql = f"UPDATE enq set availability={present} WHERE name='MUM<-->DEL(EXPRESS)'"

            cur.execute(sql)
            mysql.connection.commit()
        elif post_start_point == "Mumbai" and post_end_point == "Banglore" or post_start_point == "Banglore" and post_end_point == "Mumbai":

            cur = mysql.connection.cursor()
            sql = "SELECT * FROM enq WHERE name='BLR<-->MUM(EXPRESS)'"
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            print(a[9])
            result = a[9]
            present = int(result) - int(Booked)

            cur = mysql.connection.cursor()
            sql = f"UPDATE enq set availability={present} WHERE name='BLR<-->MUM(EXPRESS)'"

            cur.execute(sql)
            mysql.connection.commit()
        elif post_start_point == "Mumbai" and post_end_point == "Kolkata" or post_start_point == "Kolkata" and post_end_point == "Mumbai":

            cur = mysql.connection.cursor()
            sql = "SELECT * FROM enq WHERE name='MUM<-->KOL(EXPRESS)'"
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            print(a[9])
            result = a[9]
            present = int(result) - int(Booked)

            cur = mysql.connection.cursor()
            sql = f"UPDATE enq set availability={present} WHERE name='MUM<-->KOL(EXPRESS)'"

            cur.execute(sql)
            mysql.connection.commit()
        elif post_start_point == "Banglore" and post_end_point == "Kolkata" or post_start_point == "Kolkata" and post_end_point == "Banglore":

            cur = mysql.connection.cursor()
            sql = "SELECT * FROM enq WHERE name='BLR<-->KOL(EXPRESS)'"
            cur.execute(sql)
            mysql.connection.commit()
            a = cur.fetchone()
            print(a[9])
            result = a[9]
            present = int(result) - int(Booked)

            cur = mysql.connection.cursor()
            sql = f"UPDATE enq set availability={present} WHERE name='BLR<-->KOL(EXPRESS)'"

            cur.execute(sql)
            mysql.connection.commit()

        else:
            print(post_end_point)
            print(post_start_point)
            print("not accessable")

        for i in range(0, int(Booked)):

            post_name = request.form[f'name_{i}']

            post_age = request.form[f'age_{i}']
            book(post_name, post_age, post_start_point,
                 post_end_point, phone, user_id, today_date, j_date)
        # print(post_end_point)
        # print(post_start_point)

        # print(post_date)
        # print(post_name)
        # print(post_age)
        # print(post_month)
        # print(post_name)
        # print(user_id)

        # book(post_name, post_age, post_start_point, post_end_point,
        #      phone, user_id, date_t, j_date)

        # post_title = request.form['title']
        # post_content = request.form['content']
        # post_author = request.form['author']
        # new_post = BlogPost(
        #     title=post_title, content=post_content, author=post_author)
        # db.session.add(new_post)
        # db.session.commit()
        return render_template('main.html')
    else:
        return render_template('main.html', name=name_pro)


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)

# CREATE TABLE users(
#     name varchar(20),
#     Email varchar(40));
