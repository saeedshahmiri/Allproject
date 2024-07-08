import pandas as pd
from flask import Flask, jsonify
import csv

app = Flask(__name__)

# Endpoint to read data from CSV and return as JSON
@app.route('/data', methods=['GET'])
def get_data():
    data = []

    # Read data from CSV file
    with open('bank-full.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)