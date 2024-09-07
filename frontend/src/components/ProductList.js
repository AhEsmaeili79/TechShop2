import React from 'react';

const ProductList = ({ products, onEdit, onDelete }) => {
  return (
    <div className="container mt-4">
      <h2>محصولات</h2>
      <ul className="list-group">
        {products.map((product) => (
          <li className="list-group-item d-flex justify-content-between align-items-center" key={product.id}>
            {product.name} - ${product.price}
            <div>
              <button className="btn btn-warning btn-sm ml-2" onClick={() => onEdit(product)}>ویرایش</button>
              <button className="btn btn-danger btn-sm ml-2" onClick={() => onDelete(product.id)}>حذف</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
