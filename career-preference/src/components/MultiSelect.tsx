// MultiSelect.tsx
import React from "react";

interface MultiSelectProps {
  placeholder: string;
  values: string[];
}

const MultiSelect: React.FC<MultiSelectProps> = ({ placeholder, values }) => {
  return (
    <select className="select select-bordered w-full text-sm">
      <option disabled selected>
        {placeholder}
      </option>
      {values.map((val, index) => (
        <option key={index}>{val}</option>
      ))}
    </select>
  );
};

export default MultiSelect;
