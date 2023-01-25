from flask import Flask, render_template, request
import pandas as pd
import warnings
from joblib import load
from sklearn.preprocessing import PolynomialFeatures
import os


import html

app = Flask(__name__)

@app.route("/", methods=['GET'])
def select():
    text = 'bonjour voisi un example de forma json pour la prediction: <br> {"lat":-27.27,"long":182.50,"depth":51,"stations":13} > 4.5 <br> {"lat":-15,"long":184.62,"depth":40,"stations":54} > 5.1 <br> le prediction dans se ca sera de .pour predire l\'adresse et 127.0.0.1:5000/predi'
    return html.html1 + text + html.html2 

@app.route("/predi", methods=['GET'])
def predi():
    try:
        warnings.filterwarnings("ignore")
        loaded_model = load('model.joblib')
        df = pd.DataFrame([[request.json['lat'], request.json['long'], request.json['depth'], request.json['stations'], ]])
        prediction = loaded_model.predict(df)
        print(prediction,"#####################")
        prediction = "le manetude sera autoure de : " + str(prediction[0]) + " sur l'echele de richter"
        
        
    except:
        prediction = 'erreur de prediction pas de json fournie. <br> (je recommande l\'utilisation de `Development Platform - Insomnia` pour les appelle a l\'API.) <br> json> '
    return html.html1 + prediction + html.html2

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)