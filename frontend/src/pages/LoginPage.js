import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import AuthForm from '../components/AuthForm';

const LoginPage = () => {
  const [error, setError] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      // If the user is already logged in, redirect to home page
      navigate('/home');
    }
  }, [navigate]);

  const handleLogin = async (credentials) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', credentials);
      const { token } = response.data;
  
      // Save the token in localStorage
      localStorage.setItem('token', token);
      
      // Redirect to home page
      navigate('/home');
    } catch (err) {
      if (err.response && err.response.data) {
        setError(err.response.data.error || 'Login failed. Please check your credentials.');
      } else {
        setError('Network error');
      }
      console.error(err);
    }
  };
  
  return (
    <div className="container mt-4">
      <AuthForm type="Login" onSubmit={handleLogin} />
      {error && <div className="alert alert-danger mt-3">{error}</div>}
    </div>
  );
};

export default LoginPage;
