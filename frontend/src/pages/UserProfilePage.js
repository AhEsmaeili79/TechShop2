import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const UserProfilePage = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserData = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accounts/user/', {
          headers: {
            'Authorization': `Token ${token}`,
          },
        });
        setUser(response.data);
      } catch (err) {
        console.error(err);
      }
    };

    fetchUserData();
  }, []);

  const handleUpdateClick = () => {
    navigate('/update-profile'); // Redirect to the UpdateProfilePage
  };

  return (
    <div className="container mt-4">
      {user ? (
        <div>
          <h1>User Profile</h1>
          <p><strong>First Name:</strong> {user.first_name}</p>
          <p><strong>Last Name:</strong> {user.last_name}</p>
          <p><strong>Email:</strong> {user.email}</p>
          {/* Add more profile details as needed */}
          <button className="btn btn-primary mt-3" onClick={handleUpdateClick}>
            Update Profile
          </button>
        </div>
      ) : (
        <p>Loading profile data...</p>
      )}
    </div>
  );
};

export default UserProfilePage;
