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

## Backend (backend/)

app.py : Contient la logique principale de l'application Flask, y compris la gestion des routes pour l'API.
requirements.txt : Liste les dépendances nécessaires pour le backend Python.
database.db : Base de données SQLite3 où les notes sont stockées.

## Frontend (frontend/)
src/ : Contient les fichiers sources pour React (composants, états, etc.).
package.json : Contient les informations du projet React, ainsi que les scripts pour lancer l'application.
Auteur

## Développé par [Debugsvg]
