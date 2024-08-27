import axios from 'axios';
import Cookies from 'js-cookie';

const instance = axios.create({
    baseURL: 'http://localhost:8000/',
    withCredentials: true,  // Ensure cookies are sent with requests
});

instance.interceptors.request.use(config => {
    const token = Cookies.get('csrftoken');  // Get CSRF token from cookies
    if (token) {
        config.headers['X-CSRFToken'] = token;  // Include CSRF token in request headers
    }
    return config;
}, error => {
    return Promise.reject(error);
});

export default instance;
