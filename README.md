Notepad Application
Description
Cette application Notepad est un outil de prise de notes simple et efficace. Elle repose sur un backend en Python avec Flask pour la gestion des notes, et un frontend en React pour une interface utilisateur moderne et intuitive. Les notes sont sauvegardées localement dans une base de données SQLite3.

Fonctionnalités
Créer, lire, mettre à jour et supprimer des notes
Sauvegarder les notes de manière persistante dans une base de données SQLite3
Interface utilisateur moderne en React pour une navigation fluide
Installation
Prérequis
Python 3.x
Node.js et npm
Backend (Python)
Cloner le dépôt :

bash
Copier le code
git clone <https://github.com/Debugsvg/Note_app_react.git>
cd <Note_app_react>
Créer un environnement virtuel (optionnel mais recommandé) :

bash
Copier le code
python -m venv env
source env/bin/activate  # Sur MacOS et Linux
env\Scripts\activate  # Sur Windows
Installer les dépendances Python :

bash
Copier le code
pip install -r requirements.txt
Lancer le serveur backend :

bash
Copier le code
python main.py
Le serveur backend sera alors accessible sur http://localhost:5000.

Frontend (React)
Aller dans le dossier frontend :

bash
Copier le code
cd frontend
Installer les dépendances :

bash
Copier le code
npm install
Lancer le serveur frontend :

bash
Copier le code
npm run dev
L'application React sera accessible sur http://localhost:3000.

Utilisation
Ouvrir http://localhost:3000 dans votre navigateur pour accéder à l'application Notepad.
Le backend gère les requêtes de sauvegarde, mise à jour, et suppression des notes dans SQLite3.
Structure du projet
bash
Copier le code
notepad-app/
├── backend/
│   ├── app.py                
│   ├── requirements.txt       
│   └── database.db           
├── frontend/
│   ├── src/
│   └── package.json           
└── README.md                  
Auteurs
Développé par [Debugsvg]

