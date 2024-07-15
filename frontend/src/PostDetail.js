// frontend/src/PostDetail.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function PostDetail() {
    const { id } = useParams();
    const [post, setPost] = useState(null);

    useEffect(() => {
        axios.get(`/api/blog_posts/${id}/`)
            .then(response => setPost(response.data))
            .catch(error => console.error('Error fetching blog post:', error));
    }, [id]);

    if (!post) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{post.title}</h1>
            <img src={post.image} alt={post.title} />
            <p>{post.content}</p>
        </div>
    );
}

export default PostDetail;
