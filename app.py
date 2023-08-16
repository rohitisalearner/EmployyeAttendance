from flask import Flask,request,render_template, redirect
from datetime import date, datetime
from admin.fun import Attedance

obj=Attedance()
# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=="POST":

        EmpId=request.form.get("EmpId")

        data=obj.empInfo(int(EmpId))

        return render_template("user/checkin.html",data=data) 

    return render_template ("user/home.html")

@app.route("/checkedin/<EmpID>")

def checkedin(EmpID):

    name = obj.empName(EmpID)

    RefID = obj.GenerateReferenceId()

    # print(RefID, name)
    checkindate = datetime.now()

    # print(checkindate)
    # currentTime = datetime.now().strftime('%H-%M-%S')

    # checkInTime=currentTime.replace("-",":")
    # print(checkindate)
    obj.checkIn(EmpID,name,checkindate,checkindate,RefID)
   
    return render_template("checkedout.html",RefID=RefID)

@app.route('/chechoutreference',methods=['GET','POST'])

def chechoutreference():

    if request.method=="POST":

        RefID=request.form.get('checkoutrerefenceid')

        # print("-----------------",RefID)

        currentTime = datetime.now()

        # checkout=currentTime.replace("-",":")

        print(currentTime)

        obj.checkout(RefID,currentTime)
        obj.calculate_time()



    return "checkedOut"

obj.calculate_time()


# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
