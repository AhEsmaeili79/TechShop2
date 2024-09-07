import React, { useState, useEffect } from 'react';

const UpdateProfileForm = ({ user, onSave, onCancel }) => {
  const [name, setName] = useState(user ? user.name : '');
  const [email, setEmail] = useState(user ? user.email : '');
  const [password, setPassword] = useState('');

  useEffect(() => {
    if (user) {
      setName(user.name);
      setEmail(user.email);
    }
  }, [user]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave({ ...user, name, email, password });
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <h2>به‌روزرسانی پروفایل</h2>
      <div className="form-group">
        <input
          type="text"
          className="form-control"
          placeholder="نام"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
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
          placeholder="رمز عبور (برای حفظ فعلی خالی بگذارید)"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <button type="submit" className="btn btn-primary">ذخیره</button>
      <button type="button" className="btn btn-secondary" onClick={onCancel}>لغو</button>
    </form>
  );
};

export default UpdateProfileForm;
