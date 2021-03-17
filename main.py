import pickle
from flask import Flask, request, jsonify
from model_files.ml_model import predict_mpg

##creating a flask app and naming it "app"
app = Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

@app.route('/', methods=['GET'])
def my_home():
    return 'Welcome to the Home Page!!'

@app.route('/predict', methods=['POST'])
def predict():
    vehicle = request.get_json()
    print(vehicle)
    with open('model_files/model.pkl', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_mpg(vehicle, model)

    result = {
        'mpg_prediction': list(predictions) 
    }
    return jsonify(result)


# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port='5000')

