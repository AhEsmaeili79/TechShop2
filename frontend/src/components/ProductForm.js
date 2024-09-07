import React, { useState, useEffect } from 'react';

const ProductForm = ({ product, onSave, onCancel }) => {
  const [name, setName] = useState(product ? product.name : '');
  const [price, setPrice] = useState(product ? product.price : '');

  useEffect(() => {
    if (product) {
      setName(product.name);
      setPrice(product.price);
    }
  }, [product]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave({ ...product, name, price });
  };

  return (
    <form onSubmit={handleSubmit} className="container mt-4">
      <h2>{product ? 'ویرایش محصول' : 'افزودن محصول'}</h2>
      <div className="form-group">
        <input
          type="text"
          className="form-control"
          placeholder="نام محصول"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>
      <div className="form-group">
        <input
          type="number"
          className="form-control"
          placeholder="قیمت"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
          required
        />
      </div>
      <button type="submit" className="btn btn-primary">ذخیره</button>
      <button type="button" className="btn btn-secondary" onClick={onCancel}>لغو</button>
    </form>
  );
};

export default ProductForm;
