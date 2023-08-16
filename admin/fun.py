from admin.config import dbConnection

import uuid

conn = dbConnection()

class Attedance:

    def empInfo(self,EmpId):

        with conn.cursor() as cur:

            sql = "SELECT * FROM employeeinfo WHERE EmpId=%s"
            
            s=cur.execute(sql,EmpId)

            row=cur.fetchone()

            return row

    def empName(self,EmpId):

        with conn.cursor() as cur:
            sql = "SELECT Name FROM employeeinfo WHERE EmpId=%s"
            
            cur.execute(sql,EmpId)

            name=cur.fetchone()

            return name

    def checkIn(self,EmpId,Name,Date,Checkin,RefId):

            with conn.cursor() as cur:

                sql = "INSERT INTO dailyattendance (EmpId,Name,Date,CheckinTime,ReferenceID) VALUES (%s, %s, %s, %s, %s)"
                val=EmpId,Name,Date,Checkin,RefId
        
                cur.execute(sql,val)

                conn.commit()

                return "Inserted Successfully"

    def GenerateReferenceId(self):

        random_uuid = uuid.uuid4()

        random_string = str(random_uuid)

        return random_string
    
    def checkout(self, ReferenceID, checkout):

     with conn.cursor() as cur:

        sql = "UPDATE dailyattendance SET CheckoutTime = %s WHERE ReferenceID = %s AND CheckoutTime IS NULL"


        cur.execute(sql, (checkout, ReferenceID))


        conn.commit()


        return "updated"
    



     
    
    