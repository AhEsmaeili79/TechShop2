// src/pages/ProtectedDataPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProtectedDataPage = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  const fetchProtectedData = async () => {
    const token = localStorage.getItem('token');
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/protected/', {
        headers: {
          'Authorization': `Token ${token}`,
        },
      });
      setData(response.data);
    } catch (err) {
      setError('Failed to fetch protected data');
    }
  };

  useEffect(() => {
    fetchProtectedData();
  }, []);

  return (
    <div>
      <h2>Protected Data</h2>
      {error && <div className="alert alert-danger">{error}</div>}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ProtectedDataPage;
