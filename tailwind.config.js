/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './**/templates/**/*.html',
    // Add paths to other apps if necessary
  ],
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.3s ease-in-out',
        typewriter: 'typewriter 5s steps(40) forwards',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        typewriter: {
          to: {
            left: "100%"
          }
        },
        blink: {
          '0%': {
            opacity: '0',
          },
          '0.1%': {
            opacity: '1',
          },
          '50%': {
            opacity: '1',
          },
          '50.1%': {
            opacity: '0',
          },
          '100%': {
            opacity: '0',
          },
        },
      },
      colors: {
        background: '#ffffff',
        text: '#000000',
        accent: {
          DEFAULT: '#cccccc',
          hover: '#999999',
          active: '#333333',
        },
        border: '#e5e5e5',
        disabled: '#777777',
      },
    },
  },
  plugins: [],
};
