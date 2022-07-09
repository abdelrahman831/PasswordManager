from django.shortcuts import render,redirect
from password_manager_app.models import Password_Manager,User_Registration,login_form
from django.contrib.auth.models import User, auth
import mysql.connector
from django.contrib import messages
from json import dumps
# Import ListView module

def Index(request):
    print(visitor_ip_address(request))


    return render(request,'./home.html',{"state":state})


id_Logged_in =0
id_Login =1

us = ''
universal_data = [us]
siteNames = []
usernames = []
passwords = []

list_of_usernames = []

dict = {}

def logged_in(request):
    global us,siteNames,passwords,usernames

    global id_Logged_in
    siteNames = []
    usernames = []
    passwords = []
    if request.method == "POST":
        try:
            connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                                 database='sql11504914',
                                                 user='sql11504914',
                                                 password='yZHd9eItsh')

            sql_select_Query = "select * from password_manager_app_password_manager"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_select_Query)


            sitename = request.POST['siteName']
            username = request.POST['userName']
            password = request.POST['password']

            set = Password_Manager(registered_user=us,siteName= sitename,userName=username,password=password)
            set.save()

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


        return redirect(logged_in)
    else:
        try:
            connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                                 database='sql11504914',
                                                 user='sql11504914',
                                                 password='yZHd9eItsh')

            sql_data = f"select * from password_manager_app_password_manager WHERE registered_user = '{us}'"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_data)
            records = cursor.fetchall()


            for row in records:
                siteNames.append(row[2])
                usernames.append(row[3])
                passwords.append(row[4])


            all_data = {'sitenames':siteNames,'usernames':usernames,'passwords':passwords}

            dataJSON = dumps(all_data)


        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

                print("MySQL connection is closed")

        return render(request, 'index.html', {'data':dataJSON})

    return render(request,'index.html',dict)

state = "off"


def login(request):
    global us, dict, state
    if request.method == 'POST':
        try:
            connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                                 database='sql11504914',
                                                 user='sql11504914',
                                                 password='yZHd9eItsh')

            sql_select_Query = "select * from login_form"

            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            username = request.POST['username']
            us = username
            password = request.POST['password']

            global list_of_usernames
            if len(records) != 0:
                for row in records:
                    if username == row[1] and password == row[2]:
                        state = "on"

                        return redirect(Index)
                    if username == row[1] and password != row[2]:
                        # dict = {'name':username,"problem":"password Errata"}
                        messages.info(request, "Username and password don't matching")
                        state = "off"

                        return redirect(login)

            messages.info(request, "not a member? register now")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        state = "off"
        return render(request, 'login.html')
    else:

        return render(request, 'login.html')


def register(request):
    global us, dict, state
    if request.method == 'POST':
        try:
            connection = mysql.connector.connect(host='sql11.freemysqlhosting.net',
                                                 database='sql11504914',
                                                 user='sql11504914',
                                                 password='yZHd9eItsh')

            sql_select_Query = "select * from login_form"


            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            username = request.POST['nome']
            us = username
            password = request.POST['password']
            password2 = request.POST['password2']
            sql_insert_Query = f"INSERT INTO login_form(username, password) VALUES('{username}', '{password}')"
            insert_cursor = connection.cursor(buffered=True)
            global list_of_usernames
            if len(records) != 0:
                for row in records:
                    if username == row[1]:
                        messages.info(request, "Username already exist")
                        return redirect(register)
            if password2 == password:
                insert_cursor.execute(sql_insert_Query)
                connection.commit()
                state = "on"
                return redirect(Index)
            else:
                messages.info(request, "password don't match")
                return redirect(register)

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return render(request, 'registrati.html')
    else:

        return render(request, 'registrati.html')


def logout(request):
    global state
    state="off"
    return redirect(Index)

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip