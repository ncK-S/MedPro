from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/portal')
def patients_list():
    return render_template('portal.html')

@app.route('/patient')
def patient_data():
    return 'Patient Profile'
