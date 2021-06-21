from flask import Flask, request, jsonify
import numpy as np
import joblib
app = Flask(__name__)
@app.route('/', methods=['POST'])
def api():
    a=request.get_json()
    
    delhi = joblib.load("delhi.pb")
    #mumbai = joblib.load("mumbai.pb")
    #bangalore = joblib.load("bangalore.pb")
    #chennai = joblib.load("chennai.pb")
    #kolkata = joblib.load("kolkata.pb")
    #hyderabad = joblib.load("hyderabad.pb")
    
    
    
    return "hello world"
    

if __name__ == '__main__':
    app.run(debug=True )
