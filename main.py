from flask import Flask, request
import json
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/poisson')
def poisson():
    lmbd = float(request.args.get('lambda'))
    
    result = {
        'rv': np.random.poisson(lmbd)
    }
    return json.dumps(result, indent=10)

@app.route('/exponential')
def exponential():
    lmbd = float(request.args.get('lambda'))
    
    result = {
        'rv': np.random.exponential(lmbd)
    }

    return json.dumps(result, indent=10)

if __name__ == '__main__':
    app.run(debug=True)
