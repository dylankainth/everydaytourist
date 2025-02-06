/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./node_modules/flowbite/**/*.{js,ts}"
  ],
  theme: {
    extend: {
      colors: {
        celadon: {
          100: '#E5FBE6',
          200: '#CCF7CE',
          300: '#B0F2B4', // Original
          400: '#90DB96',
          500: '#6FB877',
          600: '#4D9457',
          700: '#2F6F38',
          800: '#184D20',
        },
        celeste: {
          100: '#E8FCF9',
          200: '#D2F9F3',
          300: '#BAF2E9', // Original
          400: '#93D7CB',
          500: '#6FB8AC',
          600: '#4D9488',
          700: '#2F6F64',
          800: '#184D41',
        },
        columbia: {
          100: '#EEF7FC',
          200: '#D8ECF9',
          300: '#BAD7F2', // Original
          400: '#93B5D6',
          500: '#6F91B4',
          600: '#4D6E8F',
          700: '#2F4A6A',
          800: '#182C41',
        },
        orchid: {
          100: '#FCEEF2',
          200: '#F9D7DE',
          300: '#F2BAC9', // Original
          400: '#D693A3',
          500: '#B46F7E',
          600: '#8F4D5B',
          700: '#6A2F3C',
          800: '#411824',
        },
        dutch: {
          100: '#FFF9EC',
          200: '#FEF1D9',
          300: '#F2E2BA', // Original
          400: '#D6C496',
          500: '#B4A273',
          600: '#8F7D52',
          700: '#6A5B38',
          800: '#41361E',
        },
      },

      fontFamily: {
        sans: ['Poppins', 'ui-sans-serif', 'system-ui'],
      },
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

