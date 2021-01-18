from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_mysqldb import MySQL
# from functions import *
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "omsairam"
app.config['MYSQL_DB'] = "railway"

today_date = datetime.datetime.now()
mysql = MySQL(app)
user_id = ""


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
        global user_id
        user_id = a[0]
        print(f"the user id is {user_id}")
        data = cur.rowcount
        # print(f"the user id is {user_id}")

        try:
            if user_id == "":
                return redirect("/home")

            if user_id != "":
                return render_template('Main.html', values=user_id, name=a[1])
        except:
            print("validating")
            return "this is the error"

    else:
        # print(f"the user id is {user_id}")
        # redirect(url_for('home', date=date))
        # return render_template('Main.html')
        return render_template('Signup.html')


@app.route('/home', methods=['GET', 'POST'])
def indexx():
    # print(f"the user id is {a}")
    print("this is the user id", user_id)

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


@app.route('/Book', methods=['GET', 'POST'])
def Bookk():
    if request.method == 'POST':

        post_title = request.form['booking_val']
        global ticket
        ticket = post_title
        print("the ticket is ", ticket)

        # returne(post_title)

        return render_template('booking.html', value=int(post_title))
    else:
        # global user_id
        # print("the user id is ", user_id)
        return render_template('ticket.html')

        # Handle error or do something else


if __name__ == '__main__':
    app.run(debug=True)
