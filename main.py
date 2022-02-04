from flask import Flask, request, jsonify
import joblib
import pickle
import pandas as pd

# CREATE FLASK APP

app = Flask(__name__)


# CONNECT POST API CALL --> predict() Function

@app.route('/predict', methods=['POST'])
def predict():
    # GET JSON REQUEST

    feat_data = request.json

    # CONVERT JSON tO PANDAS DF (COL NAMES)

    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)

    # PREDICT

    prediction = list(model.predict(df))

    return jsonify({'prediction': str(prediction)})


# LOAD MY MODEL and LOAD COLUMN NAMES

if __name__ == '__main__':
    model = joblib.load("gb_model.pkl")

    col_names = joblib.load('col_names.pkl')

    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
