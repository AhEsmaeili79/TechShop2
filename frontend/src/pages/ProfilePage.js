import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProfilePage = () => {
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchUserData = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        console.error('No token found');
        setError('No token found. Please log in again.');
        return;
      }

      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accounts/user/', {
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        setUserData(response.data);
      } catch (err) {
        console.error('Error fetching user data:', err);
        if (err.response && err.response.status === 401) {
          setError('Unauthorized access - possibly invalid token');
        } else {
          setError('Failed to fetch user data');
        }
      }
    };

    fetchUserData();
  }, []);

  return (
    <div className="container mt-4">
      <h2>Profile Page</h2>
      {error && <p className="text-danger">{error}</p>}
      {userData ? (
        <div>
          <p><strong>First Name:</strong> {userData.first_name}</p>
          <p><strong>Last Name:</strong> {userData.last_name}</p>
          <p><strong>Email:</strong> {userData.email}</p>
        </div>
      ) : (
        <p>Loading user data...</p>
      )}
    </div>
  );
};

export default ProfilePage;
