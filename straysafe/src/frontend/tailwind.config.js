/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,ts}"],
  theme: {
    extend: {
      colors: {
        sand: {
          400: "#bc9363",
          500: "#b5835a",
          600: "#9b6444",
        }
      },
    },
  },
  plugins: [],
};
