/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        text: "#070b0e",
        background: "#f4f9fb",
        primary: "#0aa1ff",
        secondary: "#8ac8ef",
        accent: "#4bb5f7",
        card: "#e8edef",
      },
    },
  },
  plugins: [
    // eslint-disable-next-line no-undef
    require("daisyui"),
    function ({ addComponents }) {
      const newComponents = {
        ".btnNav": {
          "@apply bg-[#0aa1ff] text-white text-sm": {},
        },
      };
      addComponents(newComponents);
    },
  ],
  daisyui: {
    themes: ["emerald"],
  },
};
