import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const LogoutPage = () => {
  const navigate = useNavigate();

  // Define the handleLogout function
  const handleLogout = () => {
    // Remove the token from localStorage
    localStorage.removeItem('token');
    
    // Redirect to login page after logout
    navigate('/login');
  };

  useEffect(() => {
    // Call handleLogout when the component mounts
    handleLogout();
  }, []);

  return <div>Logging out...</div>;
};

export default LogoutPage;
