
import React from 'react';
import '../styles/SelectionButton.css';

const SelectionButton = ({ isSelected, onSelect, label }) => {
  const handleClick = () => {
    onSelect(!isSelected);
  };

  return (
    <button
      onClick={handleClick}
      className={`selection-button ${isSelected ? 'selected' : ''}`}
    >
      {isSelected ? label : label}
    </button>
  );
};

export default SelectionButton;
