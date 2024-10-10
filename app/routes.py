from flask import render_template, request, jsonify
from app import app
from app.models import InsuranceRating

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    age = int(data['age'])
    vehicle_value = float(data['vehicleValue'])
    mileage = float(data['mileage'])
    
    premium = InsuranceRating.calculate_premium(age, vehicle_value, mileage)
    return jsonify({'premium': premium})