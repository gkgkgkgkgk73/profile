import React, { lazy, Suspense } from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';

import logo from './logo.svg';
import Loading from '../src/pages/Loading';
import './App.css';
import Introduction from './pages/Introduction';

const Main = lazy(() => import('../src/pages/Main'));

function App() {
  return (
    <Suspense fallback={<Loading/>}> 
      <BrowserRouter>
        <Routes>
           <Route path = "/" element={<Main />} />
           <Route path = "/introduction" element={<Introduction />}/>
        </Routes>
      </BrowserRouter>
    </Suspense>
  );
};

export default App;
