import React from 'react';

function NoteItem({ note, deleteNote }) {
  return (
    <div className="note-item">
      <h3>{note.title}</h3>
      <p>{note.content}</p>
      <button onClick={() => deleteNote(note.id)}>🗑️</button>
    </div>
  );
}

export default NoteItem;
