import os
import numpy as np
from prediction import *
from flask import Flask, jsonify, request, json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def price():
     data = request.json
     df = pd.DataFrame(data, index=[0])
       
     #predicting the price using the model
     price_pred = np.array2string(predict(df).round(2)) #gives output as a list
     return jsonify({"Predicted price of the house " : price_pred[1:-1]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT",  5000))

