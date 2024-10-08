import React, { lazy, Suspense } from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';

import Loading from '../src/pages/Loading';
import './App.css';
import Introduction from './pages/Introduction';
import CareerList from './pages/CareerList';

const Main = lazy(() => import('../src/pages/Main'));

function App() {
  return (
    <Suspense fallback={<Loading/>}> 
      <BrowserRouter>
        <Routes>
           <Route path = "/" element={<Main  />} />
           <Route path = "/introduction" element={<Introduction />}/>
           <Route path = "/careerlist" element={<CareerList />}/>
        </Routes>
      </BrowserRouter>
    </Suspense>
  );
};

export default App;
