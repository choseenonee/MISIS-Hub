import { Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Registration from './pages/Registration';
import HomePage from './pages/HomePage';
import Login from './pages/Login';
import Forms from './pages/Forms';

function App() {
  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Registration />} />
        <Route path="/forms" element={<Forms />} />
      </Routes>
    </>
  );
}

export default App;
