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
    try:

        name = obj.empName(EmpID)
        RefID = obj.GenerateReferenceId()
        checkindate = datetime.now()
        current_time = datetime.now().date()
        print("=======",current_time)
        data=obj.checkIn(EmpID, name,current_time, checkindate, RefID)
        return render_template("checkedout.html")

    except Exception as e:
        error_message = f"An error occurred{e}"
        return render_template("admin/error.html", error_message=error_message)

@app.route('/chechoutreference',methods=['GET','POST'])

def chechoutreference():

    if request.method=="POST":

        RefID=request.form.get('checkoutrerefenceid')

        print("-----------------",RefID)

        currentTime = datetime.now()

        # checkout=currentTime.replace("-",":")

        print(currentTime)

        obj.checkout(RefID,currentTime)

    return redirect('/')


# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
