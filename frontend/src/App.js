import React, { useState, useEffect } from 'react';
import NoteForm from './components/NoteForm';
import NotesList from './components/NotesList';
import './App.css';

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/notes')
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Error fetching notes: ' + response.status);
        }
      })
      .then((data) => setNotes(data))
      .catch((error) => console.error(error));
  }, []);

  const addNote = (title, content) => {
    const newNote = { title, content };
    fetch('http://127.0.0.1:5000/notes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newNote),
    })
      .then((response) => response.json())
      .then((data) => {
        setNotes([...notes, data]);
      })
      .catch((error) => console.error('Error adding note:', error));
  };

  const deleteNote = (index) => {
    const id = notes[index].id;
    fetch(`http://127.0.0.1:5000/notes/${id}`, {
      method: 'DELETE',
    })
      .then((response) => {
        if (response.ok) {
          setNotes(notes.filter((note, i) => i !== index));
        } else {
          console.error('Error deleting note:', response.statusText);
        }
      })
      .catch((error) => console.error('Error deleting note:', error));
  };

  return (
    <div className="App">
      <h1>Notes</h1>
      <NoteForm addNote={addNote} />
      <div className="notes-list">
        <NotesList notes={notes} deleteNote={deleteNote} />
      </div>
    </div>
  );
}

export default App;