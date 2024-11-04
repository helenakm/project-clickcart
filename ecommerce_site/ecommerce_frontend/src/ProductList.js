import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        // Fetch products from the Django REST API
        axios.get('http://127.0.0.1:8000/api/products/')
            .then(response => {
                // console.log(response.data); 
                setProducts(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the products!", error);
            });
    }, []);

    return (
        <div>
            <h1>Products</h1>
            <div className="product-list">
                {products.map(product => (
                    <div key={product.id} className="product-card">
                        <h2>{product.name}</h2>
                        <p>{product.description}</p>
                        <p>Price: ${product.price}</p>
                        {product.image && (
                            <img 
                                src={`http://127.0.0.1:8000${product.image}`} 
                                alt={product.name} 
                                style={{ width: '200px', height: '200px' }} 
                            />
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
};

export default ProductList;
