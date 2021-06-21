from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

@app.route('/', methods=['POST'])

def api():
    a=request.get_json()
    
    delhi = joblib.load("delhi.pkl")
    mumbai = joblib.load("mumbai.pkl")
    bangalore = joblib.load("bangalore.pkl")
    chennai = joblib.load("chennai.pkl")
    kolkata = joblib.load("kolkata.pkl")
    hyderabad = joblib.load("hyderabad.pkl")
    
    city=a['City']
    area=a['area']
    latitude=a['latitude']
    longitude=a['longitude']
    bedroom=a['bedroom']
    bathroom=a["bathroom"]
    balcony=a['balcony']
    resaleornew=a['resaleornew']
    parking=a['parking']
    furnished_status=a['furnished_status']
    lift=a['lift']
    landmark=a['landmark']
    flatorIndividual=a['flatorIndividual']
    
    a=[area,latitude,longitude,bedroom,bathroom,balcony,resaleornew,parking,furnished_status,lift,landmark,flatorIndividual]
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
    
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(debug=True )
