import React from 'react';
import { createRoot } from 'react-dom/client';
import 'whatwg-fetch';

import '../scss/main.scss';

function App() {
  return (
    <>
      <h1>Stationery Shop</h1>
      <p>
        Edit `react-app/js/main.jsx` and save to reload.
      </p>
    </>
  );
}

const container = document.getElementById('react-app');
const root = createRoot(container);
root.render(<App />);
