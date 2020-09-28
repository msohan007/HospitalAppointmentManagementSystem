import sqlite3
from sqlite3 import Error


class DB:
    def __init__(self, filename, tablename=None):
        self.filename = filename
        self.tablename = tablename

    def connect_DB(self):
        try:
            conn = sqlite3.connect(self.filename)
            return conn
        except Error:
            print("Unable to establish a database connection, Database file doesnot exist.")

    def createtable(self):
        conn = self.connect_DB()
        if conn:
            query_1 = """CREATE TABLE IF NOT EXISTS user(user_id integer PRIMARY KEY AUTOINCREMENT,username text, 
            password text,firstname text,lastname text,age integer,city text,gender text,address text) """
            query = """CREATE TABLE IF NOT EXISTS availability(user_id integer PRIMARY KEY AUTOINCREMENT,username 
            text,appointment_date text, appointment_time text,doctor_name text) """
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.execute(query_1)
            conn.commit()
            print("Table Created Successfully...")
            conn.close()

    def insert_into_table(self, tablename: str, data):
        conn = self.connect_DB()
        cursor = conn.cursor()
        if tablename == 'user':
            cursor.execute("INSERT INTO user VALUES (NULL,?,?,?,?,?,?,?,?)", (data))
            conn.commit()
            conn.close()
        elif tablename == 'availability':
            cursor.execute("INSERT INTO availability VALUES (NULL,?,?,?,?)", (data))
            conn.commit()
            conn.close()
        else:
            return None
        data_0 = data[0]
        userId = self.usr_id(data_0)
        print("Inserting Data complete")
        return userId[0]

    def user_details(self, username):
        conn = self.connect_DB()
        cursor = conn.cursor()
        # if tablename == "user":  # fetch from user table the particular "column_name"
        query = f"SELECT appointment_date,appointment_time,doctor_name FROM availability where username like ?"
        fetch_obj = cursor.execute(query, (username,))
        all_data = fetch_obj.fetchall()
        conn.commit()
        conn.close()
        return all_data

    def fetch_from_table(self, tablename, column_name):
        conn = self.connect_DB()
        cursor = conn.cursor()
        # if tablename == "user":  # fetch from user table the particular "column_name"
        query = f"SELECT {column_name} FROM {tablename}"
        fetch_obj = cursor.execute(query)
        all_data = fetch_obj.fetchall()
        conn.commit()
        conn.close()
        return all_data

    def get_password(self, username):
        conn = self.connect_DB()
        cursor = conn.cursor()
        obj = cursor.execute("SELECT user_id,password from user where username like ?", (username,))
        passwd = obj.fetchone()
        conn.close()
        if passwd:
            usrnm = passwd[0]
            return usrnm, passwd[1]
        else:
            return None, None

    def check_unique_username(self, username):
        conn = self.connect_DB()
        cursor = conn.cursor()
        try:
            query = "SELECT username FROM user WHERE username LIKE " + username + ";"
            # try:
            result_obj = cursor.execute(query)
            res = result_obj.fetchall()
            conn.close()
            if res:
                return True
            else:
                return False
        except sqlite3.OperationalError:
            return False

    def usr_id(self, username):
        conn = self.connect_DB()
        cursor = conn.cursor()

        query = f"SELECT user_id FROM user WHERE username LIKE ?"
        obj = cursor.execute(query, (username,))
        data = obj.fetchone()
        conn.close()
        return data

    def execute_query(self, query_string, params):
        conn = self.connect_DB()
        cursor = conn.cursor()

        search_obj = cursor.execute(query_string, params)
        data = search_obj.fetchall()
        result = []
        for row in data:
            result.append(list(row))
        return result

    def getFullName(self, username):
        conn = self.connect_DB()
        cursor = conn.cursor()

        query_string = "SELECT firstname,lastname FROM user WHERE username like ?"
        search_object = cursor.execute(query_string, (username,))

        data = search_object.fetchone()
        conn.close()
        fname, lname = data[0], data[1]
        fullname = fname + ' ' + lname
        return fullname.title()  # returns the user full name

    def update_row(self, data: tuple):  # for availability table
        """
        :param data: Last value should be the user_id
        With the following order, appointment_time, appointment_date, doctor_name, user_id
        :return: None
        """
        conn = self.connect_DB()
        cursor = conn.cursor()

        query = """UPDATE availability
         SET appointment_time = ?,
          appointment_date = ?,
           doctor_name = ?
            WHERE user_id = ?
        """
        cursor.execute(query, data)
        print("Update successful")
        conn.commit()
        conn.close()

    def get_usr_id(self, data):
        conn = self.connect_DB()
        cursor = conn.cursor()

        query = "SELECT user_id FROM availability WHERE username like ? and doctor_name like ? and appointment_date " \
                "like ? and appointment_time like ?"
        cursor.execute(query, data)
        usr_id = cursor.fetchone()
        conn.commit()
        conn.close()
        return usr_id
