import psycopg2
from pandas import DataFrame
from getpass import getpass


def connect():
    print("Connecting to PostgreSQL")
    dbname = input("Enter database name: ")
    username = input("Enter username: ")
    pwd = getpass()
    hostname = input("Enter hostname: ")
    port_num = input("Enter port: ")
    conn = psycopg2.connect(
        database=dbname,
        user=username,
        password=pwd,
        host=hostname,
        port=port_num
    )
    print(conn)
    return conn


def create(conn, table_name, fname, lname, email, enrollment_date):
    query = "INSERT INTO " + table_name + "(first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(query, (fname, lname, email, enrollment_date))
    conn.commit()


def update(conn, table_name, id, field, value):
    query = "UPDATE " + table_name + " SET " + field + " = %s WHERE student_id = %s"
    cur = conn.cursor()
    cur.execute(query, (value, str(id)))
    conn.commit()


def delete(conn,table_name, id):
    query = "DELETE FROM "+ table_name +" WHERE student_id = %s"
    cur = conn.cursor()
    cur.execute(query, str(id))
    conn.commit()


def read(conn, table_name):
    query = "SELECT * FROM "+table_name
    cur = conn.cursor()
    cur.execute(query)
    table = DataFrame(cur.fetchall())
    print(table.columns.tolist())
    print("----------------------------------------------")
    print("id fname  lname    email    enrollment_date")
    print("----------------------------------------------")
    print(table.to_string(header=False, index=False))
    print("----------------------------------------------")


def main():
    conn = connect()
    table_name = input("Enter the name of the table you would like to edit: ")
    while True:
        user_input = input("What would yo like to do? (create, update, read, delete, exit): ")
        if user_input == "read":
            read(conn, table_name)
        elif user_input == "exit":
            break
        elif user_input == "create":
            fname = input("What is the first name of the student? ")
            lname = input("What is the last name of the student? ")
            email = input("What is the email of the student? ")
            enrollment_date = input("What is the enrollment date of the student? ")
            create(conn, table_name, fname, lname, email, enrollment_date)
        elif user_input == "update":
            while True:
                try:
                    id = int(input("Which student id would you like to update? "))
                    if id < 0:
                        print("Please input a positive number")
                        continue
                    break
                except ValueError:
                    print("Please input a number")
            field = input("Which field would you like to update?(first_name, last_name, email, enrollment_date): ")
            if field != "first_name" and field != "last_name" and field != "email" and field != "enrollment_date":
                print("Invalid field")
                continue
            value = input("Please enter to value to be updated for student " + str(id) + ": ")
            update(conn, table_name, id, field, value)
        elif user_input == "delete":
            while True:
                try:
                    id = int(input("which student id would you like to delete? "))
                    if id < 0:
                        print("please input a positive number")
                        continue
                    break
                except ValueError:
                    print("Please input a number")
            delete(conn, table_name, id)
        else:
            print("Invalid input")
    print("End of the program")
    conn.close()
    print(conn)


if __name__ == "__main__":
    main()
