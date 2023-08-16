import pymysql

def dbConnection():
    conn = pymysql.connect(host='localhost',
                                user='root',
                                database='employeeattendance'
                                )
    return conn