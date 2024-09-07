import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

export const fetchProtectedData = async () => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.get(`${API_URL}protected/`, {
      headers: {
        'Authorization': `Token ${token}`,
      },
    });
    return response.data;
  } catch (err) {
    throw new Error('Failed to fetch protected data');
  }
};
