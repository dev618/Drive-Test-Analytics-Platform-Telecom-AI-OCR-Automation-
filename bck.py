from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
import pyrebase
import re
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'
uid = ""
idToken = ""
globalCircleName = ""

# Initialize Firebase
firebaseConfig = {
    "apiKey": "AIzaSyBiZWWI4vdWhNjwK1547w6dRHKBVZ9it24",
    "authDomain": "telecom-tower-performance-1.firebaseapp.com",
    "databaseURL": "https://telecom-tower-performance-1-default-rtdb.firebaseio.com",
    "projectId": "telecom-tower-performance-1",
    "storageBucket": "telecom-tower-performance-1.appspot.com",
    "messagingSenderId": "681536968586",
    "appId": "1:681536968586:web:82ebaf8bbc7a17e0191a73",
    "measurementId": "G-VP8S76MR98"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# Initialize Firebase Admin SDK with credentials
cred = credentials.Certificate("telecom-tower-performance-1-firebase-adminsdk-76b3k-265f93b36b.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()
auther = firebase.auth()

# Password regex pattern
password_regex = re.compile(r'^(?=.*[A-Z])(?=.*\d{2})(?=.*[!@#$%^&()-+=])[A-Za-z\d!@#$%^&*()-+=]{6,}$')


@app.route("/")
def home():
    return redirect(url_for('welcome'))


@app.route("/welcome")
def welcome():
    return render_template('welcome.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        circle_name = request.form['circle_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match. Please try again.", "error")
            return render_template('signup.html')

        # Validate password format
        if not password_regex.match(password):
            flash(
                "Password should contain at least six characters, one uppercase letter, two digits, and one special symbol.",
                "error")
            return render_template('signup.html')

        try:
            user = auther.create_user_with_email_and_password(email, password)
            db.collection('users').document(user['localId']).set({
                'employee_Name': employee_name,
                'circle_name': circle_name,
                'email': email,
                'isAdmin': False
            })
            flash("Registration successful! You can now login.", "success")
            return redirect(url_for('login'))  # Redirect to login page after successful registration
        except auth.EmailAlreadyExistsError:
            # Flash error message
            flash("Email already exists. Please choose a different one.", "error")
            return render_template('signup.html')
        except Exception as e:
            print('Error creating user:', e)
            # Flash error message
            flash("Registration failed. Please try again.", "error")
            return render_template('signup.html')

    return render_template('signup.html')



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            user = auther.sign_in_with_email_and_password(email, password)
            session['uid'] = user['localId']
            user_data = db.collection('users').document(user['localId']).get().to_dict()
            if user_data.get('isAdmin', True):
                return redirect(url_for('welcome_admin'))  # Redirect to welcome_admin page for admin users
            else:
                return redirect(url_for('welcome_user'))  # Redirect to welcome_user page for regular users

        except auth.UserNotFoundError:
            flash("User not found.", "error")
        except Exception as e:
            print('Error logging in:', e)
            flash(e, "error")

    return render_template('login.html')



@app.route("/welcomeadmin")
def welcome_admin():
    return render_template('welcomeadmin.html')

@app.route("/welcomeuser")
def welcome_user():
    return render_template('welcomeuser.html')

@app.route("/welcome")
def show_welcome():
    return render_template('welcome.html')


@app.route("/taskallocation", methods=['GET', 'POST'])
def task_allocation():
    global globalCircleName
    if request.method == 'POST':
        circleName = request.form.get('project')
        globalCircleName = circleName
        return redirect(url_for('task_allocation'))
    # Fetch employee names from Firestore
    employee_names = []
    users_ref = db.collection('users').where("circle_name", "==", globalCircleName)
    docs = users_ref.stream()
    for doc in docs:
        employee_names.append(doc.to_dict().get('employee_Name'))
    # Pass employee names to the taskallocation.html template
    return render_template('Taskallocation.html', employee_names=employee_names)


@app.route("/taskStatus")
def task_Status():
    if request.method == 'POST':
        return redirect(url_for('task_Status'))
    return render_template('TaskStatus.html')


@app.route('/projectallocation')
def projectallocation():
    if request.method == 'POST':
        return redirect(url_for('project_allocation'))
    return render_template('projectallocation.html')

@app.route('/Allocationrequest.html')
def Allocationrequest():
    return render_template('Allocationrequest.html')


@app.route("/AllocatedStatus.html")
def AllocatedStatus():
    return render_template("AllocatedStatus.html")

@app.route("/nooption.html")
def no_option():
    return render_template("nooption.html")

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        project = request.form.get('selectProject')
        operator = request.form.get('selectOperator')
        circle = request.form.get('project')
        activity = request.form.get('selectActivity')

        # Retrieve additional field value if present
        additional_field = request.form.get('hiddenChosenOption', None)

        # Data to be saved in Firestore
        data = {
            "project": project,
            "operator": operator,
            "circle": circle,
            "activity": activity,
            "additional_field": additional_field
        }

        try:
            # Create a new document with a unique ID in the "Project_Selection" collection
            doc_ref = db.collection("Project_Selection").document()
            doc_ref.set(data)
            doc_id = doc_ref.id
            flash("Form submitted successfully!", "success")
            return redirect(url_for('get_employees', project=project, nameCircle=circle))
        except Exception as e:
            print("Error:", str(e))
            flash("An error occurred in Firestore.", "error")
            return redirect(url_for('projectallocation'))  # Redirect back to the form page in case of an error

    # Handle the case when the form is not submitted via POST method
    return redirect(url_for('projectallocation'))




# Add this route to fetch employees based on selected circle
# Add this route to fetch employees based on selected circle
@app.route("/getEmployees", methods=['POST', 'GET'])
def get_employees():
    circleName = request.args.get('nameCircle')
    project = request.args.get('project')


    # Fetch employees based on the selected circle from Firestore
    employee_names = []
    users_ref = db.collection('users').where('circle_name', '==', circleName).stream()
    for doc in users_ref:
        employee_names.append(doc.to_dict()['employee_Name'])

    return render_template("Taskallocation.html", project=project, circleName=circleName, employee_names=employee_names)




@app.route("/saveTableData", methods=['POST'])
def save_table_data():
    if request.method == 'POST':
        data = request.json

        try:
            # Save the table data to Firestore
            doc_ref = db.collection("task_allocation").document()
            doc_ref.set(data)
            flash("Table data saved successfully!", "success")
        except Exception as e:
            print("Error:", str(e))
            flash("An error occurred while saving table data.", "error")

        return redirect(url_for('task_allocation'))

# Add this route to fetch employees based on selected circle

@app.route("/update_availability", methods=['POST'])
def update_availability():
    if 'uid' not in session:
        return jsonify({'error': 'User not authenticated'}), 401  # Unauthorized

    try:
        data = request.json
        response = data.get('response')
        uid = session['uid']

        if response == 'yes':
            db.collection('users').document(uid).update({'isAvailable': True, 'Issue': ""})
            return jsonify({'message': 'Availability updated successfully'}), 200
        else:
            db.collection('users').document(uid).update({'isAvailable': False})
            return jsonify({'message':  'Availability updated successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to update availability', 'details': str(e)}), 500



@app.route("/nooption.html", methods=['GET', 'POST'])
def store_issue():
    if request.method == 'POST':

        issue_text = request.form['other']
        try:
            global uid
            if uid:
                user_ref = db.collection('users').document(uid)
                user_ref.set({'Issue': issue_text}, merge=True)

                return "Your Issue: "+issue_text+" Stored Successfully"
            else:
                return jsonify({'error': 'User not authenticated'}), 401  # Unauthorized
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return render_template("nooption.html")

@app.route("/Completestatus")
def Complete_status():
    if request.method == 'POST':
        return redirect(url_for('Complete_status'))
    return render_template('Completestatus.html')


@app.route("/Pendingstatus")
def Pending_status():
    if request.method == 'POST':
        return redirect(url_for('Pending_status'))
    return render_template('pendingstatus.html')

@app.route("/userdetails")
def user_details():
    if request.method == 'POST':
        return redirect(url_for('user_details'))
    return render_template('Userdetails.html')



@app.route("/request_reset_password", methods=['GET', 'POST'])
def request_reset_password():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            auther.send_password_reset_email(email)
            flash("Password resent link sent to your email", "success")
            return redirect(url_for('login'))
        except Exception as e:
            return redirect(url_for('request_reset_password'))

    return render_template('ChangePass.html')


@app.route("/downloadreport")
def download_report():
    if request.method == 'POST':
        return redirect(url_for('download_report'))
    return render_template('DownloadReport.html')


@app.route("/userrequests")
def user_requests():
    return render_template('userreques.html')

@app.route('/fillpostdata')
def fillpostdata():
    return render_template('fillpostdata.html')


# Route for form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Get form data
    site_id = request.form['siteId']
    sector = request.form['sector']
    azimuth = request.form['azimuth']
    tower_height = request.form['towerHeight']
    mechanical_cell = request.form['mechanicalCell']
    electrical_cell = request.form['electricalCell']
    pole_tilt = request.form['poleTilt']

    # Create or get a reference to the main collection
    post_ref = db.collection('PostData')

    # Check if the document with the given site ID exists
    site_doc_ref = post_ref.document(site_id)
    if not site_doc_ref.get().exists:
        # If the document doesn't exist, create a new one
        site_doc_ref.set({})

    # Create or get a reference to the sector document
    sector_doc_ref = site_doc_ref.collection(sector).document('data')

    # Update the data in the sector document
    sector_doc_ref.set({
        'azimuth': azimuth,
        'tower_height': tower_height,
        'mechanical_cell': mechanical_cell,
        'electrical_cell': electrical_cell,
        'pole_tilt': pole_tilt
    })

    return "Form submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)





