// Input.tsx
import React from "react";

interface InputProps {
  placeholder: string;
  limit: number;
}

const Input: React.FC<InputProps> = ({ placeholder, limit }) => {
  return (
    <input
      type="text"
      placeholder={placeholder}
      className="input input-bordered w-full text-sm"
      maxLength={limit}
    />
  );
};

export default Input;
