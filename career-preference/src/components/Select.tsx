// Select.tsx
import React from "react";

interface SelectProps {
  placeholder: string;
  values: string[];
}

const Select: React.FC<SelectProps> = ({ placeholder, values }) => {
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

export default Select;
