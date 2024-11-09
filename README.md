# 📝 Notepad Application

## Description

Cette application **Notepad** est un outil de prise de notes simple et efficace. Elle repose sur un backend en **Python** avec **Flask** pour la gestion des notes et un frontend en **React** pour une interface utilisateur moderne et intuitive. Les notes sont sauvegardées localement dans une base de données **SQLite3**.

## Fonctionnalités

- **CRUD** : Créer, lire, mettre à jour et supprimer des notes
- **Sauvegarde persistante** : Enregistre les notes dans une base de données SQLite3
- **Interface utilisateur réactive** : Navigation fluide grâce à React

## Installation

### Prérequis

- **Python 3.x**
- **Node.js** et **npm**

### Backend (Python)

1. **Cloner le dépôt** :

   ```bash
   git clone https://github.com/Debugsvg/Note_app_react.git
   cd Note_app_react

2. **Créer un environnement virtuel (optionnel mais recommandé)** :
    ```bash
    python -m venv env
    source env/bin/activate  # Sur MacOS et Linux
    env\Scripts\activate     # Sur Windows

3. **Installer les dépendances Python** :
    ```bash
    pip install -r requirements.txt

4. **Lancer le serveur backend** :
    ```bash
    python main.py

Le serveur backend sera alors accessible sur http://localhost:5000.


### Frontend (React)

1. **Aller dans le dossier frontend** :
    ```bash
    cd frontend


2. **Installer les dépendances** :
    ```bash
    npm install


3. **Lancer le serveur frontend** :
    ```bash
    npm run dev

L'application React sera accessible sur http://localhost:3000.


### Points clés du format Markdown utilisé :
- **Titres** : Utilisation de `#` pour les titres et sous-titres (H1, H2, H3).
- **Code** : Utilisation de triple backticks \`\`\` pour les blocs de code et des backticks simples \` pour le code en ligne.
- **Liens** : Utilisation de la syntaxe `[texte du lien](url)` pour créer des liens cliquables.
- **Listes** : Listes à puces et numérotées pour organiser les sections.

Cette structure rendra le README bien lisible sur GitHub et compréhensible pour d'autres développeurs ou utilisateurs souhaitant tester et contribuer à l'application.
