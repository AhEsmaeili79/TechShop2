import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import AuthForm from '../components/AuthForm';

const SignupPage = () => {
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSignup = async (credentials) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/accounts/signup/', credentials);
      const { token } = response.data;

      // Save token in localStorage
      localStorage.setItem('token', token);

      // Redirect to home page
      navigate('/home');
    } catch (err) {
      if (err.response && err.response.data) {
        setError(err.response.data.error || 'Signup failed. Please check your details.');
      } else {
        setError('Network error');
      }
      console.error(err);
    }
  };

  return (
    <div className="container mt-4">
      <AuthForm type="Signup" onSubmit={handleSignup} />
      {error && <div className="alert alert-danger mt-3">{error}</div>}
    </div>
  );
};

export default SignupPage;
