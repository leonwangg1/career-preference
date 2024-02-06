// Input.tsx
import React from "react";

interface InputProps {
  placeholder: string;
}

const Input: React.FC<InputProps> = ({ placeholder }) => {
  return (
    <input
      type="text"
      placeholder={placeholder}
      className="input input-bordered w-full text-sm"
      // onChange={handleChange}
    />
  );
};

export default Input;
