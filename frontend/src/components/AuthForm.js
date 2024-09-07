import React, { useState } from 'react';

const AuthForm = ({ type, onSubmit }) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [password2, setPassword2] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Call onSubmit with appropriate data based on form type
    if (type === 'Login') {
      onSubmit({ email, password });
    } else {
      onSubmit({ first_name: firstName, last_name: lastName, email, password, password2 });
    }
  };

  return (
    <div className="container mt-4">
      <form onSubmit={handleSubmit} className="p-4 border rounded shadow">
        <h2>{type === 'Login' ? 'ورود' : 'ثبت‌نام'}</h2>
        {type === 'Signup' && (
          <>
            <div className="form-group">
              <input
                type="text"
                className="form-control"
                placeholder="نام"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
            </div>
            <div className="form-group">
              <input
                type="text"
                className="form-control"
                placeholder="نام خانوادگی"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
              />
            </div>
          </>
        )}
        <div className="form-group">
          <input
            type="email"
            className="form-control"
            placeholder="ایمیل"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <input
            type="password"
            className="form-control"
            placeholder="رمز عبور"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        {type === 'Signup' && (
          <div className="form-group">
            <input
              type="password"
              className="form-control"
              placeholder="تکرار رمز عبور"
              value={password2}
              onChange={(e) => setPassword2(e.target.value)}
              required
            />
          </div>
        )}
        <button type="submit" className="btn btn-primary">
          {type === 'Login' ? 'ورود' : 'ثبت‌نام'}
        </button>
      </form>
    </div>
  );
};

export default AuthForm;
