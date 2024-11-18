import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ProductReviews.css'; 

const ProductReviews = ({ productId }) => {
    const [reviews, setReviews] = useState([]);
    const [newReview, setNewReview] = useState({ rating: '', comment: '' });
    const [error, setError] = useState(null);

    useEffect(() => {
        // Fetch reviews for the specific product
        axios.get(`http://localhost:8000/products/api/products/${productId}/reviews/`)
            .then(response => {
                setReviews(response.data);
            })
            .catch(error => {
                console.error("Error fetching reviews:", error);
            });
    }, [productId]);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewReview({ ...newReview, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!newReview.rating || !newReview.comment) {
            setError("All fields are required.");
            return;
        }

        axios.post(`http://localhost:8000/products/api/add_review/`, {
            product_id: productId,
            rating: newReview.rating,
            comment: newReview.comment
        }, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), 
            }
        })
            .then(response => {
                setReviews([...reviews, response.data]);
                setNewReview({ rating: '', comment: '' });
                setError(null);
            })
            .catch(error => {
                console.error("Error adding review:", error);
                setError("Failed to add review. Please try again.");
            });
    };

    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    return (
        <div>
            <h2>Reviews for Product {productId}</h2>
            <div className="review-list">
                {reviews.length > 0 ? (
                    reviews.map(review => (
                        <div key={review.id} className="review-card">
                            <p><strong>{review.user}</strong></p>
                            <p>Rating: {review.rating}/5</p>
                            <p>{review.comment}</p>
                            <small>Posted on: {new Date(review.created_at).toLocaleDateString()}</small>
                        </div>
                    ))
                ) : (
                    <p>No reviews available.</p>
                )}
            </div>
            <div className="review-form">
                <h3>Add a Review</h3>
                {error && <p className="error-message">{error}</p>}
                <form onSubmit={handleSubmit}>
                    <div>
                        <label htmlFor="rating">Rating (1-5):</label>
                        <input
                            type="number"
                            id="rating"
                            name="rating"
                            value={newReview.rating}
                            onChange={handleInputChange}
                            min="1"
                            max="5"
                        />
                    </div>
                    <div>
                        <label htmlFor="comment">Comment:</label>
                        <textarea
                            id="comment"
                            name="comment"
                            value={newReview.comment}
                            onChange={handleInputChange}
                        />
                    </div>
                    <button type="submit">Submit Review</button>
                </form>
            </div>
        </div>
    );
};

export default ProductReviews;
