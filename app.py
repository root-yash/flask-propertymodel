from flask import Flask, request, jsonify
import numpy as np
import joblib
import sklearn
app = Flask(__name__)
@app.route('/', methods=['POST'])
def api():
    a=request.get_json()
    
    delhi = joblib.load("delhi.pb")
    mumbai = joblib.load("mumbai.pb")
    bangalore = joblib.load("bangalore.pb")
    chennai = joblib.load("chennai.pb")
    kolkata = joblib.load("kolkata.pb")
    hyderabad = joblib.load("hyderabad.pb")
    
    city=a['City']
    a=a['Prediction']
    a=np.array(a)
    a=np.expand_dims(a,0)
    
    if city=="Delhi":
        prediction = np.array2string(delhi.predict(a)*1000000)
    elif city=="Mumbai":
        prediction = np.array2string(mumbai.predict(a)*1000000)    
    elif city=="Bangalore":
        prediction = np.array2string(bangalore.predict(a)*1000000) 
    elif city=="Chennai":
        prediction = np.array2string(chennai.predict(a)*1000000) 
    elif city=="Kolkata":
        prediction = np.array2string(kolkata.predict(a)*1000000)
    else:
        prediction = np.array2string(hyderabad.predict(a)*1000000)      
    
    result={"price":prediction}
    print("hi")
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False )
