       __  __                                     _           
      |  \/  |                                   | |          
      | \  / | ___  ___ _   _ _ __ ___  ___    __| | ___  ___ 
      | |\/| |/ _ \/ __| | | | '__/ _ \/ __|  / _` |/ _ \/ __|
      | |  | |  __/\__ \ |_| | | |  __/\__ \ | (_| |  __/\__ \
      |_|  |_|\___||___/\__,_|_|  \___||___/  \__,_|\___||___/
                                                              
                                                              
       _                      _     _                           _             _      
      | |                    | |   | |                         | |           | |     
      | |_ _ __ ___ _ __ ___ | |__ | | ___ _ __ ___   ___ _ __ | |_ ___    __| | ___ 
      | __| '__/ _ \ '_ ` _ \| '_ \| |/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|  / _` |/ _ \
      | |_| | |  __/ | | | | | |_) | |  __/ | | | | |  __/ | | | |_\__ \ | (_| |  __/
       \__|_|  \___|_| |_| |_|_.__/|_|\___|_| |_| |_|\___|_| |_|\__|___/  \__,_|\___|
                                                                                      
                                                                                     
       _                                        _   _ _            _        ______ _ _ _ 
      | |                                      | | (_|_)          | |      |  ____(_|_|_)
      | |_ ___ _ __ _ __ ___   ___ _   _ _ __  | |  _ _  ___    __| | ___  | |__   _ _ _ 
      | __/ _ \ '__| '__/ _ \ / __| | | | '__| | | | | |/ _ \  / _` |/ _ \ |  __| | | | |
      | ||  __/ |  | | |  __/ \__ \ |_| | |    | | | | |  __/ | (_| |  __/ | |    | | | |
       \__\___|_|  |_|  \___| |___/\__,_|_|    |_| |_|_|\___|  \__,_|\___| |_|    |_| |_|
                                                                                   _/ |  
                                                                                  |__/   


Ce projet vise à utiliser des données de tremblements de terre pour prédire la magnitude des séismes sur l'île de Fiji pour prédire la magnitude sure l'échelle de richter.
un projet de Jean-Paul, Séraphim, Irénée SARTORIS, GRANT, KEMBEL, JEUFFRAIN 


## Environnement

Ce projet utilise Python 3.10 et a été créé dans un environnement virtuel nommé "venv". Les paquets nécessaires pour exécuter ce projet sont répertoriés dans le fichier "requirements.txt".

## Fichiers importants
- `api.py` : Ce fichier contient le code pour lancer l'API. Les paquets requis pour l'API sont listés dans `requirements.txt`
- `data.csv` : Ce fichier contient les données utilisées pour entraîner les modèles
- `*.joblib` : Ces fichiers contiennent les modèles entraînés
- `main.ipynb` : Ce fichier contient le code pour le nettoyage des données, la visualisation des données, l'entraînement des modèles et l'exportation des modèles

## Utilisation
1. Activer l'environnement python 3.10 (venv)  en utilisant la commande: `source venv/bin/activate`
2. Exécuter `pip install -r requirements.txt` pour installer les dépendances nécessaires
3. Exécuter `python api.py` pour lancer l'API
4. Utiliser les données dans `data.csv` pour entraîner les modèles en utilisant le code dans `main.ipynb`
5. Utiliser les modèles enregistrés dans les fichiers *.joblib pour effectuer des prédictions en utilisant le code dans main.ipynb ou en les chargeant dans api.py pour les utiliser dans l'API a l'adrese `http://127.0.0.1:5000/` .

## attention 

Il est important de noter que vous devrez peut-être adapter les chemins d'accès aux fichiers mentionnés ci-dessus en fonction de l'emplacement où vous avez stocké les fichiers dans votre système.
Il est également important de vérifier que les versions des librairies utilisées dans ce projet sont compatibles avec votre environnement.



