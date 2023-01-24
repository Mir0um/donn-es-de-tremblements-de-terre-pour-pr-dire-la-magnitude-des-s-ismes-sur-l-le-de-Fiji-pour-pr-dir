import pandas as pd
import warnings
from joblib import load

# Supprimer les avertissements pour éviter de les afficher
warnings.filterwarnings("ignore")

# Charger le modèle
loaded_model = load('model.joblib')



# Convertir la liste en dataframe pandas
df = pd.DataFrame([[-15.94,184.95,306,11]])#4.3
#df = pd.DataFrame([[-21.68,180.63,617,63]])#5
#df = pd.DataFrame([[-14.28,170.34,642,29]])#4.7
#df = pd.DataFrame([[49.130111693866255, 2.2864298195198254,250,56]])

# Effectuer une prédiction sur les données
prediction = loaded_model.predict(df)

print(prediction)