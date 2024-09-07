import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import SignupPage from './pages/SignupPage';
import AppNavbar from './components/Navbar';
import LoginPage from './pages/LoginPage';
import UserProfilePage from './pages/UserProfilePage';
import LogoutPage from './pages/LogoutPage';
import HomePage from './pages/HomePage';
import UpdateProfilePage from './pages/UpdateProfilePage';
import ProtectedRoute from './components/ProtectedRoute';  // Ensure this path is correct

const App = () => {
  const token = localStorage.getItem('token');

  return (
    <Router>
      <Routes>
        {/* Only show the login and signup pages if the user is not logged in */}
        {!token ? (
          <>
            <Route path="/signup" element={<SignupPage />} />
            <Route path="/login" element={<LoginPage />} />
          </>
        ) : (
          // Redirect to home if already logged in
          <Route path="/login" element={<Navigate to="/home" />} />
        )}
        <Route path="/logout" element={<LogoutPage />} />
        <Route path="/home" element={<ProtectedRoute element={<HomePage />} />} />
        <Route path="/userprofile" element={<UserProfilePage />} />
        <Route path="/update-profile" element={<UpdateProfilePage />} />
        <Route path="/" element={<Navigate to="/home" />} />
      </Routes>
    </Router>
  );
};

export default App;
