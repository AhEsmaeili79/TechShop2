import { useState, useEffect } from 'react';
import axios from 'axios';

const useProtectedData = () => {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProtectedData = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        setError('No token found');
        return;
      }
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

    fetchProtectedData();
  }, []);

  return { data, error };
};

export default useProtectedData;
