import pymysql

def dbConnection():
    conn = pymysql.connect(host='localhost',
                                user='root',
                                password='rohit123',
                                database='employeeattendance'
                                )
    return conn