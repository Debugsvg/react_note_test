from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Permet les requêtes cross-origin

# Initialisation de la base de données
def init_db():
    with sqlite3.connect("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL)''')
    conn.close()

init_db()

# Fonction pour récupérer toutes les notes depuis la base de données
@app.route('/notes', methods=['GET'])
def get_notes():
    with sqlite3.connect("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        notes = [{"id": row[0], "title": row[1], "content": row[2]} for row in cursor.fetchall()]
    print("Notes:", notes)  # Imprime les notes dans le terminal
    return jsonify(notes)

# Fonction pour ajouter une note dans la base de données
@app.route('/notes', methods=['POST'])
def add_note():
    new_note = request.json
    title = new_note.get("title")
    content = new_note.get("content")
    
    with sqlite3.connect("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        new_note_id = cursor.lastrowid
        new_note['id'] = new_note_id

    print("Note ajoutée basec:", new_note)
    return jsonify(new_note), 201

# Fonction pour supprimer une note de la base de données
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    with sqlite3.connect("notes.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        deleted_count = cursor.rowcount  # Nombre de lignes supprimées

    if deleted_count > 0:
        print("Note supprimée avec l'ID:", note_id)
        return jsonify({"message": "Note supprimée"}), 200
    else:
        print("Aucune note trouvée avec l'ID:", note_id)
        return jsonify({"error": "Note not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
