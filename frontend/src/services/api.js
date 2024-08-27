import axios from 'axios';

const API_URL = 'http://localhost:8000/api/'; // Django server URL

export const fetchUsers = async () => {
    try {
        const response = await axios.get(`${API_URL}users/`);
        return response.data;
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

// Define similar functions for other APIs
