import React from 'react';

const NotesList = ({ notes, deleteNote }) => {
  return (
    <div className="notes-list">
      {notes.map((note, index) => (
        <div key={index} className="note-item">
          <div>
            <h3>{note.title}</h3>
            <p>{note.content}</p>
          </div>
          <button onClick={() => deleteNote(index)}>Delete</button>
        </div>
      ))}
    </div>
  );
};

export default NotesList;