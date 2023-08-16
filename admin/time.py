# import pymysql

# conn = pymysql.connect(host='localhost',
#                             user='root',
#                             database='employeeattendance'
#                             )

# with conn.cursor() as cur:
#     sql="SELECT TIMEDIFF(CheckinTime,CheckoutTime) FROM dailyattendance where EmpId=105"
#     print("sql query -------------",sql)
#     cur.execute(sql)
#     time_fect=cur.fetchone()
#     # print("-------------.....//// execution=",time)
#     print("____________>>>>>>>>>>>> fetching=",time_fect[0])

import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       database='employeeattendance')

with conn.cursor() as cur:
    sql = "SELECT CheckinTime, CheckoutTime FROM dailyattendance WHERE EmpId = 8"
    cur.execute(sql)
    attendance_data = cur.fetchone()

    if attendance_data:
        checkin_time = attendance_data[0]
        checkout_time = attendance_data[1]

        time_difference = checkout_time - checkin_time
        print("Checkin Time:", checkin_time)
        print("Checkout Time:", checkout_time)
        print("Time Difference:", time_difference)

conn.close()
