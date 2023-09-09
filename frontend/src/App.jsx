import { Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Registration from './pages/Registration';
import HomePage from './pages/HomePage';
import Login from './pages/Login';

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Registration />} />
      </Routes>
    </>
  );
}

export default App;
